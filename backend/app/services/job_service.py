import requests


def fetch_company_jobs(company_slug: str):
    """
    Fetch public job listings from a company's Lever job board.
    """

    url = f"https://api.lever.co/v0/postings/{company_slug}"

    response = requests.get(
        url,
        params={"mode": "json"},
        timeout=20
    )

    response.raise_for_status()

    return response.json()


def fetch_job_details(company_slug: str, job_id: str):
    """
    Fetch detailed information for a specific Lever job.
    """

    url = f"https://api.lever.co/v0/postings/{company_slug}/{job_id}"

    response = requests.get(
        url,
        params={"mode": "json"},
        timeout=20
    )

    response.raise_for_status()

    return response.json()