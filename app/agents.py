from .models import LearnerProfile, GoalProposal
from .resume_parser import extract_text, basic_profile
from .skill_repository import all_skills

class ProfilerAgent:
    def run(self, resume_path=None, linkedin_text=None, role=None, skills=None):
        data = {"role": role or "Unknown", "skills": skills or [], "responsibilities": []}
        text = linkedin_text or ""
        if resume_path:
            text += "\n" + extract_text(resume_path)
        if text:
            parsed = basic_profile(text)
            if data["role"] == "Unknown":
                data["role"] = parsed["role"]
            data["skills"] = sorted(set(data["skills"] + parsed["skills"]))
        return LearnerProfile(**data)

class GoalAgent:
    def run(self, profile: LearnerProfile, explicit_goal=None):
        if explicit_goal:
            return GoalProposal(
                primary_goal=explicit_goal,
                alternatives=[],
                rationale=["Goal explicitly supplied by learner."]
            )

        role = profile.role.lower()
        if "data analyst" in role or "business analyst" in role:
            primary = "AI/GenAI-enabled Data Analyst"
            alternatives = ["GenAI Engineer", "AI Product Analyst"]
        elif "data engineer" in role:
            primary = "AI Data Engineer / GenAI Data Platform Engineer"
            alternatives = ["GenAI Engineer", "ML Engineer"]
        elif "software engineer" in role or "developer" in role:
            primary = "GenAI / AI Engineer"
            alternatives = ["Agentic AI Engineer", "ML Engineer"]
        else:
            primary = "AI/GenAI Engineer"
            alternatives = ["AI Application Developer", "AI Product Specialist"]

        return GoalProposal(
            primary_goal=primary,
            alternatives=alternatives,
            rationale=[
                f"Aligned with current role: {profile.role}.",
                "Uses transferable technical skills before adding new AI capabilities.",
                "Can be adapted to available weekly learning time."
            ]
        )

class SkillGapAgent:
    def run(self, profile: LearnerProfile, goal: str):
        role_text = goal.lower()
        required = []
        if "data" in role_text:
            required += ["Python", "SQL", "Statistics", "Machine Learning"]
        required += ["LLMs", "RAG", "Agentic AI", "Computer Vision", "Cloud", "MLOps", "AI Security"]
        known = {x.lower() for x in profile.skills}
        return [s for s in required if s.lower() not in known]

class RoadmapAgent:
    def run(self, goal: str, gap: list, hours_per_week: int):
        phases = [
            ("AI Foundations", ["Python", "SQL", "Statistics"]),
            ("Machine Learning", ["Machine Learning", "Model Evaluation"]),
            ("Deep Learning", ["Neural Networks", "PyTorch"]),
            ("Generative AI", ["LLMs", "Transformers", "Embeddings", "RAG"]),
            ("Agentic AI", ["Tool Calling", "MCP", "A2A", "Memory", "Agent Evals"]),
            ("Computer Vision", ["CNNs", "Vision Transformers", "YOLO", "OCR", "Multimodal AI"]),
            ("Cloud AI Architecture", ["AWS/Azure/GCP", "Docker", "Kubernetes", "IAM", "Scalable AI Architectures"]),
            ("Production & Security", ["MLOps", "LLMOps", "Observability", "AI Security"]),
            ("Portfolio & Jobs", ["Production AI Project", "System Design", "Interview Preparation"])
        ]
        filtered = []
        gapset = {x.lower() for x in gap}
        for i, (title, skills) in enumerate(phases, 1):
            relevant = [s for s in skills if s.lower() in gapset or title.lower() in goal.lower()]
            if relevant or i in (4,5,8,9):
                filtered.append((i, title, skills))
        weekly = max(4, hours_per_week)
        hours_per_phase = max(week := 3, round(week * 1.5))
        from .models import RoadmapPhase
        return [
            RoadmapPhase(
                phase=i, title=title, skills=skills,
                hours=hours_per_phase,
                outcome=f"Demonstrate {title} through practice and a small project."
            )
            for i, title, skills in filtered
        ]

class EvaluatorAgent:
    def run(self, roadmap):
        issues = []
        if not roadmap:
            issues.append("Roadmap is empty.")
        if len(roadmap) < 4:
            issues.append("Roadmap has too few phases.")
        required_domains = {"Generative AI","Agentic AI","Computer Vision","Cloud AI Architecture"}
        titles = {x.title for x in roadmap}
        issues.extend([f"Missing domain: {d}" for d in required_domains if d not in titles])
        return {"passed": not issues, "issues": issues}
