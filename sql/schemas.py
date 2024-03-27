from msilib.schema import File

from fastapi.params import File
from pydantic import BaseModel


class Skill(BaseModel):
    skillName: str
    skillPercent: float
    skillType: str
    skillIcon: str


class Project(BaseModel):
    projectName: str
    projectDescription: str
    projectDemoUrl : str

