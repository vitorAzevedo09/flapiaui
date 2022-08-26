from fastapi.security import OAuth2PasswordBearer
from fastapi import status, HTTPException, Depends
from .services.oauth2 import AuthService, get_auth_service
from .models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

async def is_admin(auth_service: AuthService = Depends(get_auth_service),
        token: str = Depends(oauth2_scheme)
        ):
    current_user = await auth_service.get_current_user(token=token)
    if current_user and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Permission Denied")
    return True
