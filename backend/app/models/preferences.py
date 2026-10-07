from typing import List, Optional
from pydantic import BaseModel, Field


class CareerPreferences(BaseModel):

    target_roles: List[str] = Field(default_factory=list)

    preferred_locations: List[str] = Field(default_factory=list)

    work_modes: List[str] = Field(default_factory=list)

    experience_level: Optional[str] = None

    minimum_salary: Optional[float] = None

    preferred_industries: List[str] = Field(default_factory=list)