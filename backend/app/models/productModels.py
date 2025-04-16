from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.baseModel import TimeStampedModel
from app.models.stockStatusModels import StockStatusModel
from app.models.mainCategoriesModels import MainCategoryModel
from app.models.subCategoriesModels import SubCategoriesModel




class ProductModel(TimeStampedModel):
    __tablename__ = 'Product'

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    productName = Column(String, nullable=False, unique=True)
    imageURL = Column(String, nullable = True)
    product_price = Column(String, nullable=False)
    # foreign keys
    stock_id = Column(Integer, ForeignKey('lookup.StockStatus.ID'), nullable= False, index=True)
    category_id = Column(Integer, ForeignKey('Categories.ID'), nullable=False, index=True)
    sub_category_id = Column(Integer, ForeignKey('SubCategories.ID'), nullable=False, index=True)

    # relationships
    stock = relationship('StockStatusModel')
    category= relationship('MainCategoryModel', back_populates='product')
    subCategory = relationship('SubCategoriesModel', back_populates='product')


