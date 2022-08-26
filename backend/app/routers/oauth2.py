from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..schemas.oauth2 import Token
from ..services.oauth2 import AuthService, get_auth_service

router: APIRouter = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService =  Depends(get_auth_service)) -> dict[str, str]:
    return auth_service.login(credentials=user_credentials)
