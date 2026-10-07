from app.services.job_service import fetch_company_jobs
from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)
from app.services.job_analyzer import analyze_job_description
from app.services.job_storage import (
    save_jobs,
    load_jobs
)


COMPANY = "CRED"
COMPANY_SLUG = "cred"

jobs = fetch_company_jobs(COMPANY_SLUG)

job_profiles = []

for raw_job in jobs[:3]:

    job = parse_lever_job(
        raw_job,
        company=COMPANY
    )

    if job.description:

        analysis = analyze_job_description(
            job.description
        )

        job = enrich_job_profile(
            job,
            analysis
        )

    job_profiles.append(job)


# Save
save_jobs(job_profiles)

print("\nJobs saved successfully.")


# Load
loaded_jobs = load_jobs()

print("Jobs loaded:", len(loaded_jobs))

for job in loaded_jobs:

    print("\n----------------")
    print("Title:", job.title)
    print("Company:", job.company)
    print("Location:", job.location)