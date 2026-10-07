import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from app.services.career_tools import search_and_rank_candidate_jobs


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def run_career_agent(
    candidate_skills: list[str],
    candidate_text: str,
    user_request: str
):

    # Step 1: Agent decides what information it needs
    planning_prompt = f"""
You are CareerIQ, an AI career agent.

Candidate:
{candidate_text}

Candidate Skills:
{candidate_skills}

User Request:
{user_request}

Decide what job-search query should be used to find
relevant jobs for this candidate.

Return ONLY JSON:

{{
    "query": "job search query"
}}
"""

    planning_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a career agent that plans job searches."
            },
            {
                "role": "user",
                "content": planning_prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    plan = json.loads(
        planning_response.choices[0].message.content
    )

    query = plan.get("query", user_request)

    # Step 2: Agent uses the job-search tool
    jobs = search_and_rank_candidate_jobs(
        candidate_skills=candidate_skills,
        candidate_text=candidate_text,
        query=query,
        top_k=5
    )

    # Step 3: Give tool results back to the LLM
    results_text = json.dumps(
        jobs,
        indent=2,
        ensure_ascii=False
    )

    final_prompt = f"""
You are CareerIQ, an AI career intelligence agent.

Candidate:
{candidate_text}

User Request:
{user_request}

Jobs retrieved by the CareerIQ job-search tool:

{results_text}

Answer the user's request using the retrieved job information.

Rules:
- Use the actual retrieved results.
- Do not invent jobs.
- Do not change the numerical match scores.
- Clearly explain why the recommended jobs are relevant.
- Mention important skill gaps when available.
"""

    final_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a professional career intelligence agent."
            },
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    return {
        "query_used": query,
        "jobs": jobs,
        "answer": final_response.choices[0].message.content
    }