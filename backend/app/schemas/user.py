from pydantic import BaseModel
from datetime import date

from helpers.convertion import to_camel

from payment_book import PaymentBookOut

class UserBase(BaseModel):
    class config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class UserCreate(UserBase):
    first_name: str
    last_name: str
    document: str
    password: str
    birth_date: date

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    document: str
    is_admin: bool
    payment_books: list[PaymentBookOut] = list()

class UserLogin(BaseModel):
    document: str
    password: str
