from app.services.career_strategy import generate_career_strategy


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science",
    "Artificial Intelligence"
]


target_role = "Machine Learning Engineer"


missing_skills = [
    "LLM",
    "RAG",
    "NLP",
    "SQL",
    "Docker",
    "Model Optimization",
    "Monitoring",
    "Prompt Engineering"
]


career_intelligence = """
The candidate has a strong foundation in Python,
Machine Learning and Data Science.

The candidate is a final-year B.Tech student.

The candidate matches some core requirements for
Machine Learning roles but has gaps in modern
LLM, RAG, NLP and production-oriented skills.
"""


print("\n===== CAREERIQ CAREER STRATEGY TEST =====")


strategy = generate_career_strategy(
    candidate_skills=candidate_skills,
    target_role=target_role,
    missing_skills=missing_skills,
    career_intelligence=career_intelligence
)


print("\n===== CAREER STRATEGY =====")
print(strategy)