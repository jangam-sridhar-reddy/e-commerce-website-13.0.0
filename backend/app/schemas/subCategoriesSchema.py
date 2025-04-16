
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SubCategoriesBase(BaseModel):
    subCname:str  
    is_active:bool


class SubCategoriesCreateSchema(SubCategoriesBase):
    pass

class SubCategoriesSchema(SubCategoriesBase):
    ID: int
    created_at: datetime
    updated_at: Optional[datetime] 
   
    class Config:
        from_attributes = True
    


