
from sqlalchemy.orm import Session
from app.schemas.userSchema import CreateUserSchema, UserLoginSchema
from app.models.userModel import UserModel
from fastapi import HTTPException
from app.utils.auth import hashPassword, verifyPassword, create_access_token, decode_access_code




def createUser(user:CreateUserSchema, db:Session) -> UserModel:
    userExist = db.query(UserModel).filter(UserModel.email == user.email).first()

    if userExist:
        raise HTTPException(status_code=400, detail=f'Woops Email : {user.email} already in Use.')
    
    hash_password:str = hashPassword(user.hashPassword)

    new_user = UserModel(
        firstName = user.firstName,
        lastName = user.lastName,
        email  = user.email,
        hashPassword = hash_password,
        roleId = user.roleId
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def userLogin(login: UserLoginSchema, db:Session):
    userExist = db.query(UserModel).filter(UserModel.email == login.email).first()

    if not userExist or not verifyPassword(login.hashPassword, userExist.hashPassword):
        raise HTTPException(status_code=401, detail=f"Invalid credentials")

    token: str = create_access_token(data = {'sub': login.email})
    return {"access_token": token, 'token_type': "bearer"}

    
def getUser(token:str, db:Session) -> UserModel:
    try:
        get_email_from_token = decode_access_code(token=token)
        user = db.query(UserModel).filter(UserModel.email == get_email_from_token).first()
        if not user:
            raise HTTPException(status_code=401, detail='User Not Found')
        return user
        
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

