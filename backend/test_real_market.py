from app.services.job_storage import load_jobs
from app.services.market_intelligence import (
    analyze_job_market,
    compare_candidate_to_market
)


# Load the jobs already stored by CareerIQ
jobs = load_jobs()

# Convert Pydantic models into dictionaries
job_data = [
    job.model_dump()
    for job in jobs
]


print("\n===== CAREERIQ REAL JOB MARKET =====")

print("\nJobs Loaded:")
print(len(job_data))


# Analyze actual stored jobs
market_data = analyze_job_market(job_data)


print("\n===== MARKET ANALYSIS =====")

print("\nTotal Jobs:")
print(market_data["total_jobs"])


print("\nTop Skills:")

for item in market_data["top_skills"]:
    print(
        f"- {item['skill']}: "
        f"{item['job_count']} jobs"
    )


print("\nExperience Levels:")

for level, count in market_data["experience_levels"].items():
    print(f"- {level}: {count}")


print("\nWork Modes:")

for mode, count in market_data["work_modes"].items():
    print(f"- {mode}: {count}")


print("\nLocations:")

for location, count in market_data["locations"].items():
    print(f"- {location}: {count}")


# Candidate
candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]


comparison = compare_candidate_to_market(
    candidate_skills=candidate_skills,
    market_data=market_data
)


print("\n===== CANDIDATE VS MARKET =====")

print("\nSkills Found In Market:")

for skill in comparison[
    "candidate_skills_found_in_market"
]:
    print("-", skill)


print("\nMarket Skills Missing From Candidate:")

for skill in comparison[
    "market_skills_missing_from_candidate"
]:
    print("-", skill)