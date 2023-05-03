# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.utils.postgres_manager import Base, engine, SessionLocal
from app.routers import update_database, activities
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(update_database.router, prefix="/")
app.include_router(activities.router, prefix="/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def create_tables():
    with engine.begin() as conn:
        Base.metadata.create_all(conn)


@app.get("/")
async def root():
    return "Working!!!"
