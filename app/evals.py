import asyncio
from .models import LearnerRequest
from .orchestrator import TutorOrchestrator

SCENARIOS = [
    LearnerRequest(current_role="Data Analyst", current_skills=["Python","SQL"], goal=None, hours_per_week=7, monthly_budget=0),
    LearnerRequest(current_role="Software Engineer", current_skills=["Python","Git"], goal="GenAI Engineer", hours_per_week=10, monthly_budget=2000),
    LearnerRequest(current_role="Mechanical Engineer", current_skills=[], goal=None, hours_per_week=5, monthly_budget=0),
]

async def run_evals():
    orch = TutorOrchestrator()
    results = []
    for i, scenario in enumerate(SCENARIOS, 1):
        result = await orch.build_roadmap(scenario)
        r = result["eval"]
        results.append({
            "scenario": i,
            "goal": result["goal_proposal"]["primary_goal"],
            "passed": r["passed"],
            "issues": r["issues"]
        })
    return results

if __name__ == "__main__":
    print(asyncio.run(run_evals()))
