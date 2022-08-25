from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..configs.sessions import Base

from uuid import uuid4

from .monthly_payment import *
from .user import *


class PaymentBook(Base):
    ''' Carnê '''

    __tablename__ = "payment_books"
    payment_book_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4)
    year = Column(Integer, nullable=False)
    is_payed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    payer_id = Column(UUID(as_uuid=True),
                      ForeignKey("users.user_id", ondelete="CASCADE"),
                      nullable=False)
    payer = relationship("User", back_populates="payment_books")
    monthly_payments = relationship(
        'MonthlyPayment', back_populates="payment_book")
