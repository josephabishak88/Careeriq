from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


candidate = """
Python, Machine Learning, FastAPI, XGBoost,
Data Science and Artificial Intelligence
"""


job_a = """
Looking for a candidate with experience in Python,
machine learning, predictive modeling and backend APIs.
"""


job_b = """
Looking for a finance professional with experience in
accounting, GST, financial reporting and treasury management.
"""


candidate_vector = model.encode(
    [candidate],
    normalize_embeddings=True
)

job_a_vector = model.encode(
    [job_a],
    normalize_embeddings=True
)

job_b_vector = model.encode(
    [job_b],
    normalize_embeddings=True
)


similarity_a = cosine_similarity(
    candidate_vector,
    job_a_vector
)[0][0]

similarity_b = cosine_similarity(
    candidate_vector,
    job_b_vector
)[0][0]


print("Candidate ↔ Job A:", similarity_a)
print("Candidate ↔ Job B:", similarity_b)