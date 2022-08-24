from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.monthly_payment import MonthlyPayment
from ..schemas.monthly_payment import MonthlyPaymentCreate, MonthlyPaymentUpdate
from ..configs.sessions import get_session

from .base import BaseService

class MonthlyPaymentService(BaseService[MonthlyPayment, MonthlyPaymentCreate, MonthlyPaymentUpdate]):
    def __init__(self, db_session: Session):
        super(MonthlyPaymentService, self).__init__(MonthlyPayment, db_session)

def get_monthly_payment_service(db_session: Session = Depends(get_session)) -> MonthlyPaymentService:
    return MonthlyPaymentService(db_session)
