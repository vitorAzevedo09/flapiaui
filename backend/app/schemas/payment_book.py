from pydantic import BaseModel
from pydantic.types import UUID4

from ..helpers.convertion import to_camel

from .monthly_payment import MonthlyPaymentOut

class PaymentBookBase(BaseModel):
    class config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class PaymentBookCreate(PaymentBookBase):
    payment_book_id: UUID4
    payer_id: UUID4
    year: int

class PaymentBookUpdate(PaymentBookBase):
    payer_id: UUID4
    is_payed: bool
    year: int

class PaymentBookOut(PaymentBookBase):
    payer_id: UUID4
    year: int
    is_payed: bool
    monthly_payments: list[MonthlyPaymentOut] = list()
