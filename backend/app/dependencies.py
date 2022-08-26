from fastapi import status, HTTPException, Depends
from .services.oauth2 import get_auth_service
from .models.user import User

async def is_admin(current_user: User = Depends(get_auth_service().get_current_user)):
    if current_user and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Permission Denied")
    return True
