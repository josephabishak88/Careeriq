from bs4 import BeautifulSoup

from app.models.job import JobProfile


def extract_job_description(job: dict) -> str:
    lists = job.get("lists", [])

    if not lists:
        return ""

    html_content = lists[0].get("content", "")

    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, "html.parser")

    return soup.get_text(
        separator="\n",
        strip=True
    )


def parse_lever_job(job: dict, company: str) -> JobProfile:

    categories = job.get("categories", {})

    description = extract_job_description(job)

    return JobProfile(
        job_id=job.get("id"),
        title=job.get("text"),
        company=company,
        location=categories.get("location"),
        work_mode=job.get("workplaceType"),
        description=description,
        source_url=job.get("hostedUrl")
    )


def enrich_job_profile(
    job: JobProfile,
    analysis: dict
) -> JobProfile:

    job.required_skills = analysis.get(
        "required_skills", []
    )

    job.preferred_skills = analysis.get(
        "preferred_skills", []
    )

    job.responsibilities = analysis.get(
        "responsibilities", []
    )

    job.education = analysis.get(
        "education"
    )

    job.experience_level = analysis.get(
        "experience_level"
    )

    return job