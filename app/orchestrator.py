from .models import LearnerRequest, Roadmap
from .agents import ProfilerAgent, GoalAgent, SkillGapAgent, RoadmapAgent, EvaluatorAgent
from .rag import ResourceRAG

class TutorOrchestrator:
    def __init__(self):
        self.profiler = ProfilerAgent()
        self.goal_agent = GoalAgent()
        self.gap_agent = SkillGapAgent()
        self.roadmap_agent = RoadmapAgent()
        self.evaluator = EvaluatorAgent()
        self.rag = ResourceRAG()

    async def build_roadmap(self, request: LearnerRequest):
        profile = self.profiler.run(
            request.resume_path, request.linkedin_text,
            request.current_role, request.current_skills
        )
        goal = self.goal_agent.run(profile, request.goal)
        gap = self.gap_agent.run(profile, goal.primary_goal)
        phases = self.roadmap_agent.run(goal.primary_goal, gap, request.hours_per_week)

        skills_for_resources = [s for p in phases for s in p.skills]
        resources = self.rag.search(skills_for_resources, request.monthly_budget)

        eval_result = self.evaluator.run(phases)

        # Human approval is intentionally represented as a gate in the response.
        return {
            "profile": profile.model_dump(),
            "goal_proposal": goal.model_dump(),
            "skill_gaps": gap,
            "roadmap": Roadmap(
                goal=goal.primary_goal,
                target_weeks=max(8, len(phases) * 3),
                daily_minutes=max(30, round(request.hours_per_week * 60 / 7)),
                phases=phases,
                resources=resources,
                daily_reminder="Your AI learning target is scheduled for today. Start with the next unfinished task.",
                motivation_message="Small, consistent AI projects compound into real industrial capability. Build something today.",
            ).model_dump(),
            "eval": eval_result,
            "next_action": "USER_APPROVAL_REQUIRED: Accept, Modify, or Reject the suggested goal/roadmap."
        }
