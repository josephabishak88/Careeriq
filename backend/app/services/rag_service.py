import os

from dotenv import load_dotenv
from openai import OpenAI

from app.services.vector_store import search_jobs


load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def generate_rag_answer(
    candidate_text: str,
    query: str,
    top_k: int = 3
) -> str:

    # -----------------------------------------
    # 1. Retrieve relevant jobs from ChromaDB
    # -----------------------------------------

    results = search_jobs(
        query=query,
        top_k=top_k
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    if not documents:
        return "No relevant jobs were found."

    # -----------------------------------------
    # 2. Build evidence context
    # -----------------------------------------

    context_parts = []

    for index, document in enumerate(documents, start=1):

        context_parts.append(
            f"""
===== RETRIEVED JOB {index} =====

{document}

===== END RETRIEVED JOB {index} =====
"""
        )

    context = "\n".join(context_parts)

    # -----------------------------------------
    # 3. Grounded RAG prompt
    # -----------------------------------------

    prompt = f"""
You are CareerIQ, an AI career intelligence assistant.

Your task is to answer the user's career question using
the candidate information and retrieved job evidence below.

-----------------------------------------
CANDIDATE INFORMATION
-----------------------------------------

{candidate_text}

-----------------------------------------
RETRIEVED JOB EVIDENCE
-----------------------------------------

{context}

-----------------------------------------
USER QUESTION
-----------------------------------------

{query}

-----------------------------------------
GROUNDING RULES
-----------------------------------------

1. Use the retrieved job evidence as the primary source
   for claims about jobs.

2. Use the candidate information as the primary source
   for claims about the candidate.

3. Do NOT invent:
   - skills
   - experience
   - qualifications
   - job requirements
   - responsibilities
   - companies
   - salary information
   - hiring information

4. Do NOT assume that a skill is required unless it is
   explicitly present in the retrieved job evidence.

5. Do NOT claim that the candidate has a skill unless it
   is explicitly present in the candidate information.

6. If the retrieved evidence does not contain enough
   information to answer the question, clearly say:
   "The retrieved job information does not provide enough
   evidence to determine this."

7. Distinguish clearly between:
   - Candidate strengths
   - Job requirements
   - Skill gaps
   - Reasonable interpretation

8. When comparing the candidate with a job, explain the
   comparison using only information supported by the
   provided evidence.

9. Do not change, estimate, or fabricate numerical values
   that are provided in the context.

10. Prefer concise, evidence-based answers over generic
    career advice.

-----------------------------------------
ANSWER FORMAT
-----------------------------------------

When appropriate, structure the answer as:

1. Direct Answer
2. Evidence from Retrieved Jobs
3. Candidate Match
4. Skill Gaps
5. Conclusion

Only include sections that are relevant to the question.
"""

    # -----------------------------------------
    # 4. Generate grounded answer
    # -----------------------------------------

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional career intelligence "
                    "assistant that must provide grounded, "
                    "evidence-based answers."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content