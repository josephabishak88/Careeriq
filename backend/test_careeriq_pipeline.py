from app.services.careeriq_pipeline import run_careeriq_pipeline


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science",
    "Artificial Intelligence"
]


candidate_text = """
Final-year B.Tech Computer Science and Engineering student
with skills in Python, Machine Learning, FastAPI, XGBoost,
Data Science and Artificial Intelligence.

Interested in AI, Machine Learning and Data Science roles.
"""


target_role = "Machine Learning Engineer"


query = """
AI machine learning data science Python
"""


print("\n===== CAREERIQ END-TO-END PIPELINE =====")


result = run_careeriq_pipeline(
    candidate_skills=candidate_skills,
    candidate_text=candidate_text,
    target_role=target_role,
    query=query,
    candidate_years=0,
    top_k=5
)


print("\n===== TOP JOBS =====")


for index, job in enumerate(
    result["jobs"],
    start=1
):

    print(f"\n--- Rank {index} ---")

    print(
        "Title:",
        job["title"]
    )

    print(
        "Company:",
        job["company"]
    )

    print(
        "Final Score:",
        job["final_score"]
    )

    print(
        "Matched Skills:",
        job["matched_skills"]
    )

    print(
        "Missing Skills:",
        job["missing_skills"]
    )


print("\n===== CAREER STRATEGY =====")

print(
    result["career_strategy"]
)