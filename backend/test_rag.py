from app.services.rag_service import generate_rag_answer


candidate_text = """
I am a final-year B.Tech Computer Science and Engineering student
with skills in Python, Machine Learning, FastAPI, XGBoost and Data Science.
I am interested in AI and Data Science roles.
"""


query = """
Which of the retrieved jobs is most relevant to this candidate,
and why?
"""


print("\n===== CAREERIQ RAG TEST =====")

answer = generate_rag_answer(
    candidate_text=candidate_text,
    query=query,
    top_k=3
)

print("\n===== RAG ANSWER =====")
print(answer)