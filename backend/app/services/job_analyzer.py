import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def analyze_job_description(description: str) -> dict:

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": """
You are a professional job description analysis system.

Analyze the provided job description and extract structured
job requirements.

Return JSON with exactly these fields:

{
    "required_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "education": null,
    "experience_level": null
}

IMPORTANT RULES:

1. required_skills must contain ONLY individual,
   reusable skills, technologies, tools, methodologies,
   or professional competencies.

Examples:
- Python
- SQL
- Machine Learning
- Data Analysis
- AWS
- Docker
- Financial Reporting
- Communication
- Project Management

Do NOT put complete sentences or requirement descriptions
inside required_skills.

BAD:
"Deep understanding of Indian statutory regulations
(TDS, GST, MSME Act, Companies Act)"

GOOD:
"GST"
"TDS"
"MSME Act"
"Companies Act"

2. Do not put qualifications such as
"4-7 years of experience" into required_skills.

3. Do not put degree requirements into required_skills.
Put them in education.

4. preferred_skills should contain individual skills that are
explicitly described as preferred, desirable, nice-to-have,
or equivalent.

5. responsibilities should contain actual job responsibilities,
not skills.

6. experience_level should contain explicitly stated experience
requirements such as:
- "0-2 years"
- "3+ years"
- "4-7 years"
- "Senior"
- "Entry level"

7. Do not invent information.

8. Keep skill names concise and reusable across different jobs.

If something is not present, return an empty list or null.
"""
            },
            {
                "role": "user",
                "content": description
            }
        ],
        response_format={"type": "json_object"}
    )

    raw_output = response.choices[0].message.content

    return json.loads(raw_output)