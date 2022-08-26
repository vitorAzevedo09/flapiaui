from fastapi import Depends
from sqlalchemy.orm import Session

from starlette.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

from ..models.user import User
from ..helpers.hash import hash
from ..schemas.user import UserCreate, UserUpdate
from ..configs.sessions import get_session

from .base import BaseService

class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, db_session: Session):
        super(UserService, self).__init__(User, db_session)

    def create(self, user: UserCreate) -> User:
        user.password = hash(user.password)
        db_user: User = self.model(**user.dict())
        self.db_session.add(db_user)
        try:
            self.db_session.commit()
        except IntegrityError as e:
            self.db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_user

def get_user_service(db_session: Session = Depends(get_session)) -> UserService:
    return UserService(db_session)
