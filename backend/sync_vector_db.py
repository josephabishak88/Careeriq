from app.services.job_storage import load_jobs
from app.services.vector_store import add_job


print("\n===== CAREERIQ VECTOR DATABASE SYNC =====")


jobs = load_jobs()

print("Jobs loaded:", len(jobs))


success_count = 0
failed_count = 0


for job in jobs:

    try:

        add_job(job)

        success_count += 1

        print(
            f"[OK] {job.company} - {job.title}"
        )

    except Exception as e:

        failed_count += 1

        print(
            f"[FAILED] {job.company} - {job.title}"
        )

        print("Error:", e)


print("\n===== SYNC COMPLETE =====")

print("Successfully added:", success_count)
print("Failed:", failed_count)