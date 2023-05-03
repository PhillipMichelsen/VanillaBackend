from pydantic import BaseModel
from typing import Optional
from datetime import date


class ActivityBase(BaseModel):
    task: str
    name: str
    section_name: str
    plants: str
    date: str


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(ActivityBase):
    id: int


class Activity(ActivityBase):
    id: int

    class Config:
        orm_mode = True
