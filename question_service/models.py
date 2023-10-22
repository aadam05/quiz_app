from sqlalchemy import Column, Integer, String, DateTime
from config.database import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, unique=True)
    question = Column(String)
    answer = Column(String, nullable=True)
    created = Column(DateTime)
