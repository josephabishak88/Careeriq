from app.services.job_service import fetch_company_jobs
from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)
from app.services.job_analyzer import analyze_job_description


jobs = fetch_company_jobs("cred")

raw_job = jobs[0]

job = parse_lever_job(
    raw_job,
    company="CRED"
)

print("\n===== JOB =====")
print("Title:", job.title)
print("Company:", job.company)
print("Location:", job.location)

print("\n===== DESCRIPTION =====")
print(job.description[:1000])

analysis = analyze_job_description(
    job.description
)

# Merge LLM analysis into JobProfile
job = enrich_job_profile(
    job,
    analysis
)

print("\n===== JOB INTELLIGENCE =====")

print("\nRequired Skills:")
for skill in job.required_skills:
    print("-", skill)

print("\nPreferred Skills:")
for skill in job.preferred_skills:
    print("-", skill)

print("\nResponsibilities:")
for item in job.responsibilities:
    print("-", item)

print("\nEducation:")
print(job.education)

print("\nExperience Level:")
print(job.experience_level)

print("\n===== FINAL JOB PROFILE =====")
print(job.model_dump())