from app.services.seniority_matcher import (
    detect_seniority,
    calculate_seniority_fit
)


test_titles = [
    "Junior Machine Learning Engineer",
    "Machine Learning Engineer",
    "Senior Machine Learning Engineer",
    "Lead AI Engineer",
    "Principal Machine Learning Engineer",
    "Engineering Manager",
    "Director of Engineering"
]


print("\n===== SENIORITY DETECTION TEST =====")


for title in test_titles:

    seniority = detect_seniority(title)

    result = calculate_seniority_fit(
        candidate_seniority="entry",
        job_seniority=seniority
    )

    print("\nTitle:", title)
    print("Detected:", seniority)
    print("Score:", result["seniority_score"])
    print("Status:", result["seniority_status"])