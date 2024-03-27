from fastapi import Depends
from sqlalchemy.orm import Session

from . import models, schemas
from sql.database import SessionLocal


def get_all_skill(db: Session):
    return db.query(models.Skill).all()


def get__all_project(db: Session):
    return db.query(models.Project).all()


def add_new_skill(db: Session, skill: schemas.Skill):
    db_skill = models.Skill(skillName=skill.skillName, skillPercent=skill.skillPercent, skillType=skill.skillType,
                            skillIcon=skill.skillIcon)
    try:
        db.add(db_skill)
        db.commit()
    except:
        db.rollback()
    db.refresh(db_skill)
    return db_skill


def add_new_project(db: Session, project: schemas.Project):
    db_project = models.Project(projectName=project.projectName, projectDescription=project.projectDescription,
                                projectImage=project.projectImage)
    try:
        db.add(db_project)
        db.commit()
    except:
        db.rollback()
    db.refresh()
    return db_project
