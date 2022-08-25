from sqlalchemy import (
        Date,
        Column,
        String,
        Integer,
        Boolean,
        )

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..configs.sessions import Base

from uuid import uuid4

class User(Base):
    ''' Usuario '''
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True, unique=True)
    document = Column(String, nullable=False, unique=True)
    is_admin = Column(Boolean, default=False)
    password = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False,)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    logged_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=func.now())
    payment_books = relationship("PaymentBook", back_populates="payer")
