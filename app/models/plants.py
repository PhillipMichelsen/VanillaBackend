# models/plants.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.utils.postgres_manager import Base


class Plant(Base):
    __tablename__ = "plants"

    plant_id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey("sections.section_id"), nullable=False)
    seed_id = Column(String, nullable=False)
    seed_type = Column(String, nullable=False)
    date_planted = Column(Date, nullable=False)
    number_of_branches_when_planted = Column(Integer, nullable=False)
