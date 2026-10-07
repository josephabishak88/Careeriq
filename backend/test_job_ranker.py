from app.services.job_ranker import rank_job


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]


job_required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "FastAPI",
    "Docker"
]


semantic_similarity = 0.55466866


# Final-year student
candidate_years = 0


# Example job requirement
job_experience_level = "3+ years"


# Example job title
job_title = "Senior Machine Learning Engineer"


result = rank_job(
    candidate_skills=candidate_skills,
    job_required_skills=job_required_skills,
    semantic_similarity=semantic_similarity,
    candidate_years=candidate_years,
    job_experience_level=job_experience_level,
    job_title=job_title
)


print("\n===== JOB RANKING =====")


print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print("-", skill)


print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("-", skill)


print("\nSkill Score:",
      result["skill_score"], "%")


print("Semantic Score:",
      result["semantic_score"], "%")


print("Experience Score:",
      result["experience_score"], "%")


print("Experience Status:",
      result["experience_status"])


print("Seniority Score:",
      result["seniority_score"], "%")


print("Seniority Status:",
      result["seniority_status"])


print("Detected Seniority:",
      result["job_seniority"])


print("Final Job Score:",
      result["final_score"], "%")