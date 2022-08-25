from fastapi import APIRouter, status, Depends

from typing import List
from pydantic import UUID4

from ..models.user import User
from ..schemas.user import UserOut, UserCreate, UserUpdate
from ..services.user import UserService, get_user_service

router = APIRouter(prefix="/users", tags=['Users'])


@router.get('/{id}',
            response_model=UserOut)
async def get_user(id: UUID4,
                   user_service: UserService = Depends(get_user_service)):
    return user_service.get(id=id)


@router.post('/{id}',
             status_code=status.HTTP_201_CREATED,
             response_model=UserOut)
async def create_user(user: UserCreate,
                      user_service: UserService = Depends(get_user_service)):
    return user_service.create(user)


@router.get('/',
            response_model=List[UserOut])
async def list_user(user_service: UserService = Depends(get_user_service)) -> List[User]:
    return user_service.list()


@router.patch('/{id}',
              response_model=UserOut)
async def update_user(id: UUID4,
                      user: UserUpdate,
                      user_service: UserService = Depends(get_user_service)):
    return user_service.update(id=id, obj=user)


@router.delete('/{id}',
               status_code=status.HTTP_200_OK)
async def delete_user(
        id: UUID4,
        user_service: UserService = Depends(get_user_service)) -> None:
    return user_service.delete(id=id)
