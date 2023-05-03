from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.utils.postgres_manager import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    name = Column(String, nullable=False)
    section_id = Column(Integer, ForeignKey('sections.section_id'), nullable=False)
    plants = Column(String, nullable=False)
    date = Column(String, nullable=False)
