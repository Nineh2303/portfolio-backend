from enum import Enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


# class SkillType(String, Enum):
#     backend = "BACK_END"
#     frontend = "FRONT_END"
#     design = "DESIGN"


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skillName = Column(String, index=True)
    skillPercent = Column(Float, index=True)
    skillType = Column(String)
    skillIcon = Column(String)
    isDeleted = Column(Boolean, default=False)


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    projectName = Column(String, index=True)
    projectDescription = Column(String)
    projectImage = Column(String)
    projectDemoUrl = Column(String)
