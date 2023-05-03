# models/harvests.py
from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from app.utils.postgres_manager import Base

class Harvest(Base):
    __tablename__ = "harvests"

    harvest_id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, ForeignKey("plants.plant_id"), nullable=False)
    harvest_date = Column(Date, nullable=False)
    vanilla_beans = Column(Integer, nullable=False)
    bean_weight = Column(Float, nullable=False)
