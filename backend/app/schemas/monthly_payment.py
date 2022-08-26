from typing import Optional
from pydantic import BaseModel
from pydantic.types import condecimal, UUID4

from ..helpers.convertion import to_camel

class MonthlyPaymentBase(BaseModel):
    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class MonthlyPaymentCreate(MonthlyPaymentBase):
    payment_book_id: UUID4
    price: condecimal(decimal_places=2) # type: ignore
    month: int
    is_payed: Optional[bool] = False

class MonthlyPaymentUpdate(MonthlyPaymentBase):
    price: Optional[condecimal(decimal_places=2)] # type: ignore
    month: Optional[int]
    is_payed: Optional[bool] = False

class MonthlyPaymentOut(MonthlyPaymentBase):
    payment_book_id: int
    price: float
    month: int
    is_payed: bool
