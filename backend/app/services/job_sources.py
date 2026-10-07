import requests


def fetch_lever_jobs(company_slug: str):
    """
    Fetch public job postings from a company's Lever job board.
    """

    url = f"https://api.lever.co/v0/postings/{company_slug}"

    response = requests.get(
        url,
        params={"mode": "json"},
        timeout=20
    )

    response.raise_for_status()

    return response.json()


def fetch_ashby_jobs(company_slug: str):
    """
    Fetch public job postings from an Ashby job board.
    """

    url = (
        "https://api.ashbyhq.com/posting-api/job-board/"
        f"{company_slug}"
    )

    response = requests.get(
        url,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("jobs", [])


def fetch_jobs(source_type: str, company_slug: str):
    """
    Fetch jobs based on the company's ATS source.
    """

    if source_type == "lever":
        return fetch_lever_jobs(company_slug)

    if source_type == "ashby":
        return fetch_ashby_jobs(company_slug)

    raise ValueError(
        f"Unsupported job source: {source_type}"
    )