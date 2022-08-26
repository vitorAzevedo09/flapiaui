

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException

from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import Any

from datetime import datetime, timedelta

from ..configs.settings import get_settings
from ..configs.sessions import get_session
from ..schemas import oauth2
from ..models.user import User
from ..helpers.hash import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET_KEY
# Algorithm
# Expriation time

SECRET_KEY = get_settings().SECRET_KEY
ALGORITHM = get_settings().ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = get_settings().ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: Any = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = oauth2.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})

    token_db: oauth2.TokenData = verify_access_token(token, credentials_exception)

    user = db.query(User).filter(User.id == token_db.id).first()

    return user
