from sqlalchemy import (
        Column,
        Integer,
        Boolean,
        ForeignKey,
        )

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from configs.sessions import Base



class PaymentBook(Base):
    ''' Carnê '''
    __tablename__ = "payment_books"
    id = Column(Integer, primary_key=True, nullable=False)
    year = Column(Integer, nullable=False)
    is_payed = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    payer_id = Column(Integer,
                      ForeignKey("users.id", ondelete="CASCADE"),
                      nullable=False)
    payer = relationship("User", back_populates="payment_books")
    monthly_payments = relationship("MonthlyPayment", back_populates="payment_book")
