import time

from app.services.job_sources import fetch_jobs
from app.services.job_parser import (
    parse_lever_job,
    enrich_job_profile
)
from app.services.ashby_parser import (
    parse_ashby_job,
    enrich_ashby_job
)
from app.services.job_analyzer import analyze_job_description
from app.services.job_storage import load_jobs, save_jobs


COMPANIES = [
    {
        "slug": "cred",
        "name": "CRED",
        "source_type": "lever"
    },
    {
        "slug": "hevodata",
        "name": "Hevo Data",
        "source_type": "lever"
    },
    {
        "slug": "100ms",
        "name": "100ms",
        "source_type": "lever"
    },
    {
        "slug": "levelai",
        "name": "Level AI",
        "source_type": "lever"
    },
    {
        "slug": "ema",
        "name": "Ema",
        "source_type": "ashby"
    }
]


MAX_RETRIES = 5
RETRY_DELAY = 3


print("\n===== CAREERIQ RESUME-SAFE MULTI-ATS INGESTION =====")


# Load jobs already processed
existing_jobs = load_jobs()

jobs_by_id = {
    job.job_id: job
    for job in existing_jobs
    if job.job_id
}

print(
    f"\nExisting jobs already stored: "
    f"{len(jobs_by_id)}"
)


for company in COMPANIES:

    slug = company["slug"]
    name = company["name"]
    source_type = company["source_type"]

    print("\n===================================")
    print(f"Company: {name}")
    print(f"ATS: {source_type}")
    print("===================================")

    try:

        raw_jobs = fetch_jobs(
            source_type=source_type,
            company_slug=slug
        )

        print(
            f"Jobs fetched: {len(raw_jobs)}"
        )

    except Exception as e:

        print(
            f"Could not fetch {name}: {e}"
        )

        continue


    company_processed = 0
    company_skipped = 0


    for raw_job in raw_jobs:

        # -----------------------------
        # Parse job
        # -----------------------------

        try:

            if source_type == "lever":

                job = parse_lever_job(
                    raw_job,
                    company=name
                )

            elif source_type == "ashby":

                job = parse_ashby_job(
                    raw_job,
                    company=name
                )

            else:

                print(
                    f"Unsupported ATS: {source_type}"
                )

                continue

        except Exception as e:

            print(
                f"[PARSE FAILED] {name}: {e}"
            )

            continue


        # -----------------------------
        # Skip existing jobs
        # -----------------------------

        if job.job_id in jobs_by_id:

            company_skipped += 1

            continue


        # -----------------------------
        # Validate description
        # -----------------------------

        if not job.description:

            print(
                f"[SKIPPED] No description: "
                f"{job.title}"
            )

            continue


        # -----------------------------
        # LLM analysis with retry
        # -----------------------------

        analysis = None

        for attempt in range(1, MAX_RETRIES + 1):

            try:

                print(
                    f"[ANALYZING] "
                    f"{name} → {job.title}"
                )

                analysis = analyze_job_description(
                    job.description
                )

                break

            except Exception as e:

                error_text = str(e)

                if "429" not in error_text:

                    print(
                        f"[FAILED] {job.title}: {e}"
                    )

                    break

                print(
                    f"[RATE LIMIT] "
                    f"{job.title} "
                    f"(attempt {attempt}/{MAX_RETRIES})"
                )

                time.sleep(
                    RETRY_DELAY * attempt
                )


        # -----------------------------
        # Skip if analysis failed
        # -----------------------------

        if analysis is None:

            print(
                f"[SKIPPED] "
                f"Could not analyze: "
                f"{job.title}"
            )

            continue


        # -----------------------------
        # Enrich JobProfile
        # -----------------------------

        try:

            if source_type == "lever":

                job = enrich_job_profile(
                    job,
                    analysis
                )

            elif source_type == "ashby":

                job = enrich_ashby_job(
                    job,
                    analysis
                )

        except Exception as e:

            print(
                f"[ENRICH FAILED] "
                f"{job.title}: {e}"
            )

            continue


        # -----------------------------
        # Save immediately
        # -----------------------------

        jobs_by_id[job.job_id] = job

        save_jobs(
            list(jobs_by_id.values())
        )

        company_processed += 1

        print(
            f"[SAVED] "
            f"{job.company} → {job.title}"
        )


    print(
        f"\n{name} summary:"
    )

    print(
        "New jobs processed:",
        company_processed
    )

    print(
        "Existing jobs skipped:",
        company_skipped
    )


print("\n===================================")
print("===== INGESTION COMPLETE =====")
print("===================================")

print(
    "Total jobs stored:",
    len(jobs_by_id)
)