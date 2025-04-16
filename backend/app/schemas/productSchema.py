from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    productName:str
    imageURL:Optional[str]
    product_price:str
    stock_id:int
    category_id:int
    sub_category_id:int

class CreateProductSchema(ProductBase):
    pass

class ProductSchema(ProductBase):
    ID: int
    created_at: datetime
    updated_at:Optional[datetime] 