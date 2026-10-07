import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_interview_prep(
    candidate_text: str,
    job_title: str,
    company: str,
    job_description: str,
    required_skills: list[str],
    missing_skills: list[str]
) -> str:

    prompt = f"""
You are CareerIQ, an AI interview preparation assistant.

Prepare the candidate for an interview for the following job.

CANDIDATE:
{candidate_text}

TARGET JOB:
{job_title}

COMPANY:
{company}

JOB DESCRIPTION:
{job_description}

REQUIRED SKILLS:
{required_skills}

IDENTIFIED SKILL GAPS:
{missing_skills}

Create a focused interview preparation plan.

Provide:

1. Technical Topics to Prepare
List the most important technical topics based on the job.

2. Technical Interview Questions
Generate realistic questions related to the role and required skills.

3. Project-Based Questions
Generate questions an interviewer could ask about the candidate's
actual projects or experience.

4. Behavioral Questions
Generate relevant HR/behavioral interview questions.

5. Skill-Gap Questions
Generate questions that may test the candidate's weaker areas.

6. Answer Guidance
For each important question, explain what a strong answer should cover.
Do not write a fake answer for the candidate.

IMPORTANT RULES:

- Use the candidate's actual information.
- Do not invent projects, experience, skills or achievements.
- Do not assume the candidate has a missing skill.
- Questions should be specific to the target job.
- Prioritize the most important topics.
- Keep the preparation practical for an interview.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional technical interview "
                    "preparation assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content