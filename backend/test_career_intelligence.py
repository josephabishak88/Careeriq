from app.services.career_intelligence import generate_career_intelligence


candidate_text = """
Final-year B.Tech Computer Science and Engineering student
with skills in Python, Machine Learning, FastAPI, XGBoost
and Data Science. Interested in AI and Data Science roles.
"""


result = generate_career_intelligence(
    candidate_text=candidate_text,

    job_title="Credit Card Bill Payments Growth",
    company="CRED",

    required_skills=[
        "product analytics",
        "experimentation",
        "data analysis",
        "machine learning"
    ],

    matched_skills=[
        "machine learning",
        "data analysis"
    ],

    missing_skills=[
        "product analytics",
        "experimentation"
    ],

    skill_score=50.0,
    semantic_score=72.5,
    final_score=59.0
)


print("\n===== CAREERIQ CAREER INTELLIGENCE =====\n")

print(result)