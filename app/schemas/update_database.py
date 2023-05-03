# app/schemas_update.py
from datetime import date
from typing import List
from pydantic import BaseModel


class SectionUpdate(BaseModel):
    section_id: int
    section_name: str = None
    batch_number: int = None
    section_type: str = None


class PlantUpdate(BaseModel):
    plant_id: int
    section_id: int = None
    seed_id: str = None
    seed_type: str = None
    date_planted: date = None
    number_of_branches_when_planted: int = None


class HarvestUpdate(BaseModel):
    harvest_id: int
    plant_id: int = None
    harvest_date: date = None
    vanilla_beans: int = None
    bean_weight: float = None
