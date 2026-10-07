from app.services.job_sources import fetch_jobs
from app.services.job_parser import parse_lever_job
from app.services.ashby_parser import parse_ashby_job


COMPANIES = [
    {
        "slug": "cred",
        "name": "CRED",
        "source_type": "lever"
    },
    {
        "slug": "ema",
        "name": "Ema",
        "source_type": "ashby"
    }
]


print("\n===== CAREERIQ MULTI-ATS TEST =====")


for company in COMPANIES:

    print("\n------------------------------")
    print("Company:", company["name"])
    print("ATS:", company["source_type"])
    print("------------------------------")

    try:

        jobs = fetch_jobs(
            source_type=company["source_type"],
            company_slug=company["slug"]
        )

        print("Jobs found:", len(jobs))

        if not jobs:
            continue

        raw_job = jobs[0]

        if company["source_type"] == "lever":

            job = parse_lever_job(
                raw_job,
                company=company["name"]
            )

        elif company["source_type"] == "ashby":

            job = parse_ashby_job(
                raw_job,
                company=company["name"]
            )

        print("First job:", job.title)
        print("Location:", job.location)
        print("Description length:", len(job.description))

    except Exception as e:

        print("ERROR:", e)


print("\n===== TEST COMPLETE =====")