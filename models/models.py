# models.py
from sqlalchemy import Column, Integer, String, Float
from db.db_connect import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    impressions = Column(Integer, nullable=False)
