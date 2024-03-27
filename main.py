from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import SkillRouter, ProjectRouter
from sql import models
from sql.database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
]





app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(SkillRouter.router)
app.include_router(ProjectRouter.router)
