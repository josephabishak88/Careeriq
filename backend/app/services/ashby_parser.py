from bs4 import BeautifulSoup

from app.models.job import JobProfile


def extract_ashby_description(job: dict) -> str:
    """
    Extract readable job description from Ashby job data.
    """

    description = job.get("descriptionPlain")

    if description:
        return description.strip()

    html = job.get("descriptionHtml")

    if not html:
        return ""

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    return soup.get_text(
        separator="\n",
        strip=True
    )


def parse_ashby_job(
    job: dict,
    company: str
) -> JobProfile:

    description = extract_ashby_description(job)

    return JobProfile(
        job_id=job.get("id"),
        title=job.get("title"),
        company=company,
        location=job.get("location"),
        work_mode=job.get("workplaceType"),
        description=description,
        source_url=job.get("jobUrl")
    )


def enrich_ashby_job(
    job: JobProfile,
    analysis: dict
) -> JobProfile:

    job.required_skills = analysis.get(
        "required_skills",
        []
    )

    job.preferred_skills = analysis.get(
        "preferred_skills",
        []
    )

    job.responsibilities = analysis.get(
        "responsibilities",
        []
    )

    job.education = analysis.get(
        "education"
    )

    job.experience_level = analysis.get(
        "experience_level"
    )

    return job