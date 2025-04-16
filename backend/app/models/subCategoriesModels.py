
from sqlalchemy import Boolean, Column, Integer, String
from app.models.baseModel import TimeStampedModel 

 

class SubCategoriesModel(TimeStampedModel):

    __tablename__: str = 'SubCategories'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    subCname = Column(String(50), nullable=False, unique=True)
    is_active = Column(Boolean, default=1) 

    