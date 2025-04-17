from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.baseModel import TimeStampedModel

class UserRoleModel(TimeStampedModel):
    __tablename__ = "UserRole"

    ID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    roleName = Column(String, nullable=False, index=True, unique=True)

    user = relationship('UserModel', back_populates='userRole')