from app.services.job_sources import fetch_jobs
from app.services.ashby_parser import (
    parse_ashby_job,
    enrich_ashby_job
)
from app.services.job_analyzer import analyze_job_description


print("\n===== CAREERIQ ASHBY PIPELINE =====")

# 1. Fetch Ashby jobs
jobs = fetch_jobs(
    source_type="ashby",
    company_slug="ema"
)

print("Jobs fetched:", len(jobs))


# 2. Take one job for testing
if not jobs:
    print("No jobs found.")
    exit()


raw_job = jobs[0]


# 3. Convert Ashby JSON → JobProfile
job = parse_ashby_job(
    raw_job,
    company="Ema"
)


print("\n===== BASIC JOB PROFILE =====")

print("Title:", job.title)
print("Company:", job.company)
print("Location:", job.location)
print("Source URL:", job.source_url)


# 4. Analyze description with LLM
print("\nAnalyzing job with LLM...")

analysis = analyze_job_description(
    job.description
)


# 5. Add LLM intelligence to JobProfile
job = enrich_ashby_job(
    job,
    analysis
)


# 6. Display result
print("\n===== ASHBY JOB INTELLIGENCE =====")

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