
from sqlalchemy import Boolean, Column, Integer, String 
from sqlalchemy.orm import relationship
from app.models.baseModel import TimeStampedModel 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.productModels import ProductModel


class MainCategoryModel(TimeStampedModel):
    __tablename__: str = 'Categories'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    cName = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, default=1) 

    product = relationship('ProductModel', back_populates='category')

