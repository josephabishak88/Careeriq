from app.services.market_intelligence import (
    analyze_job_market,
    compare_candidate_to_market
)


jobs = [
    {
        "title": "Data Scientist",
        "required_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Statistics"
        ],
        "experience_level": "0-2 years",
        "work_mode": "Hybrid",
        "location": "Bengaluru"
    },
    {
        "title": "ML Engineer",
        "required_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Docker"
        ],
        "experience_level": "1-3 years",
        "work_mode": "Remote",
        "location": "Bengaluru"
    },
    {
        "title": "Data Analyst",
        "required_skills": [
            "Python",
            "SQL",
            "Data Analysis",
            "Statistics"
        ],
        "experience_level": "0-2 years",
        "work_mode": "On-site",
        "location": "Chennai"
    }
]


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]


print("\n===== CAREERIQ MARKET INTELLIGENCE =====")


market_data = analyze_job_market(jobs)


print("\nTotal Jobs:")
print(market_data["total_jobs"])


print("\nTop Market Skills:")

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


market_comparison = compare_candidate_to_market(
    candidate_skills=candidate_skills,
    market_data=market_data
)


print("\n===== CANDIDATE VS MARKET =====")


print("\nCandidate Skills Found In Market:")

for skill in market_comparison[
    "candidate_skills_found_in_market"
]:
    print("-", skill)


print("\nMarket Skills Missing From Candidate:")

for skill in market_comparison[
    "market_skills_missing_from_candidate"
]:
    print("-", skill)