from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import activities, sections
from app.schemas.activities import ActivityCreate, ActivityUpdate, Activity
from app.utils.postgres_manager import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/activities", response_model=int)
def create_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    section = db.query(sections.Section).filter(sections.Section.section_name == activity.section_name).first()
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    new_activity = activities.Activity(**activity.dict(exclude={"section_name"}), section_id=section.section_id)
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity.id

@router.put("/activities/{activity_id}", response_model=int)
def update_activity(activity_id: int, activity_update: ActivityUpdate, db: Session = Depends(get_db)):
    activity = db.query(activities.Activity).filter(activities.Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    if activity_update.section_name:
        section = db.query(sections.Section).filter(sections.Section.section_name == activity_update.section_name).first()
        if not section:
            raise HTTPException(status_code=404, detail="Section not found")
        activity_update.section_id = section.section_id

    for key, value in activity_update.dict(exclude={"section_name"}).items():
        if value is not None:
            setattr(activity, key, value)
    db.commit()
    return activity.id
