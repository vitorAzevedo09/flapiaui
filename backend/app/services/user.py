from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserCreate, UserUpdate
from ..configs.sessions import get_session

from .base import BaseService

class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, db_session: Session):
        super(UserService, self).__init__(User, db_session)

def get_user_service(db_session: Session = Depends(get_session)) -> UserService:
    return UserService(db_session)
