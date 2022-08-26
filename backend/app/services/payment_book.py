
from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.payment_book import PaymentBook
from ..schemas.payment_book import PaymentBookCreate, PaymentBookUpdate
from ..configs.sessions import get_session

from .base import BaseService

class PaymentBookService(BaseService[PaymentBook, PaymentBookCreate, PaymentBookUpdate]):
    def __init__(self, db_session: Session):
        super(PaymentBookService, self).__init__(PaymentBook, db_session)

def get_payment_book_service(db_session: Session = Depends(get_session)) -> PaymentBookService:
    return PaymentBookService(db_session)
