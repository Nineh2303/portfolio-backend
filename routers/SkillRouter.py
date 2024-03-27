from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sql.database import SessionLocal
from sql.crud import get_all_skill, add_new_skill
from sql import schemas

router = APIRouter(prefix="/skills", tags=["skill"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def GetAllSkill(db: Session = Depends(get_db)):
    return  get_all_skill(db)


@router.post("/add", response_model=schemas.Skill)
async def AddNewSkill(skill: schemas.Skill, db: Session = Depends(get_db)):
    return add_new_skill(db, skill)
