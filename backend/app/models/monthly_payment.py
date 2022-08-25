from sqlalchemy import (
        Column,
        Integer,
        Boolean,
        Numeric,
        ForeignKey,
        )

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from configs.sessions import Base

from uuid import uuid4


class MonthlyPayment(Base):
    ''' Mensalidade '''
    __tablename__ = "monthly_payments"
    monthly_payments_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    price = Column(Numeric, nullable=False)
    month = Column(Integer,nullable=False)
    is_payed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    payment_book_id = Column(Integer,
                             ForeignKey("payment_books.payment_book_id",
                                        ondelete="CASCADE"),
                             nullable=False)
    payment_book = relationship("PaymentBook", back_populates="monthly_payments")
