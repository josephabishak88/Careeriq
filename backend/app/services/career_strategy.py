import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_career_strategy(
    candidate_skills: list[str],
    target_role: str,
    missing_skills: list[str],
    career_intelligence: str
) -> str:

    prompt = f"""
You are CareerIQ, an AI career strategy assistant.

Candidate Skills:
{candidate_skills}

Target Role:
{target_role}

Missing Skills:
{missing_skills}

Career Intelligence:
{career_intelligence}

Create a practical career strategy for the candidate.

Provide:

1. Career Direction
2. Priority Skills to Learn
3. Recommended Learning Order
4. Project Ideas
5. Short-Term Roadmap

Rules:
- Prioritize the provided missing skills.
- Do not invent skills the candidate already has.
- Do not claim the candidate has experience that was not provided.
- Keep the roadmap realistic for a student or early-career candidate.
- Focus on actionable recommendations.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional career strategy assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content