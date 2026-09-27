from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
import shutil

from .orchestrator import TutorOrchestrator
from .models import LearnerRequest

app = FastAPI(title="AI E-Tutor", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

orchestrator = TutorOrchestrator()

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-etutor"}

@app.post("/roadmap")
async def create_roadmap(request: LearnerRequest):
    return await orchestrator.build_roadmap(request)

@app.post("/roadmap/from-resume")
async def roadmap_from_resume(
    file: UploadFile = File(...),
    goal: str | None = Form(None),
    hours_per_week: int = Form(7),
    budget: int = Form(0)
):
    if not file.filename:
        raise HTTPException(400, "File is required")
    suffix = Path(file.filename).suffix.lower()
    if suffix not in {".pdf", ".docx", ".txt"}:
        raise HTTPException(400, "Only PDF, DOCX and TXT are supported")
    temp = Path("/tmp") / f"etutor_{file.filename}"
    with temp.open("wb") as out:
        shutil.copyfileobj(file.file, out)

    request = LearnerRequest(
        goal=goal,
        hours_per_week=hours_per_week,
        monthly_budget=budget,
        resume_path=str(temp)
    )
    return await orchestrator.build_roadmap(request)
