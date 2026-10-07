import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_career_intelligence(
    candidate_text: str,
    job_title: str,
    company: str,
    required_skills: list[str],
    matched_skills: list[str],
    missing_skills: list[str],
    skill_score: float,
    semantic_score: float,
    final_score: float
) -> str:

    prompt = f"""
You are CareerIQ, an AI career intelligence system.

Your task is to analyze how well a candidate fits a specific job
and provide a professional, clear, evidence-based career assessment.

==================================================
CANDIDATE INFORMATION
==================================================

{candidate_text}

==================================================
TARGET JOB
==================================================

Job Title: {job_title}
Company: {company}

Required Skills:
{required_skills}

==================================================
MATCH RESULTS
==================================================

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Skill Score: {skill_score}%
Semantic Score: {semantic_score}%
Final Match Score: {final_score}%

==================================================
ANALYSIS REQUIRED
==================================================

Provide the analysis using exactly these six sections:

1. Overall Assessment
Explain the candidate's overall suitability for this role.
Mention the actual final match score and briefly explain what
the score indicates.

2. Candidate Strengths
Identify the strongest relevant skills, education, projects,
or experience that are explicitly supported by the candidate
information.

For each important strength:
- Name the strength.
- Briefly explain the evidence from the candidate information.

3. Skill Gaps
Identify the most important skills from the job requirements
that are missing from the candidate profile.

For each major gap:
- Name the missing skill.
- Briefly explain why it matters for this role.

4. Why the Candidate Matches
Explain the strongest areas of alignment between the candidate
and the target job.

Use the provided matched skills, scores, projects, education,
and experience as evidence.

5. Main Concerns
Explain the main factors that could reduce the candidate's
fit for the role.

Focus on actual skill gaps, experience gaps, seniority gaps,
or other limitations supported by the provided information.

6. Final Recommendation
Give a realistic recommendation about the candidate's current
fit for this role.

Clearly state whether the candidate appears:
- Strongly aligned
- Moderately aligned
- Partially aligned
- Currently underqualified

Explain the recommendation briefly.

==================================================
STRICT OUTPUT FORMAT
==================================================

The final response must be clean plain text.

Use exactly the numbered section headings:

1. Overall Assessment
2. Candidate Strengths
3. Skill Gaps
4. Why the Candidate Matches
5. Main Concerns
6. Final Recommendation

Formatting rules:

- Do NOT use Markdown tables.
- Do NOT use vertical bar tables such as | Skill | Evidence |.
- Do NOT use horizontal separators such as --- or ===.
- Do NOT use Markdown bold such as **text**.
- Do NOT use Markdown headings such as # or ##.
- Do NOT use code blocks.
- Do NOT use decorative symbols.
- Do NOT repeat the section headings.
- Use short paragraphs and simple bullet points where useful.
- Keep each section concise and readable.
- Leave a blank line between sections.
- Keep bullet points short.
- Do not create very long paragraphs.
- Do not write generic career advice unrelated to this job.

TRUTHFULNESS RULES:

- Use only information explicitly provided about the candidate.
- Do not invent skills.
- Do not invent experience.
- Do not invent projects.
- Do not invent certifications.
- Do not invent achievements.
- Do not invent responsibilities.
- Do not invent salary information.
- Do not invent job requirements.
- Do not assume that a missing skill is present.
- Do not change the provided numerical scores.
- Do not estimate or recalculate the provided scores.
- Clearly distinguish between matched skills and missing skills.

The result should read like a professional career assessment
prepared for a candidate, not like a chatbot conversation.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional career intelligence "
                    "analyst. Produce concise, structured, "
                    "evidence-based plain-text reports."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content