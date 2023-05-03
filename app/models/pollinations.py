# models/pollinations.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from app.utils.postgres_manager import Base

class Pollination(Base):
    __tablename__ = "pollinations"

    pollination_id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.plant_id"), nullable=False)
    date_pollinated = Column(Date, nullable=False)
    flowers_pollinated = Column(Integer, nullable=False)
