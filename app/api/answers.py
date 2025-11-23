from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db.session import SessionLocal

router = APIRouter(tags=["answers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/questions/{question_id}/answers/",
    response_model=schemas.AnswerRead,
    status_code=status.HTTP_201_CREATED,
)
def create_answer(
    question_id: int, a_in: schemas.AnswerCreate, db: Session = Depends(get_db)
):
    ans = crud.create_answer(db, question_id, a_in)
    if ans is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return ans


@router.get("/answers/{answer_id}", response_model=schemas.AnswerRead)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    a = crud.get_answer(db, answer_id)
    if not a:
        raise HTTPException(status_code=404, detail="Answer not found")
    return a


@router.delete("/answers/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_answer(db, answer_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Answer not found")
    return
