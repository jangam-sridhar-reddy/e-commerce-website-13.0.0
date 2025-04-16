
from sqlalchemy import Boolean, Column, Integer, String 
from app.models.baseModel import TimeStampedModel 


class MainCategoryModel(TimeStampedModel):
    __tablename__: str = 'Categories'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    cName = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, default=1) 

