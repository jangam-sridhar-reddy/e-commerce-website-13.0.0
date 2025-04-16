from pydantic import BaseModel

class stockStatusSchema(BaseModel):
    ID:int
    statusName:str