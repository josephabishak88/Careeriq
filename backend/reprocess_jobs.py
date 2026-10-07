from app.services.job_service import fetch_company_jobs
from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)
from app.services.job_analyzer import analyze_job_description
from app.services.job_storage import save_jobs


COMPANY_SLUG = "cred"
COMPANY_NAME = "CRED"


print("\n===== REPROCESSING JOBS =====")

raw_jobs = fetch_company_jobs(COMPANY_SLUG)

processed_jobs = []


for raw_job in raw_jobs:

    job = parse_lever_job(
        raw_job,
        company=COMPANY_NAME
    )

    if not job.description:
        continue

    analysis = analyze_job_description(
        job.description
    )

    job = enrich_job_profile(
        job,
        analysis
    )

    processed_jobs.append(job)

    print("\nJob:", job.title)

    print("Required Skills:")
    for skill in job.required_skills:
        print("-", skill)

    print("Preferred Skills:")
    for skill in job.preferred_skills:
        print("-", skill)

    print("Experience:", job.experience_level)

    print("Education:", job.education)


save_jobs(processed_jobs)


print("\n===== COMPLETE =====")
print("Jobs saved:", len(processed_jobs))