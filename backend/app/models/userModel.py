from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models.baseModel import TimeStampedModel
from app.models.userRoleModel import UserRoleModel 

class UserModel(TimeStampedModel):
    __tablename__ = 'AdminUsers'
    __table_args__ = {'schema': 'dbo'}

    ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    firstName = Column(String, nullable=False, index=True)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashPassword = Column(String, nullable=False)
    roleId = Column(Integer, ForeignKey('UserRole.ID'), nullable=True, index=True)

    userRole = relationship('UserRoleModel', back_populates = 'user')

    

