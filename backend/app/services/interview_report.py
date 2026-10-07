import os
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_interview_report(
    candidate_text: str,
    job_title: str,
    interview_history: list[dict]
) -> dict:

    prompt = f"""
You are CareerIQ, generating a final interview performance report.

CANDIDATE:
{candidate_text}

TARGET ROLE:
{job_title}

INTERVIEW HISTORY:
{json.dumps(interview_history, indent=2)}

Analyze the complete interview session.

Return ONLY JSON:

{{
    "overall_score": 0,
    "technical_performance": 0,
    "communication_score": 0,
    "strengths": [],
    "weaknesses": [],
    "topics_to_revise": [],
    "readiness": "",
    "final_feedback": ""
}}

Rules:

- Scores must be from 0 to 10.
- Base the report only on the interview answers provided.
- Do not invent candidate experience or skills.
- Do not give credit for information the candidate did not demonstrate.
- Identify recurring weaknesses across answers.
- Recommend revision topics based on demonstrated gaps.
- Readiness should be realistic:
  "Needs Preparation", "Developing", "Interview Ready", or
  "Strongly Prepared".
- Keep the feedback constructive and practical.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional interview evaluator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )