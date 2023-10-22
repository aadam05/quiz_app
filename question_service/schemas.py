from pydantic import BaseModel
from datetime import datetime


class QuestionsInfo(BaseModel):
    questions_num: int


class Question(BaseModel):
    id: int
    question_id: int
    question: str
    answer: str
    created: datetime = None
