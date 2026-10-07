from collections import Counter


def normalize_location(location: str) -> str:
    """
    Normalize common location variations into a consistent label.
    """

    location = location.strip().lower()

    if "bengaluru" in location or "bangalore" in location:
        return "Bengaluru"

    if "hyderabad" in location:
        return "Hyderabad"

    if "pune" in location:
        return "Pune"

    if "noida" in location:
        return "Noida"

    if "san francisco" in location or "bay area" in location:
        return "San Francisco Bay Area"

    if "united kingdom" in location or "uk" in location:
        return "United Kingdom"

    if "united states" in location or "usa" in location:
        return "United States"

    if "remote" in location:
        return "Remote"

    return location.title()


def normalize_work_mode(work_mode: str) -> str:
    """
    Normalize work-mode variations.
    """

    work_mode = work_mode.strip().lower()

    if work_mode == "remote":
        return "Remote"

    if work_mode == "hybrid":
        return "Hybrid"

    if work_mode == "onsite":
        return "Onsite"

    return work_mode.title()


def analyze_job_market(jobs: list[dict]) -> dict:

    if not jobs:
        return {
            "total_jobs": 0,
            "top_skills": [],
            "all_market_skills": [],
            "experience_levels": {},
            "work_modes": {},
            "locations": {}
        }

    skill_counter = Counter()
    experience_counter = Counter()
    work_mode_counter = Counter()
    location_counter = Counter()

    for job in jobs:

        # -----------------------------------------
        # Skills
        # -----------------------------------------

        for skill in job.get("required_skills", []):
            if skill:
                skill_counter[skill.strip()] += 1

        # -----------------------------------------
        # Experience
        # -----------------------------------------

        experience = job.get("experience_level")

        if experience:
            experience_counter[experience.strip()] += 1

        # -----------------------------------------
        # Work Mode
        # -----------------------------------------

        work_mode = job.get("work_mode")

        if work_mode:
            normalized_mode = normalize_work_mode(work_mode)
            work_mode_counter[normalized_mode] += 1

        # -----------------------------------------
        # Location
        # -----------------------------------------

        location = job.get("location")

        if location:
            normalized_location = normalize_location(location)
            location_counter[normalized_location] += 1

    return {
        "total_jobs": len(jobs),

        # Top 10 skills for market dashboard
        "top_skills": [
            {
                "skill": skill,
                "job_count": count
            }
            for skill, count in skill_counter.most_common(10)
        ],

        # All skills available in the overall market
        "all_market_skills": [
            {
                "skill": skill,
                "job_count": count
            }
            for skill, count in skill_counter.most_common()
        ],

        "experience_levels": dict(
            experience_counter.most_common()
        ),

        "work_modes": dict(
            work_mode_counter.most_common()
        ),

        "locations": dict(
            location_counter.most_common()
        )
    }


def compare_candidate_to_market(
    candidate_skills: list[str],
    jobs: list[dict]
) -> dict:
    """
    Compare candidate skills against skills required
    by the relevant jobs returned by CareerIQ.
    """

    market_skill_counter = Counter()

    for job in jobs:
        for skill in job.get("required_skills", []):
            if skill:
                market_skill_counter[skill.strip().lower()] += 1

    market_skills = set(market_skill_counter.keys())

    candidate_set = {
        skill.strip().lower()
        for skill in candidate_skills
        if skill
    }

    matched = sorted(
        candidate_set.intersection(market_skills)
    )

    missing = sorted(
        market_skills - candidate_set
    )

    return {
        "candidate_skills_found_in_market": matched,
        "market_skills_missing_from_candidate": missing,
        "relevant_market_skills": [
            {
                "skill": skill,
                "job_count": count
            }
            for skill, count in market_skill_counter.most_common()
        ]
    }