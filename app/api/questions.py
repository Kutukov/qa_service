from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db.session import SessionLocal

router = APIRouter(prefix="/questions", tags=["questions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.QuestionRead])
def list_questions(db: Session = Depends(get_db)):
    return crud.list_questions(db)


@router.post(
    "/", response_model=schemas.QuestionRead, status_code=status.HTTP_201_CREATED
)
def create_question(q_in: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, q_in)


@router.get("/{question_id}", response_model=schemas.QuestionRead)
def get_question(question_id: int, db: Session = Depends(get_db)):
    q = crud.get_question(db, question_id)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_question(db, question_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Question not found")
    return
