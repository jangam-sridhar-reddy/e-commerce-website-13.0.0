from fastapi import APIRouter, Depends 
from app.schemas.userSchema import CreateUserSchema, UserLoginSchema, UserSchema, TokenResponse
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.userServices import createUser, userLogin, getUser
from app.models.userModel import UserModel
from app.utils.auth import getCurrentUser

router = APIRouter(prefix='/auth', tags=['Authentication'])

 

@router.post('/registration', response_model=UserSchema)
def create_User(user:CreateUserSchema, db:Session = Depends(get_db)) -> UserModel:
    db_user: UserModel = createUser(user=user, db=db)
    return db_user


@router.post('/login', response_model = TokenResponse)
def user_login(login: UserLoginSchema, db:Session = Depends(get_db)) -> dict[str, str]:
    jwt_token_obj:dict[str, str] = userLogin(login=login, db=db)
    return jwt_token_obj

@router.get('/user', response_model = UserSchema)
def get_user(current_user: UserSchema = Depends(getCurrentUser())) -> UserModel:
    db_user: UserModel = current_user
    return db_user