import re

from app.models.profile import CandidateProfile


def extract_basic_profile(text: str) -> CandidateProfile:

    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    email = email_match.group(0) if email_match else None

    phone_match = re.search(
        r"\+?\d[\d\s\-]{8,}\d",
        text
    )

    phone = phone_match.group(0) if phone_match else None

    return CandidateProfile(
        email=email,
        phone=phone
    )