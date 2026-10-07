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
You are CareerIQ, an AI career strategy system.

Your job is to create a realistic skill-gap analysis and
career development strategy using ONLY the information
provided below.

CANDIDATE SKILLS:
{candidate_skills}

TARGET ROLE:
{target_role}

MISSING SKILLS:
{missing_skills}

CAREER INTELLIGENCE:
{career_intelligence}


Provide the following sections:

1. Career Direction

Explain whether the target role is currently a realistic
direction based on the candidate's existing skills and the
identified gaps.

2. Existing Strengths

Identify the candidate's strongest relevant skills from
the provided candidate skills.

3. Critical Skill Gaps

Identify the most important missing skills for the target role.

4. Important Skill Gaps

Identify missing skills that are useful but less critical.

5. Learning Priority

Create a prioritized learning order.

For each priority explain briefly:
- Skill
- Why it matters
- What the candidate should learn

6. Recommended Projects

Suggest practical projects that help develop the missing
skills.

Projects must be realistic for a student or early-career
candidate.

7. Short-Term Roadmap

Create a practical roadmap divided into:

Phase 1:
Foundation

Phase 2:
Skill Development

Phase 3:
Project Implementation

Phase 4:
Job Preparation


IMPORTANT RULES:

- Do not invent candidate experience.
- Do not claim the candidate already knows a missing skill.
- Do not fabricate job requirements.
- Prioritize the provided missing skills.
- Do not recommend every missing skill equally.
- Focus on skills that are relevant to the target role.
- Keep recommendations realistic.
- Do not guarantee employment.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional AI career "
                    "strategy assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content