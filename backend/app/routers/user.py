from fastapi import APIRouter, status, Depends

from typing import List

from ..models.user import User
from ..schemas.user import UserOut, UserCreate
from ..services.user import UserService, get_user_service

router = APIRouter(prefix="/users", tags=['Users'])


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=UserOut)
async def create_user(user: UserCreate,
                      user_service: UserService = Depends(get_user_service)):
    return user_service.create(user)


@router.get('/',
            response_model=List[UserOut])
async def list_user(user_service: UserService = Depends(get_user_service)) -> List[User]:
    return user_service.list()
