# models/sections.py
from sqlalchemy import Column, Integer, String
from app.utils.postgres_manager import Base

class Section(Base):
    __tablename__ = "sections"

    section_id = Column(Integer, primary_key=True, index=True)
    section_name = Column(String, nullable=False)
    batch_number = Column(Integer, nullable=False)
    section_type = Column(String, nullable=False)
