from app.services.experience_matcher import (
    calculate_experience_fit
)


candidate_years = 0


test_jobs = [
    "0-2 years",
    "1+ years",
    "3+ years",
    "8+ years",
    None
]


print("\n===== EXPERIENCE MATCH TEST =====")


for requirement in test_jobs:

    result = calculate_experience_fit(
        candidate_years=candidate_years,
        job_experience_level=requirement
    )

    print("\nJob Requirement:", requirement)
    print("Result:", result)