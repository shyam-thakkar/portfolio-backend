
from django.db import models
from pgvector.django import VectorField

class Document(models.Model):
    text = models.TextField()
    embedding = VectorField(dimensions=1536)  # Groq embedding dimension
