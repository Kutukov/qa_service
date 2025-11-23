from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas


# Questions
def get_question(db: Session, question_id: int) -> Optional[models.Question]:
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def list_questions(db: Session) -> List[models.Question]:
    return db.query(models.Question).order_by(models.Question.created_at.desc()).all()


def create_question(db: Session, q_in: schemas.QuestionCreate) -> models.Question:
    q = models.Question(text=q_in.text)
    db.add(q)
    db.commit()
    db.refresh(q)
    return q


def delete_question(db: Session, question_id: int) -> bool:
    q = get_question(db, question_id)
    if not q:
        return False
    db.delete(q)
    db.commit()
    return True


# Answers
def get_answer(db: Session, answer_id: int) -> Optional[models.Answer]:
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()


def create_answer(
    db: Session, question_id: int, a_in: schemas.AnswerCreate
) -> Optional[models.Answer]:
    # Validate question exists
    q = get_question(db, question_id)
    if not q:
        return None
    ans = models.Answer(question_id=question_id, user_id=a_in.user_id, text=a_in.text)
    db.add(ans)
    db.commit()
    db.refresh(ans)
    return ans


def delete_answer(db: Session, answer_id: int) -> bool:
    a = get_answer(db, answer_id)
    if not a:
        return False
    db.delete(a)
    db.commit()
    return True
