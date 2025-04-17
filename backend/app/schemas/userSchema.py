from datetime import datetime
from typing import Optional 
from pydantic import BaseModel, EmailStr

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserLoginSchema(BaseModel):
    email:EmailStr
    hashPassword:str

class UserBase(UserLoginSchema):
    firstName:str
    lastName:str
    roleId:int

class CreateUserSchema(UserBase):
    
    model_config = {
        "from_attributes": True   
    }
    

class UserSchema(BaseModel):
    ID:int
    firstName:str
    lastName:str
    email:EmailStr
    roleId:int
    created_at:datetime
    updated_at:Optional[datetime]

    model_config = {
        "from_attributes": True   
    }
