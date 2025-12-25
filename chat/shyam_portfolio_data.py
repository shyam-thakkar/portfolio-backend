"""
Shyam Thakkar's Portfolio Data for RAG System
This file contains structured information about Shyam Thakkar for the chatbot
"""

SHYAM_PORTFOLIO_DATA = [
    # ===== ABOUT ME =====
    {
        "category": "about",
        "title": "Introduction",
        "text": """I'm Shyam Thakkar, a Gen AI Developer and Product Builder. I'm the creator of AIFolio.in — 
        I build production-grade AI products using Python with Django and FastAPI for backend. I specialize 
        in Gen AI applications with LangChain and LangGraph, creating intelligent SaaS solutions powered by AI. 
        I have 1.5 years of experience and have worked on 10+ GenAI projects. I'm based in Ahmedabad, Gujarat, India.""",
        "source": "portfolio"
    },
    {
        "category": "about",
        "title": "Professional Summary",
        "text": """I'm currently working as an SDE-1 (GenAI Developer) at WeServeCodes Pvt Ltd, where I engineer 
        AI-driven automation systems and build robust data-extraction pipelines. I have experience in 
        developing RAG systems, custom tool-call frameworks for LLMs, and dynamic content-generation 
        workflows. My background includes AI/ML internships and data analysis roles. My flagship product 
        is AIFolio.in, an AI-powered portfolio publishing platform that I built and launched.""",
        "source": "resume"
    },
    {
        "category": "about",
        "title": "Contact Information",
        "text": """You can reach me at work.shyamthakkar@gmail.com or call me at +91 9979194059. 
        I'm also active on LinkedIn and GitHub. I'm based in Ahmedabad, Gujarat, India. 
        You can check out my flagship product AIFolio at aifolio.in.""",
        "source": "resume"
    },
    
    # ===== EDUCATION =====
    {
        "category": "education",
        "title": "Bachelor's Degree - Computer Engineering",
        "text": """I completed my Bachelor's degree in Computer Engineering from G H Patel College of 
        Engineering and Technology (GCET) in Anand, India, from 2021 to 2025. I graduated with 
        a CGPA of 8.73, demonstrating strong academic performance throughout my undergraduate studies.""",
        "source": "resume"
    },
    
    # ===== TECHNICAL SKILLS =====
    {
        "category": "skills",
        "title": "Programming Languages",
        "text": """I am proficient in multiple programming languages including Python (my primary language), 
        JavaScript, C++, C, and Java. I use Python extensively for AI/ML development, backend systems, 
        and automation. JavaScript for web development, and C++/Java for systems programming and 
        algorithmic problem-solving.""",
        "source": "resume"
    },
    {
        "category": "skills",
        "title": "AI/ML Frameworks and Libraries",
        "text": """I have extensive experience with AI/ML frameworks including Django, LangChain, LangGraph, 
        TensorFlow, Keras, PyTorch, and OpenCV. I specialize in LangChain and LangGraph for building 
        LLM applications and RAG systems. I use TensorFlow, Keras, and PyTorch for deep learning models, 
        and OpenCV for computer vision applications.""",
        "source": "resume"
    },
    {
        "category": "skills",
        "title": "Web Development and Automation",
        "text": """I work with web frameworks like Django and FastAPI for building backend systems and APIs. 
        For frontend development and data apps, I use Streamlit. I'm experienced with web automation 
        using Selenium and Playwright for scraping, testing, and automated workflows.""",
        "source": "resume"
    },
    {
        "category": "skills",
        "title": "Tools and Technologies",
        "text": """My technical toolkit includes Git for version control, Docker for containerization, 
        Vector Databases (like Weaviate, pgvector) for RAG systems, SQL for database management, 
        and various tools for RAG Systems development, Prompt Engineering, LLM Evaluation, OCR, 
        Data Cleaning, Preprocessing, and Visualization. I also build and consume RESTful APIs.""",
        "source": "resume"
    },
    {
        "category": "skills",
        "title": "GenAI and LLM Expertise",
        "text": """I specialize in Generative AI and Large Language Models. My expertise includes building 
        RAG (Retrieval-Augmented Generation) systems, prompt engineering, LLM evaluation, custom 
        tool-call frameworks, and integrating LLMs with business logic. I work with various LLM 
        models including LLaMA 3, DeepSeek R1, and commercial APIs.""",
        "source": "resume"
    },
    
    # ===== WORK EXPERIENCE =====
    {
        "category": "experience",
        "title": "WeServeCodes Pvt Ltd - SDE-1 (GenAI Developer)",
        "text": """I'm currently working as an SDE-1 (GenAI Developer) at WeServeCodes Pvt Ltd since June 2025. 
        In this role, I engineer AI-driven automation systems by integrating LLMs with complex business 
        logic, enabling natural-language instructions to trigger reliable, validated actions across 
        internal platforms. I build robust data-extraction and validation pipelines that combine web 
        automation, structured LLM output, and real-time API checks to ensure accuracy, consistency, 
        and trust in generated data. I design and implement custom tool-call frameworks allowing LLMs 
        to safely interact with external APIs, verify user-provided inputs, and request missing or 
        corrected information when required. I also develop dynamic content-generation workflows powered 
        by rule-based logic and LLM capabilities, improving data quality, operational efficiency, and 
        automation across business processes.""",
        "source": "resume"
    },
    {
        "category": "experience",
        "title": "CrossShores Infotech - AI/ML Intern",
        "text": """I worked as an AI/ML Intern at CrossShores Infotech from December 2024 to June 2025. 
        During this internship, I developed an in-house API for background removal, designed for 
        cleaning logos and product images using BiRefNet and open-source Rembg, eliminating the need 
        for third-party services and reducing client costs by 7%. I designed and implemented a 
        Candidate Filtering RAG System using LLM-based prompt engineering, hybrid retrievers, and 
        CrossEncoder rerankers, enabling accurate matching of resumes to job descriptions through an 
        ensemble of SelfQueryRetriever, ideal JD generation using LLaMA 3, and key detail extraction 
        using DeepSeek R1. I built a modular pipeline incorporating question generation, JSON-based 
        metadata filtering, and vector store retrieval using Weaviate to optimize relevance scoring 
        and document reranking.""",
        "source": "resume"
    },
    {
        "category": "experience",
        "title": "Tech Elecon Pvt. Ltd. - Data Analyst Intern",
        "text": """I worked as a Data Analyst Intern at Tech Elecon Pvt. Ltd. from May 2024 to June 2024. 
        In this role, I developed an invoice reader project using optical character recognition (OCR) 
        technology to accurately read and display the contents of invoices. I also led a team of interns 
        on various projects, providing guidance and support to ensure successful project completion. 
        This experience helped me develop leadership skills and practical experience with OCR technology.""",
        "source": "resume"
    },
    
    # ===== PROJECTS =====
    {
        "category": "projects",
        "title": "Karate Kata Evaluation System",
        "text": """I designed and developed a Karate Kata Evaluation System using Google MoveNet and a custom 
        deep neural network for real-time pose detection and analysis. The system integrates TensorFlow, 
        OpenCV, Scikit-Learn, and Keras for posture assessment and movement analysis. I built and hosted 
        a user-friendly Streamlit interface for real-time feedback and performance evaluation, ensuring 
        accuracy through rigorous testing and optimization. The project demonstrates my expertise in 
        computer vision, deep learning, and building practical AI applications. You can try the live 
        demo at karatekataevaluation.streamlit.app and view the code on my GitHub.""",
        "source": "resume"
    },
    {
        "category": "projects",
        "title": "Stock Price Prediction System",
        "text": """I developed a real-time stock price prediction web application using Streamlit and LSTM 
        models for accurate 7-day forecasts, integrating real-time data sources. The project implements 
        data preprocessing and visualization with Pandas and NumPy to enhance user experience. I built 
        and trained an LSTM model using TensorFlow and Keras, employing a sliding window algorithm for 
        improved accuracy. This project showcases my skills in time series analysis, deep learning, 
        and building interactive data applications.""",
        "source": "resume"
    },
    {
        "category": "projects",
        "title": "Candidate Filtering RAG System",
        "text": """At CrossShores Infotech, I designed and implemented a sophisticated Candidate Filtering 
        RAG System that uses LLM-based prompt engineering, hybrid retrievers, and CrossEncoder rerankers 
        to match resumes with job descriptions accurately. The system uses an ensemble approach combining 
        SelfQueryRetriever, ideal job description generation with LLaMA 3, and key detail extraction 
        using DeepSeek R1. I built a modular pipeline with question generation, JSON-based metadata 
        filtering, and vector store retrieval using Weaviate for optimized relevance scoring and 
        document reranking. This project demonstrates my expertise in building production-ready RAG 
        systems.""",
        "source": "resume"
    },
    {
        "category": "projects",
        "title": "Background Removal API",
        "text": """I developed an in-house API for background removal at CrossShores Infotech, designed 
        specifically for cleaning logos and product images. The API uses BiRefNet and open-source 
        Rembg models, eliminating the need for expensive third-party services and reducing client 
        costs by 7%. This project showcases my ability to build cost-effective AI solutions that 
        provide real business value.""",
        "source": "resume"
    },
    {
        "category": "projects",
        "title": "Invoice Reader OCR System",
        "text": """At Tech Elecon Pvt. Ltd., I developed an invoice reader project using optical character 
        recognition (OCR) technology to accurately read and display the contents of invoices. The 
        system automates the extraction of key information from invoices, improving efficiency and 
        reducing manual data entry errors. This project demonstrates my practical experience with 
        OCR technology and document processing.""",
        "source": "resume"
    },
    {
        "category": "projects",
        "title": "Portfolio RAG Chatbot",
        "text": """I built an intelligent chatbot for my portfolio website using RAG (Retrieval-Augmented 
        Generation) technology. The system uses Django Channels for WebSocket connections, PostgreSQL 
        with pgvector for vector storage, LangChain for RAG orchestration, and OpenAI embeddings and 
        GPT models for generating responses. The chatbot features session management, allowing users 
        to have continuous conversations, and can answer questions about my experience, skills, and 
        projects based on semantic search through my portfolio data. This project showcases my 
        full-stack development skills and expertise in building production-ready RAG systems.""",
        "source": "portfolio"
    },
    
    # ===== ACHIEVEMENTS & HIGHLIGHTS =====
    {
        "category": "achievements",
        "title": "Cost Reduction Achievement",
        "text": """At CrossShores Infotech, I successfully reduced client costs by 7% by developing an 
        in-house background removal API that eliminated the need for expensive third-party services. 
        This demonstrates my ability to create cost-effective solutions that provide tangible business value.""",
        "source": "resume"
    },
    {
        "category": "achievements",
        "title": "Academic Excellence",
        "text": """I graduated with a CGPA of 8.73 from G H Patel College of Engineering and Technology, 
        demonstrating consistent academic excellence throughout my Bachelor's degree in Computer Engineering.""",
        "source": "resume"
    },
    {
        "category": "achievements",
        "title": "Leadership Experience",
        "text": """During my internship at Tech Elecon Pvt. Ltd., I led a team of interns on various projects, 
        providing guidance and support to ensure successful project completion. This experience developed 
        my leadership and mentoring skills.""",
        "source": "resume"
    },
    
    # ===== INTERESTS & SPECIALIZATIONS =====
    {
        "category": "interests",
        "title": "Areas of Expertise",
        "text": """My primary areas of expertise include Generative AI, Large Language Models (LLMs), 
        RAG (Retrieval-Augmented Generation) systems, AI automation, prompt engineering, and building 
        intelligent applications. I specialize in integrating LLMs with business logic, creating custom 
        tool-call frameworks, and developing data-extraction pipelines. I'm also experienced in computer 
        vision, deep learning, and building web applications.""",
        "source": "portfolio"
    },
    {
        "category": "interests",
        "title": "Technology Focus",
        "text": """I focus on cutting-edge AI technologies including LangChain, LangGraph, vector databases, 
        and various LLM models. I'm passionate about building practical AI solutions that solve real-world 
        problems, particularly in automation, data extraction, and intelligent content generation. I stay 
        updated with the latest developments in GenAI and continuously experiment with new tools and 
        techniques.""",
        "source": "portfolio"
    },
    
    # ===== AIFOLIO - FLAGSHIP PRODUCT =====
    {
        "category": "projects",
        "title": "AIFolio - AI-Powered Portfolio Publishing Platform",
        "text": """I built and launched AIFolio (aifolio.in), an AI-powered portfolio builder and publishing 
        platform that transforms a user's resume into a structured, editable portfolio and publishes it as 
        a live personal website on a unique subdomain (e.g., username.aifolio.in). The platform features 
        strong draft-publish separation, versioned publishing, and safe AI augmentation, ensuring users 
        retain full control over what is publicly visible while benefiting from AI-assisted content 
        generation. The system is production-grade, multi-tenant, and built with a focus on data isolation, 
        immutability, and user trust. This is my flagship product demonstrating end-to-end product ownership 
        and real-world GenAI integration.""",
        "source": "portfolio"
    },
    {
        "category": "projects",
        "title": "AIFolio - Core Philosophy and User Workflow",
        "text": """AIFolio is built around three core principles: (1) Nothing is public by default - all user 
        edits happen in draft mode and content is only visible publicly after an explicit publish action. 
        (2) Publishing is versioned and reversible - each publish creates an immutable snapshot, and users 
        can republish updates or unpublish without data loss. (3) AI assists but never overrides user intent - 
        AI-generated content is controlled, reviewable, and derived strictly from user-provided data. The 
        user workflow includes resume upload (PDF/DOCX), LLM-powered structured JSON extraction, real-time 
        split editor with draft preview, username selection for permanent identity, atomic versioned 
        publishing, and safe unpublish behavior with preserved drafts and snapshots.""",
        "source": "portfolio"
    },
    {
        "category": "projects",
        "title": "AIFolio - AI Features and RAG Chatbot",
        "text": """AIFolio includes powerful AI features: (1) AI Resume Structuring - uses LLM to transform 
        unstructured resume text into structured JSON for editing, publishing, and AI-powered features. 
        (2) AI Rewrite - section-aware, prompt-controlled rewriting assistance that is non-destructive and 
        applies only to drafts. (3) Portfolio-Aware Chatbot using Controlled RAG - on publish, the system 
        generates canonical 'user truths' from structured JSON, embeds them in a vector database with strict 
        user_id metadata. Retrieval enforces mandatory metadata filtering before vector similarity search, 
        guaranteeing multi-tenant isolation. On republish, all vectors are removed and fresh truths are 
        regenerated. The chatbot only answers questions grounded in published data and refuses queries 
        outside available information to prevent hallucination.""",
        "source": "portfolio"
    },
    {
        "category": "projects",
        "title": "AIFolio - Technical Architecture",
        "text": """AIFolio's technical stack includes: Frontend built with Next.js featuring real-time editor 
        and preview modes, Backend with Django-based APIs, Async Processing with background tasks for 
        extraction and AI generation, Vector Database for metadata-scoped RAG, Reverse Proxy with Nginx, 
        Process Management using PM2 for frontend and Gunicorn for backend, and Networking via Cloudflare 
        for SSL and wildcard subdomains. Key engineering challenges solved include draft vs live isolation, 
        atomic publishing, username uniqueness and reservation, multi-tenant AI safety, deterministic RAG 
        updates, preventing AI hallucination, safe unpublish behavior, and production-ready infrastructure 
        for subdomain-based SaaS with wildcard DNS routing.""",
        "source": "portfolio"
    },
    {
        "category": "achievements",
        "title": "AIFolio Product Launch",
        "text": """I successfully built and launched AIFolio (aifolio.in) as a complete production-grade 
        SaaS product. This demonstrates my ability to own a product end-to-end, from conception through 
        development to deployment. The project showcases real-world GenAI integration with safe and 
        explainable AI systems, multi-tenant architecture with proper data isolation, strong UX and 
        system thinking, and production deployment skills including subdomain-based routing, Cloudflare 
        integration, and scalable infrastructure.""",
        "source": "portfolio"
    },
]
