from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text(path: str) -> str:
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        return "\n".join(page.extract_text() or "" for page in PdfReader(str(p)).pages)
    if p.suffix.lower() == ".docx":
        return "\n".join(x.text for x in Document(str(p)).paragraphs)
    return p.read_text(encoding="utf-8", errors="ignore")

def basic_profile(text: str) -> dict:
    low = text.lower()
    known = [
        "python","sql","pandas","spark","databricks","machine learning",
        "deep learning","tensorflow","pytorch","llm","rag","langchain",
        "computer vision","opencv","aws","azure","gcp","docker","kubernetes",
        "tableau","power bi","airflow","git"
    ]
    skills = [s for s in known if s in low]
    roles = ["data analyst", "data engineer", "software engineer", "developer",
             "data scientist", "machine learning engineer", "business analyst"]
    role = next((r for r in roles if r in low), "Technology Professional")
    return {"role": role.title(), "skills": skills, "responsibilities": []}
