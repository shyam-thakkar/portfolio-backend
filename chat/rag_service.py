"""
RAG Service for Portfolio Chatbot using LangChain
Optimized for performance with caching and lazy loading
"""
import os
from typing import List, Dict, Any, Optional
from functools import lru_cache

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores.pgvector import PGVector
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document as LangChainDocument

from .models import Document


class RAGService:
    """
    Optimized RAG service with caching and lazy loading
    Uses Google embeddings and Groq LLM
    """
    
    def __init__(self):
        """Initialize with lazy loading for expensive operations"""
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        self.groq_api_key = os.getenv('GROQ_API_KEY')
        
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        
        # Cache expensive objects
        self._embeddings = None
        self._llm = None
        self._vector_store = None
        self._connection_string = None
        
        # Collection name for the vector store
        self.collection_name = "portfolio_documents"
    
    @property
    def embeddings(self):
        """Lazy load embeddings (768 dimensions)"""
        if self._embeddings is None:
            self._embeddings = GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004",
                google_api_key=self.google_api_key
            )
        return self._embeddings
    
    @property
    def llm(self):
        """Lazy load LLM (Groq - llama-3.3-70b-versatile)"""
        if self._llm is None:
            self._llm = ChatGroq(
                model="meta-llama/llama-prompt-guard-2-86m",
                temperature=0.7,
                max_tokens=500,
                groq_api_key=self.groq_api_key
            )
        return self._llm
    
    @property
    def connection_string(self) -> str:
        """Cache connection string"""
        if self._connection_string is None:
            from django.conf import settings
            db_config = settings.DATABASES['default']
            self._connection_string = (
                f"postgresql://{db_config['USER']}:{db_config['PASSWORD']}"
                f"@{db_config['HOST']}:{db_config['PORT']}/{db_config['NAME']}"
            )
        return self._connection_string
    
    def get_vector_store(self) -> PGVector:
        """Get cached vector store instance"""
        if self._vector_store is None:
            self._vector_store = PGVector(
                collection_name=self.collection_name,
                connection_string=self.connection_string,
                embedding_function=self.embeddings,
            )
        return self._vector_store
    
    def add_document(
        self,
        text: str,
        category: str,
        title: str = "",
        source: str = ""
    ) -> Document:
        """
        Add a document to both Django model and vector store
        
        Args:
            text: Document content
            category: Category (skills, projects, etc.)
            title: Optional title
            source: Optional source
            
        Returns:
            Created Document instance
        """
        # Generate embedding
        embedding = self.embeddings.embed_query(text)
        
        # Save to Django model
        doc = Document.objects.create(
            text=text,
            embedding=embedding,
            category=category,
            title=title,
            source=source
        )
        
        # Add to vector store
        langchain_doc = LangChainDocument(
            page_content=text,
            metadata={
                "id": doc.id,
                "category": category,
                "title": title,
                "source": source
            }
        )
        
        self.get_vector_store().add_documents([langchain_doc])
        
        return doc
    
    def similarity_search(
        self,
        query: str,
        top_k: int = 5,
        category: Optional[str] = None
    ) -> List[LangChainDocument]:
        """
        Perform similarity search
        
        Args:
            query: Search query
            top_k: Number of results to return
            category: Optional category filter
            
        Returns:
            List of LangChain Document objects
        """
        return self.get_vector_store().similarity_search(
            query,
            k=top_k,
            filter={"category": category} if category else None
        )
    
    @lru_cache(maxsize=128)
    def _get_prompt_template(self) -> PromptTemplate:
        """Cache prompt template"""
        template = """You are SHYAM-DEV-1, representing Shyam Thakkar's portfolio.

RESPONSE RULES:
1. ONLY answer questions about Shyam's professional profile (skills, experience, projects, education, contact)

2. For off-topic questions, respond: "I'm SHYAM-DEV-1, designed to answer questions about Shyam's professional background and technical expertise. Ask me about his skills, projects, or experience!"

3. Be DIRECT and CONFIDENT:
   ✓ "I'm a GenAI engineer at WeServeCodes"
   ✓ "I built a RAG system using LangChain"
   ✓ "I specialize in Python and LLM applications"
   
   ✗ "I can confirm that I work..."
   ✗ "I can say that I built..."
   ✗ "Yes, I have experience in..."

4. Keep responses natural and concise
5. Only use facts from the context below

Context:
{context}

Question: {question}

Answer:"""
        
        return PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
    
    def create_qa_chain(
        self,
        category: Optional[str] = None,
        top_k: int = 5
    ) -> RetrievalQA:
        """
        Create a LangChain RetrievalQA chain
        
        Args:
            category: Optional category filter
            top_k: Number of documents to retrieve
            
        Returns:
            RetrievalQA chain
        """
        # Create retriever
        search_kwargs = {"k": top_k}
        if category:
            search_kwargs["filter"] = {"category": category}
        
        retriever = self.get_vector_store().as_retriever(
            search_kwargs=search_kwargs
        )
        
        # Create QA chain
        return RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self._get_prompt_template()}
        )
    
    def process_query(
        self,
        query: str,
        top_k: int = 5,
        category: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process a user query using RAG pipeline
        
        Args:
            query: User's question
            top_k: Number of documents to retrieve
            category: Optional category filter
            
        Returns:
            Dictionary with response and metadata
        """
        try:
            # Create and run QA chain
            qa_chain = self.create_qa_chain(category=category, top_k=top_k)
            result = qa_chain.invoke({"query": query})
            
            # Extract response and source documents
            bot_response = result["result"]
            source_docs = result.get("source_documents", [])
            
            # Format sources efficiently
            sources = [
                {
                    "id": doc.metadata.get("id"),
                    "category": doc.metadata.get("category", ""),
                    "title": doc.metadata.get("title", ""),
                    "snippet": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
                }
                for doc in source_docs
            ]
            
            return {
                "response": bot_response,
                "sources": sources,
                "success": True
            }
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            return {
                "response": "I'm not able to process your query",
                "error": str(e),
                "sources": [],
                "success": False
            }
    
    def sync_documents_to_vectorstore(self) -> int:
        """
        Sync all Django documents to vector store (batch operation)
        Useful for initial setup or re-indexing
        
        Returns:
            Number of documents synced
        """
        # Batch fetch all documents
        all_docs = Document.objects.all().only('id', 'text', 'category', 'title', 'source')
        
        # Build langchain documents in batch
        langchain_docs = [
            LangChainDocument(
                page_content=doc.text,
                metadata={
                    "id": doc.id,
                    "category": doc.category,
                    "title": doc.title,
                    "source": doc.source
                }
            )
            for doc in all_docs
        ]
        
        if langchain_docs:
            # Batch add to vector store
            self.get_vector_store().add_documents(langchain_docs)
            print(f"✓ Synced {len(langchain_docs)} documents to vector store")
        else:
            print("No documents to sync")
        
        return len(langchain_docs)
