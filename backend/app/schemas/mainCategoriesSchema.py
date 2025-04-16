from typing import  Optional
from datetime import datetime
from pydantic import BaseModel 


class MainCategoryBase(BaseModel):
    cName:str
    is_active:bool

class CreateMainCategory(MainCategoryBase):
    pass

class MainCategorySchema(MainCategoryBase):
    ID: int
    created_at: datetime
    updated_at: Optional[datetime] 

     

