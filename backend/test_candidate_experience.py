from app.services.candidate_experience import (
    calculate_candidate_years,
    determine_candidate_seniority
)

print("\n===== CAREERIQ EXPERIENCE TEST =====")

experience = [
    type(
        "Experience",
        (),
        {
            "duration": "June 2026 – July 2026"
        }
    )()
]

years = calculate_candidate_years(experience)
seniority = determine_candidate_seniority(years)

print("Candidate Experience:", years, "years")
print("Candidate Seniority:", seniority)

assert years == 0.1
assert seniority == "entry"

print("\nTEST PASSED")