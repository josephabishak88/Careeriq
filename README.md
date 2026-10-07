# CareerIQ

## AI-Powered Career Intelligence, Job Discovery & Career Strategy Platform

CareerIQ is an AI-powered career intelligence platform designed to help candidates
discover relevant job opportunities, understand their skill fit, identify skill gaps,
analyze the job market, optimize their resume, and prepare for interviews.

Instead of functioning as a simple job-search chatbot, CareerIQ combines
semantic job retrieval, hybrid candidate-job matching, Retrieval-Augmented Generation
(RAG), career strategy, market intelligence, resume optimization, and interview
intelligence into one system.

---

# 1. Problem Statement

Job seekers often need to manually search through large numbers of job postings,
compare requirements with their resumes, identify missing skills, understand market
expectations, modify their resumes, and prepare for interviews.

This process is time-consuming and does not provide a unified understanding of:

- Which jobs are most relevant
- Why a candidate matches a job
- Which skills are missing
- What skills are currently appearing across relevant jobs
- What the candidate should learn next
- How the resume can be better aligned with a target job
- What interview topics should be prepared

CareerIQ addresses these challenges through an integrated AI-based career
intelligence pipeline.

---

# 2. Objectives

The main objectives of CareerIQ are:

1. Extract structured candidate information from resumes.
2. Discover structured job listings from public ATS job-board APIs.
3. Analyze job descriptions and identify relevant requirements.
4. Retrieve semantically relevant job opportunities.
5. Calculate candidate-job compatibility using multiple factors.
6. Identify candidate skill gaps.
7. Analyze skills and patterns across retrieved job postings.
8. Provide grounded career intelligence using RAG.
9. Generate personalized career development strategies.
10. Optimize resumes for specific job opportunities without fabricating information.
11. Generate targeted interview preparation.
12. Evaluate retrieval, matching, and RAG behavior.

---

# 3. System Architecture

```text
                         USER
                           |
                           v
                  +------------------+
                  | CareerIQ Frontend|
                  |     Next.js      |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  |     FastAPI      |
                  |     Backend      |
                  +--------+---------+
                           |
              +------------+-------------+
              |            |             |
              v            v             v
           Resume      Career Goal   Preferences
           Analysis
              |
              v
      +----------------------+
      | Candidate Profile    |
      | Pydantic Validation  |
      +----------+-----------+
                 |
                 v
      +----------------------+
      |   Job Intelligence   |
      +----------+-----------+
                 |
          +------+------+
          |             |
          v             v
     Lever APIs     Ashby APIs
          |             |
          +------+------+
                 |
                 v
          Job Profiles
                 |
                 v
        +----------------+
        |  Job Analyzer  |
        |      LLM       |
        +-------+--------+
                |
                v
             jobs.json
                |
                v
             ChromaDB
                |
          +-----+------+
          |            |
          v            v
      Embeddings   Semantic Search
          |            |
          +-----+------+
                |
                v
         Hybrid Matching
                |
       +--------+---------+
       |        |         |
       v        v         v
     Skills Experience Seniority
       |        |         |
       +--------+---------+
                |
                v
           Job Ranking
                |
       +--------+---------+
       |        |         |
       v        v         v
      RAG    Career     Market
             Strategy  Intelligence
       |        |         |
       +--------+---------+
                |
                v
       Resume Optimization
                |
                v
      Interview Intelligence
                |
                v
         CareerIQ Dashboard