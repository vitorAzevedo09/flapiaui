from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..schemas.oauth2 import Token
from ..services import oauth2

router: APIRouter = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    return oauth2.login(user_credentials=user_credentials)
