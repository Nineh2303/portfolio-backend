from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status

from sql.schemas import Project
from sql.crud import get__all_project, add_new_project

from sql.database import SessionLocal, Base

router = APIRouter(prefix="/projects", tags=["project"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def getAllProject(db: Session = Depends(get_db)):
    return get__all_project(db)


@router.post("/file")
async def create_file(file:UploadFile  , data : Annotated[Project,Project]):
    return {"!23": "123"}
