from app.services.job_service import fetch_company_jobs

from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)

from app.services.job_analyzer import analyze_job_description

from app.services.vector_store import add_job

from app.services.job_search_ranker import search_and_rank_jobs


print("\n===== FETCHING JOBS =====")

raw_jobs = fetch_company_jobs("cred")

print("Total jobs found:", len(raw_jobs))


print("\n===== UPDATING CHROMADB =====")

for raw_job in raw_jobs:

    job = parse_lever_job(
        raw_job,
        company="CRED"
    )

    if job.description:

        analysis = analyze_job_description(
            job.description
        )

        job = enrich_job_profile(
            job,
            analysis
        )

    add_job(job)

    print("\nStored:", job.title)
    print("Required Skills:", job.required_skills)


print("\n===== CHROMADB UPDATED =====")


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]


candidate_text = """
Python, Machine Learning, FastAPI, XGBoost,
Data Science and Artificial Intelligence
"""


query = """
Python machine learning data science backend API
"""


print("\n===== SEARCHING AND RANKING =====")


results = search_and_rank_jobs(
    candidate_skills=candidate_skills,
    candidate_text=candidate_text,
    query=query,
    top_k=5
)


print("\n===== CAREERIQ JOB RANKING =====")


for index, job in enumerate(results, start=1):

    print(f"\n===== RANK {index} =====")

    print("Title:", job["title"])
    print("Company:", job["company"])
    print("Location:", job["location"])

    print("\nRequired Skills:")

    for skill in job["required_skills"]:
        print("-", skill)

    print("\nMatched Skills:")

    for skill in job["matched_skills"]:
        print("-", skill)

    print("\nMissing Skills:")

    for skill in job["missing_skills"]:
        print("-", skill)

    print("\nSkill Score:", job["skill_score"], "%")
    print("Semantic Score:", job["semantic_score"], "%")
    print("Final Score:", job["final_score"], "%")

    print("Chroma Distance:", job["chroma_distance"])

    print("Source:", job["source_url"])