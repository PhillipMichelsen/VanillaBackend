# models/plant_history.py
from sqlalchemy import String, Column, Integer, Date, ForeignKey
from app.utils.postgres_manager import Base

class PlantHistory(Base):
    __tablename__ = "plant_history"

    history_id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.plant_id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.section_id"), nullable=False)
    seed_id = Column(Integer, nullable=False)
    seed_type = Column(String, nullable=False)
    date_planted = Column(Date, nullable=False)
    number_of_branches_when_planted = Column(Integer, nullable=False)
    date_removed = Column(Date, nullable=False)
