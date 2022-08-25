from pydantic.types import UUID4
from pydantic import BaseModel
from datetime import date
from typing import Optional

from ..helpers.convertion import to_camel

from .payment_book import PaymentBookOut

class UserBase(BaseModel):
    class config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class UserCreate(UserBase):
    user_id: UUID4
    first_name: str
    last_name: str
    document: str
    password: str
    birth_date: date

class UserUpdate(UserBase):
    first_name: Optional[str]
    last_name: Optional[str]
    document: Optional[str]
    password: Optional[str]
    birth_date: Optional[date]


class UserOut(BaseModel):
    user_id: UUID4
    first_name: str
    last_name: str
    document: str
    is_admin: bool
    payment_books: list[PaymentBookOut] = list()

class UserLogin(BaseModel):
    document: str
    password: str
