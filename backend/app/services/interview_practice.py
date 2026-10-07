import os
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def start_interview(
    candidate_text: str,
    job_title: str,
    job_description: str,
    required_skills: list[str]
) -> dict:

    prompt = f"""
You are CareerIQ, conducting a professional job interview.

CANDIDATE:
{candidate_text}

TARGET ROLE:
{job_title}

JOB DESCRIPTION:
{job_description}

REQUIRED SKILLS:
{required_skills}

Start the interview by asking ONE question only.

Choose the most relevant first question based on the
candidate and target role.

The question can be technical, project-based, or
experience-based.

Return ONLY JSON:

{{
    "question": "your interview question",
    "category": "technical/project/experience"
}}

Do not provide the answer.
"""


    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional interviewer."
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


def evaluate_answer(
    candidate_text: str,
    job_title: str,
    question: str,
    answer: str
) -> dict:

    prompt = f"""
You are CareerIQ, evaluating a candidate's interview answer.

CANDIDATE:
{candidate_text}

TARGET ROLE:
{job_title}

INTERVIEW QUESTION:
{question}

CANDIDATE ANSWER:
{answer}

Evaluate the answer professionally.

Score these areas from 0 to 10:

- relevance
- technical_accuracy
- clarity
- depth

Also provide:

- overall_score
- strengths
- weaknesses
- missing_points
- improvement_advice

Return ONLY JSON:

{{
    "relevance": 0,
    "technical_accuracy": 0,
    "clarity": 0,
    "depth": 0,
    "overall_score": 0,
    "strengths": [],
    "weaknesses": [],
    "missing_points": [],
    "improvement_advice": ""
}}

Rules:
- Evaluate only what the candidate actually said.
- Do not assume knowledge that was not demonstrated.
- Do not invent achievements.
- Be constructive and realistic.
"""


    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional technical interviewer and evaluator."
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