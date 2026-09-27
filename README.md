# AI E-Tutor — Agentic AI Career & Learning MVP

## What is included

- Minimal-input learner profiling from resume/LinkedIn text
- Goal discovery when the learner does not provide a goal
- Skill-gap analysis
- Adaptive roadmap generation
- Foundations, ML, Deep Learning, GenAI, Agentic AI, Computer Vision, Cloud AI Architecture, MLOps/Security and Career readiness
- Lightweight resource retrieval/RAG-style component
- Budget-aware free-resource filtering
- Evaluator/Evals scenarios
- FastAPI APIs
- Human approval gate before roadmap execution

## Run

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python run.py
```

Open:
http://127.0.0.1:8000/docs

Run evaluations:

```bash
python app/evals.py
```

## API examples

### JSON roadmap

POST `/roadmap`

```json
{
  "current_role": "Data Analyst",
  "current_skills": ["Python", "SQL"],
  "hours_per_week": 7,
  "monthly_budget": 0
}
```

### Resume roadmap

POST `/roadmap/from-resume` as multipart form:
- `file`: PDF/DOCX/TXT
- `goal`: optional
- `hours_per_week`: optional
- `budget`: optional

## Production upgrade path

1. Replace the local resource catalog with PostgreSQL + pgvector.
2. Add an LLM provider and structured output.
3. Replace direct orchestration with Microsoft Agent Framework workflows.
4. Add MCP tool servers for web/search/calendar/GitHub/code execution.
5. Add A2A for external agent interoperability.
6. Add OAuth/OIDC, WAF, PII redaction and a tool firewall.
7. Add Redis/event bus and persistent learner memory.
8. Add OpenTelemetry tracing.
9. Add comprehensive agent/workflow/RAG/security Evals.
10. Add Next.js dashboard + embedded tutor chat.
