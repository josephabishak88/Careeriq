from app.services.job_sources import fetch_jobs
from app.services.ashby_parser import parse_ashby_job


print("\n===== ASHBY PARSER TEST =====")

jobs = fetch_jobs(
    source_type="ashby",
    company_slug="ema"
)

print("Jobs fetched:", len(jobs))

if jobs:

    job = parse_ashby_job(
        jobs[0],
        company="Ema"
    )

    print("\n===== PARSED JOB =====")

    print("Job ID:", job.job_id)
    print("Title:", job.title)
    print("Company:", job.company)
    print("Location:", job.location)
    print("Work Mode:", job.work_mode)
    print("Source URL:", job.source_url)

    print("\nDescription:")
    print(job.description[:1000])

    print("\n===== VALIDATED JOB PROFILE =====")
    print(job.model_dump())