from datetime import datetime
import string
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    productName:str
    imageURL:Optional[str]
    product_price:str
    stock_id:int
    category_id:int
    sub_category_id:int
    class Config:
        from_attributes = True

class CreateProductSchema(ProductBase):
    class Config:
        from_attributes = True
    pass

class ProductSchema(ProductBase):
    ID: int
    created_at: datetime
    updated_at:Optional[datetime] 
    
    class Config:
        from_attributes = True

class ProductSchemaOut(ProductSchema):
    category_name: str
    subCategory_name: str
    stockStatus: str

    class Config:
        from_attributes = True