from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class LearnerRequest(BaseModel):
    resume_path: Optional[str] = None
    linkedin_text: Optional[str] = None
    current_role: Optional[str] = None
    current_skills: List[str] = Field(default_factory=list)
    goal: Optional[str] = None
    hours_per_week: int = Field(default=7, ge=1, le=80)
    monthly_budget: int = Field(default=0, ge=0)

class LearnerProfile(BaseModel):
    role: str = "Unknown"
    experience_years: float = 0
    skills: List[str] = Field(default_factory=list)
    responsibilities: List[str] = Field(default_factory=list)
    education: List[str] = Field(default_factory=list)

class GoalProposal(BaseModel):
    primary_goal: str
    alternatives: List[str]
    rationale: List[str]

class RoadmapPhase(BaseModel):
    phase: int
    title: str
    skills: List[str]
    hours: int
    outcome: str

class Roadmap(BaseModel):
    goal: str
    target_weeks: int
    daily_minutes: int
    phases: List[RoadmapPhase]
    resources: List[Dict[str, Any]]
    daily_reminder: str
    motivation_message: str
