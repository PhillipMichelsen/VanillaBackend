# app/update_database.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import sections, plants
from app.schemas.update_database import SectionUpdate, PlantUpdate
from app.utils.postgres_manager import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sections", response_model=int)
def create_section(section: SectionUpdate, db: Session = Depends(get_db)):
    section_id = section.section_id

    existing_section = db.query(sections.Section).filter(sections.Section.section_id == section_id).first()  # type: ignore

    if existing_section:
        raise HTTPException(status_code=400, detail="Section with this ID already exists")

    new_section = sections.Section(**section.dict())

    db.add(new_section)
    db.commit()
    db.refresh(new_section)

    return new_section.section_id


@router.put("/sections", response_model=int)
def update_section(section_update: SectionUpdate, db: Session = Depends(get_db)):
    section_id = section_update.section_id

    section = db.query(sections.Section).filter(sections.Section.section_id == section_id).first()  # type: ignore

    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    for key, value in section_update.dict().items():
        if value is not None:
            setattr(section, key, value)

    db.commit()

    return section.section_id


@router.delete("/sections/{section_id}", response_model=int)
def delete_section(section_id: int, db: Session = Depends(get_db)):
    section = db.query(sections.Section).filter(sections.Section.section_id == int(section_id)).first()  # type: ignore

    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    db.delete(section)
    db.commit()

    return section.section_id


# Plants
@router.post("/plants", response_model=int)
def create_plant(plant: PlantUpdate, db: Session = Depends(get_db)):
    plant_id = plant.plant_id

    existing_plant = db.query(plants.Plant).filter(plants.Plant.plant_id == plant_id).first()  # type: ignore

    if existing_plant:
        raise HTTPException(status_code=400, detail="Plant with this ID already exists")

    section_id = plant.section_id

    section = db.query(sections.Section).filter(sections.Section.section_id == section_id).first()  # type: ignore

    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    new_plant = plants.Plant(**plant.dict())

    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)

    return new_plant.plant_id


@router.put("/plants", response_model=int)
def update_plant(plant_update: PlantUpdate, db: Session = Depends(get_db)):
    plant_id = plant_update.plant_id
    plant = db.query(plants.Plant).filter(plants.Plant.plant_id == plant_id).first()  # type: ignore
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    for key, value in plant_update.dict().items():
        if value is not None:
            setattr(plant, key, value)
    db.commit()
    return plant.plant_id


@router.delete("/plants/{plant_id}", response_model=int)
def delete_plant(plant_id: int, db: Session = Depends(get_db)):
    plant = db.query(plants.Plant).filter(plants.Plant.plant_id == plant_id).first()  # type: ignore
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    db.delete(plant)
    db.commit()
    return plant.plant_id
