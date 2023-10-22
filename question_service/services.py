import os
import logging
import requests
from fastapi import APIRouter, Depends, HTTPException
from .schemas import QuestionsInfo, Question
from .models import Base, Question
from config.database import SessionLocal, engine

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


log_filename = "logger/qaModule.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
logging.basicConfig(filename='logger/qaService.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


question_service = APIRouter()


@question_service.get("/questions/", tags=['questions'])
async def get_questions(db: SessionLocal = Depends(get_db)):
    return db.query(Question).all()


@question_service.post("/questions/", tags=['questions'])
async def create_questions(questions_info: QuestionsInfo, db: SessionLocal = Depends(get_db)):
    response = request_questions_from_external_api(count=questions_info.questions_num)
    data = response.json()

    last_saved_question = db.query(Question).order_by(Question.id.desc()).first()

    for item in data:

        while db.query(Question).filter_by(question_id=item['id']).first():
            inner_response = request_questions_from_external_api()
            item = inner_response.json()[0]

        db_question = Question(question_id=item['id'], question=item['question'], answer=item['answer'], created=item['created_at'])
        db.add(db_question)
        db.commit()
    logging.info(f"Questions was saved, no error occurred")

    return last_saved_question.question if last_saved_question else {}


def request_questions_from_external_api(count=1):
    response = requests.get('https://jservice.io/api/random', params={'count': count})
    if response.status_code not in [200, 201]:
        logging.error(f"External API error")
        raise HTTPException(status_code=500, detail="External API error")
    return response
