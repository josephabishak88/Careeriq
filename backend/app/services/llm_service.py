import os
import json
from dotenv import load_dotenv
from openai import OpenAI

from app.services.skill_normalizer import normalize_candidate_profile
from app.models.profile import CandidateProfile


# Load .env
load_dotenv()


# Groq client using OpenAI-compatible API
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def analyze_resume_with_llm(resume_text: str) -> CandidateProfile:

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": """
You are a professional resume information extraction system.

Extract ONLY information that is explicitly present in the resume.

Do NOT invent:
- skills
- companies
- job roles
- education
- projects
- certifications
- dates
- contact information

If information is missing, return null for optional fields
or an empty list where appropriate.

Return the candidate information according to the provided JSON schema.
"""
            },
            {
                "role": "user",
                "content": resume_text
            }
        ],

        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "candidate_profile",
                "schema": CandidateProfile.model_json_schema()
            }
        }
    )

    # Get JSON returned by LLM
    raw_output = response.choices[0].message.content

    # Convert JSON string → Python dictionary
    profile_data = json.loads(raw_output)

    # Validate using Pydantic
    profile = CandidateProfile.model_validate(profile_data)

    # Normalize candidate skills
    profile = normalize_candidate_profile(profile)

    return profile