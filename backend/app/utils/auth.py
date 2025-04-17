from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from fastapi.security import  HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database.database import get_db
import jwt as _jwt
import os

from app.models.userModel import UserModel 
load_dotenv()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

security = HTTPBearer()

def hashPassword(password:str) -> str:
    return pwd_context.hash(password)

def verifyPassword(password:str, hashPassword:str):
    return pwd_context.verify(password, hashPassword)


def create_access_token(data:dict) -> str:
    to_encode:dict = data.copy()
    expire: datetime = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return _jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_code(token:str):
    try:
        payload: dict = _jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload.get('sub')
    except _jwt.ExpiredSignatureError:
        raise Exception('Token expired')
    except _jwt.PyJWTError:
        raise Exception('Invalid Token')
    
def getCurrentUser(admin_only: bool = False):
    def _get_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db)
    ):
        token = credentials.credentials
        try:
            payload = _jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email = payload.get("sub")
            if not email:
                raise HTTPException(status_code=401, detail="Invalid token: no subject")
        except _jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except _jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if admin_only and user.roleId != 1: 
            raise HTTPException(status_code=403, detail="Admins only")
        
        return user

    return _get_user
    
