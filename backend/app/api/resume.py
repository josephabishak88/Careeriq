import os
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.parser import extract_resume_text
from app.services.llm_service import analyze_resume_with_llm
from app.services.careeriq_pipeline import run_careeriq_pipeline


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    target_role: str = "Machine Learning Engineer",
    query: str = "machine learning artificial intelligence data science"
):

    allowed_extensions = [".pdf", ".docx"]

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    temp_path = None

    try:

        # -----------------------------------------
        # 1. Read uploaded resume
        # -----------------------------------------

        contents = await file.read()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp:

            temp.write(contents)
            temp_path = temp.name

        # -----------------------------------------
        # 2. Extract resume text
        # -----------------------------------------

        resume_text = extract_resume_text(
            temp_path
        )

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume."
            )

        # -----------------------------------------
        # 3. Extract CandidateProfile using LLM
        # -----------------------------------------

        profile = analyze_resume_with_llm(
            resume_text
        )

        # -----------------------------------------
        # 4. Run complete CareerIQ pipeline
        # -----------------------------------------

        careeriq_result = run_careeriq_pipeline(

            candidate_profile=profile,

            candidate_text=resume_text,

            target_role=target_role,

            query=query,

            top_k=5
        )

        # -----------------------------------------
        # 5. Return result
        # -----------------------------------------

        return {

            "filename":
                file.filename,

            "extracted_text_length":
                len(resume_text),

            "profile":
                profile.model_dump(),

            "careeriq":
                careeriq_result
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"CareerIQ analysis failed: {str(e)}"
        )

    finally:

        if (
            temp_path
            and os.path.exists(temp_path)
        ):
            os.remove(temp_path)