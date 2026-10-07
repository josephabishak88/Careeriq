import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def optimize_resume_for_job(
    resume_text: str,
    job_title: str,
    company: str,
    job_description: str,
    required_skills: list[str],
    missing_skills: list[str]
) -> str:

    prompt = f"""
You are CareerIQ, an AI resume optimization assistant.

Your task is to tailor an existing resume for a specific job
WITHOUT changing the truth of the candidate's background.

==================================================
CANDIDATE RESUME
==================================================

{resume_text}

==================================================
TARGET JOB
==================================================

Title: {job_title}
Company: {company}

JOB DESCRIPTION:

{job_description}

REQUIRED SKILLS:

{required_skills}

IDENTIFIED SKILL GAPS:

{missing_skills}


==================================================
CORE RULE: EVIDENCE-BASED OPTIMIZATION
==================================================

Every resume recommendation must be supported by explicit
evidence in the candidate's resume.

Use this classification:

1. SUPPORTED
Information explicitly present in the resume.

2. TRANSFERABLE
An existing skill that may be relevant to the target job,
but the candidate has NOT demonstrated actual experience
performing that job responsibility.

3. UNSUPPORTED
A requirement that is not demonstrated by the resume.


==================================================
1. TARGETED PROFESSIONAL SUMMARY
==================================================

Create a concise professional summary tailored to the job.

ONLY use:
- Existing education
- Existing experience
- Existing projects
- Existing skills
- Existing certifications

Do NOT claim:
- Finance experience
- Management experience
- Industry experience
- Leadership experience
- Responsibilities not shown in the resume


==================================================
2. RELEVANT SKILLS TO EMPHASIZE
==================================================

List only skills explicitly present in the resume.

Do NOT convert related concepts into new skills.

For example:

If the resume contains:
"Python, SQL, Pandas"

Do NOT automatically claim:
"Financial Analytics"
"Financial Reporting"
"Accounting Automation"


==================================================
3. RESUME BULLET IMPROVEMENTS
==================================================

Improve existing resume bullets.

IMPORTANT:

Do NOT create fictional work.

Do NOT invent:
- achievements
- percentages
- datasets
- responsibilities
- business impact
- deployment
- automation
- financial processes
- users
- revenue
- time savings

If the original resume does not contain enough detail,
say:

"Insufficient evidence in the provided resume to safely
rewrite this bullet."


==================================================
4. RELEVANT KEYWORDS
==================================================

Create two separate groups.

SUPPORTED KEYWORDS:
Keywords from the job that are explicitly supported by
the candidate's resume.

TRANSFERABLE KEYWORDS:
Concepts that are related to existing candidate skills but
are NOT directly demonstrated as job experience.

Never present transferable keywords as existing experience.


==================================================
5. UNSUPPORTED REQUIREMENTS
==================================================

List important job requirements that are not demonstrated
in the candidate's resume.

For each requirement explain briefly why it is unsupported.

Examples:

Requirement:
"4-7 years Accounts Payable experience"

Reason:
"The provided resume shows Data Science internship
experience rather than Accounts Payable experience."


==================================================
6. TRUTH & SAFETY CHECK
==================================================

Before producing the final answer, verify every claim.

Do NOT:
- Invent experience
- Invent skills
- Invent projects
- Invent certifications
- Invent achievements
- Invent metrics
- Invent responsibilities
- Invent job titles
- Invent industry experience
- Convert transferable skills into demonstrated experience
- Claim a technology was used unless the resume supports it

If uncertain, classify the information as:
"Not demonstrated in the provided resume."


==================================================
OUTPUT FORMAT
==================================================

1. Targeted Professional Summary

2. Relevant Skills to Emphasize

3. Resume Bullet Improvements

4. Supported Keywords

5. Transferable Keywords

6. Unsupported Requirements

7. Truthfulness Check

Keep the recommendations practical and ATS-friendly while
preserving the candidate's actual background.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional ATS-aware resume "
                    "optimization assistant focused on "
                    "evidence-based, truth-preserving resumes."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content