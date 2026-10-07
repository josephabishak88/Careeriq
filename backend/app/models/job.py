from typing import List, Optional
from pydantic import BaseModel, Field


class JobProfile(BaseModel):
    job_id: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    work_mode: Optional[str] = None
    experience_level: Optional[str] = None

    salary: Optional[str] = None

    description: Optional[str] = None

    required_skills: List[str] = Field(default_factory=list)
    preferred_skills: List[str] = Field(default_factory=list)

    education: Optional[str] = None

    responsibilities: List[str] = Field(default_factory=list)

    source_url: Optional[str] = None