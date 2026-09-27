SKILLS = {
    "foundations": ["Python", "SQL", "Git", "Linux", "Mathematics", "Statistics"],
    "data": ["Pandas", "Data Engineering", "Spark", "Data Modeling"],
    "ml": ["Machine Learning", "Model Evaluation", "Feature Engineering"],
    "deep_learning": ["Neural Networks", "PyTorch", "Deep Learning"],
    "nlp": ["NLP", "Transformers", "Text Classification"],
    "genai": ["LLMs", "Prompt Engineering", "Embeddings", "RAG", "Fine-tuning"],
    "agentic_ai": ["Tool Calling", "MCP", "A2A", "Planning", "Memory", "Multi-Agent Systems", "Agent Evals"],
    "computer_vision": ["CNNs", "Vision Transformers", "Object Detection", "YOLO", "OCR", "Multimodal AI"],
    "cloud": ["AWS", "Azure", "GCP", "Docker", "Kubernetes", "Networking", "IAM",
              "Serverless", "Cloud AI Services", "Scalable AI Architectures"],
    "production": ["MLOps", "LLMOps", "APIs", "CI/CD", "Observability"],
    "security": ["Prompt Injection", "PII Protection", "AI Security", "AI Governance"],
    "career": ["System Design", "Portfolio", "GitHub", "Interview Preparation"]
}

def all_skills():
    return [x for values in SKILLS.values() for x in values]
