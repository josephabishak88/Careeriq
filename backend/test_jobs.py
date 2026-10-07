from app.services.job_service import fetch_company_jobs
from app.services.job_parser import parse_lever_job


jobs = fetch_company_jobs("cred")

print(f"Total jobs found: {len(jobs)}")

for raw_job in jobs[:5]:

    job = parse_lever_job(
        raw_job,
        company="CRED"
    )

    print("\n----------------")
    print("Job ID:", job.job_id)
    print("Title:", job.title)
    print("Company:", job.company)
    print("Location:", job.location)
    print("Description:", job.description[:200] if job.description else None)
    print("URL:", job.source_url)