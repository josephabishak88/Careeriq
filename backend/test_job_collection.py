from app.services.job_service import fetch_company_jobs
from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)
from app.services.job_analyzer import analyze_job_description


COMPANY = "CRED"
COMPANY_SLUG = "cred"

jobs = fetch_company_jobs(COMPANY_SLUG)

print(f"\nTotal jobs found: {len(jobs)}")

job_profiles = []

for index, raw_job in enumerate(jobs[:3], start=1):

    print(f"\n===== PROCESSING JOB {index} =====")

    # Convert raw Lever job → JobProfile
    job = parse_lever_job(
        raw_job,
        company=COMPANY
    )

    print("Title:", job.title)
    print("Location:", job.location)

    # Analyze description with LLM
    if job.description:

        analysis = analyze_job_description(
            job.description
        )

        # Merge analysis into JobProfile
        job = enrich_job_profile(
            job,
            analysis
        )

    job_profiles.append(job)

print("\n\n===== COLLECTION COMPLETE =====")

print("Jobs processed:", len(job_profiles))

for job in job_profiles:

    print("\n----------------------------")
    print("Title:", job.title)
    print("Company:", job.company)
    print("Location:", job.location)
    print("Work Mode:", job.work_mode)
    print("Experience:", job.experience_level)
    print("Required Skills:", job.required_skills)
    print("Source:", job.source_url)