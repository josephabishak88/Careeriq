from app.services.job_sources import fetch_jobs


COMPANY_SLUG = "ema"


print("\n===== ASHBY TEST =====")

try:
    jobs = fetch_jobs(
        source_type="ashby",
        company_slug=COMPANY_SLUG
    )

    print("Jobs found:", len(jobs))

    if jobs:
        print("\nFirst job:")
        print(jobs[0])

except Exception as e:
    print("\nAshby fetch failed:")
    print(e)