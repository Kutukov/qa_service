from fastapi import FastAPI
from app.api import questions, answers
from app.db import base
from app.db.session import engine
from app.core.config import settings


app = FastAPI(title="QA API")

app.include_router(questions.router)
app.include_router(answers.router)
