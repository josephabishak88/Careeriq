from app.services.job_search_ranker import search_and_rank_jobs


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


query = """
AI machine learning data science Python
"""


print("\n===== CAREERIQ CANDIDATE JOB RANKING =====")


results = search_and_rank_jobs(
    candidate_skills=candidate_skills,
    candidate_text=candidate_text,
    query=query,
    candidate_years=0,
    top_k=10
)


print("\n===== TOP MATCHES =====")


for index, job in enumerate(results, start=1):

    print(f"\n--- Rank {index} ---")

    print("Title:", job["title"])
    print("Company:", job["company"])
    print("Location:", job["location"])

    print(
        "Final Score:",
        job["final_score"]
    )

    print(
        "Skill Score:",
        job["skill_score"]
    )

    print(
        "Semantic Score:",
        job["semantic_score"]
    )

    print(
        "Experience Score:",
        job["experience_score"]
    )

    print(
        "Experience Status:",
        job["experience_status"]
    )

    print(
        "Seniority Score:",
        job["seniority_score"]
    )

    print(
        "Seniority Status:",
        job["seniority_status"]
    )

    print(
        "Detected Seniority:",
        job["job_seniority"]
    )

    print(
        "Matched Skills:",
        job["matched_skills"]
    )

    print(
        "Missing Skills:",
        job["missing_skills"]
    )

    print(
        "Source:",
        job["source_url"]
    )