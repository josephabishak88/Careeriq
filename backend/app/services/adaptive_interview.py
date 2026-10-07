from app.services.interview_practice import (
    start_interview,
    evaluate_answer
)


def run_interview_turn(
    candidate_text: str,
    job_title: str,
    job_description: str,
    required_skills: list[str],
    question: str,
    answer: str
) -> dict:

    evaluation = evaluate_answer(
        candidate_text=candidate_text,
        job_title=job_title,
        question=question,
        answer=answer
    )

    # If the answer has important missing points,
    # use them to guide the next question.
    missing_points = evaluation.get("missing_points", [])

    if missing_points:
        next_question = (
            "Can you explain more about "
            + missing_points[0]
            + " in the context of your project or experience?"
        )
    else:
        next_question_result = start_interview(
            candidate_text=candidate_text,
            job_title=job_title,
            job_description=job_description,
            required_skills=required_skills
        )

        next_question = next_question_result["question"]

    return {
        "current_question": question,
        "answer": answer,
        "evaluation": evaluation,
        "next_question": next_question
    }