from pydantic import BaseModel, Optional

from helpers.convertion import to_camel

class MonthlyPaymentBase(BaseModel):
    class config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class MonthlyPaymentCreate(MonthlyPaymentBase):
    payment_book_id: Optional[int] = None
    price: Optional[float] = None
    month: Optional[int] = None
    is_payed: Optional[bool] = False

class MonthlyPaymentOut(MonthlyPaymentBase):
    payment_book_id: int
    price: float
    month: int
    is_payed: bool
