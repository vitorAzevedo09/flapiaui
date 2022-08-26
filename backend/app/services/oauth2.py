from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException

from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import Any

from datetime import datetime, timedelta

from ..configs.settings import get_settings
from ..configs.sessions import get_session
from ..models.user import User
from ..schemas import oauth2
from ..helpers.hash import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = get_settings().SECRET_KEY
ALGORITHM = get_settings().ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = get_settings().ACCESS_TOKEN_EXPIRE_MINUTES


class AuthService():

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_access_token(self, data: dict):
        to_encode = data.copy()

        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt


    def verify_access_token(self,token: str, credentials_exception):

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            id: Any = payload.get("user_id")
            if id is None:
                raise credentials_exception
            token_data = oauth2.TokenData(id=id)
        except JWTError:
            raise credentials_exception

        return token_data


    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"})

        token_db = self.verify_access_token(token, credentials_exception)

        user = self.db_session.query(User).filter(User.id == token_db.id).first()
        return user


    def login(self, credentials: OAuth2PasswordRequestForm) -> dict[str, str]:
        user = self.db_session.query(User).filter(
            User.document == credentials.username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail=f"Invalid Credentials")

        if not verify(credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail=f"Invalid Credentials")

        access_token = self.create_access_token(data={"user_id": str(user.user_id)})

        return {"access_token": access_token, "token_type": "bearer"}


def get_auth_service(db_session: Session = Depends(get_session)) -> AuthService:
    return AuthService(db_session)
