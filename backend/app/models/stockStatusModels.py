from sqlalchemy import Column, Integer, String
from app.models.baseModel import Base


class StockStatusModel(Base):
    __tablename__ = 'lookup.StockStatus'

    ID = Column(Integer, primary_key=True, nullable= False)
    statusName = Column(String, nullable=False, unique=True)

    