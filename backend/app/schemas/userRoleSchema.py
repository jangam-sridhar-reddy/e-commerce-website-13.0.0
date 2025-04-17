from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserRoleBase(BaseModel):
    roleName:str

class CreateUserRoleSchema(UserRoleBase):
    model_config = {
        "from_attributes": True   
    }

class UserRoleSchema(UserRoleBase):
    ID:int
    created_at:datetime
    updated_at:Optional[datetime]

    model_config={
        "from_attributes": True
    }