from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class AnswerCreate(BaseModel):
    user_id: str = Field(..., description="user identifier (uuid or similar)")
    text: str


class AnswerRead(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

    model_config = {"from_attributes": True}


class QuestionCreate(BaseModel):
    text: str


class QuestionRead(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerRead] = []

    model_config = {"from_attributes": True}
