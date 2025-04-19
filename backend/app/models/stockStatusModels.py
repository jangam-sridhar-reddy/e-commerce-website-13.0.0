from sqlalchemy import Column, Integer, String
from app.models.baseModel import Base


class StockStatusModel(Base):
    __tablename__ = "StockStatus"
    __table_args__ = {"schema": "lookup"}

    ID = Column(Integer, primary_key=True, nullable= False)
    statusName = Column(String, nullable=False, unique=True)

    