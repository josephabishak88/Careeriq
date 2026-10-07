from app.services.job_ranker import rank_job


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost"
]

job_required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Docker"
]


result = rank_job(
    candidate_skills=candidate_skills,
    job_required_skills=job_required_skills,
    semantic_similarity=0.55,
    candidate_years=0.5,
    candidate_seniority="entry",
    job_experience_level="3+ years",
    job_title="Senior Machine Learning Engineer"
)


print("\n===== UPDATED JOB RANKER TEST =====")

print("Matched Skills:", result["matched_skills"])
print("Missing Skills:", result["missing_skills"])
print("Experience Score:", result["experience_score"])
print("Experience Status:", result["experience_status"])
print("Candidate Seniority:", result["candidate_seniority"])
print("Job Seniority:", result["job_seniority"])
print("Seniority Score:", result["seniority_score"])
print("Seniority Status:", result["seniority_status"])
print("Final Score:", result["final_score"])