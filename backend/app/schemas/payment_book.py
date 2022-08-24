from pydantic import BaseModel

from helpers.convertion import to_camel

from monthly_payment import MonthlyPaymentOut

class PaymentBookBase(BaseModel):
    class config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class PaymentBookCreate(PaymentBookBase):
    payer_id: int
    year: int


class PaymentBookOut(PaymentBookBase):
    payer_id: int
    year: int
    is_payed: bool
    monthly_payments: list[MonthlyPaymentOut] = list()
