import json
import os

from app.models.job import JobProfile


DATA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "..",
    "data"
)

DATA_DIR = os.path.abspath(DATA_DIR)

os.makedirs(DATA_DIR, exist_ok=True)

JOBS_FILE = os.path.join(DATA_DIR, "jobs.json")


def save_jobs(jobs: list[JobProfile]):

    data = [
        job.model_dump()
        for job in jobs
    ]

    with open(JOBS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_jobs() -> list[JobProfile]:

    if not os.path.exists(JOBS_FILE):
        return []

    with open(JOBS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        JobProfile.model_validate(job)
        for job in data
    ]