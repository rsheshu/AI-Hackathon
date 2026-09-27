from typing import List, Dict
import re

class ResourceRAG:
    """
    Lightweight local RAG-like retriever for the MVP.
    Replace with pgvector/FAISS/Chroma in production.
    """

    def __init__(self):
        self.resources = [
            {"title":"Python Official Tutorial", "skill":"Python", "cost":0, "format":"docs", "url":"https://docs.python.org/3/tutorial/"},
            {"title":"Kaggle Learn", "skill":"Machine Learning", "cost":0, "format":"interactive", "url":"https://www.kaggle.com/learn"},
            {"title":"Hugging Face Course", "skill":"Transformers", "cost":0, "format":"course", "url":"https://huggingface.co/learn"},
            {"title":"PyTorch Tutorials", "skill":"Deep Learning", "cost":0, "format":"docs", "url":"https://pytorch.org/tutorials/"},
            {"title":"OpenCV Tutorials", "skill":"Computer Vision", "cost":0, "format":"docs", "url":"https://docs.opencv.org/"},
            {"title":"AWS Machine Learning", "skill":"AWS", "cost":0, "format":"docs", "url":"https://aws.amazon.com/machine-learning/"},
            {"title":"Microsoft Learn AI", "skill":"Azure", "cost":0, "format":"course", "url":"https://learn.microsoft.com/training/"},
            {"title":"Google Cloud AI", "skill":"GCP", "cost":0, "format":"docs", "url":"https://cloud.google.com/learn"},
        ]

    def search(self, skills: List[str], budget: int, limit: int = 10) -> List[Dict]:
        hits = []
        for r in self.resources:
            if any(re.search(re.escape(s), r["skill"], re.I) for s in skills):
                if r["cost"] <= budget:
                    hits.append(r)
        return hits[:limit]
