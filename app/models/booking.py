from sqlalchemy import Column, Integer, DateTime
from ..database.database import Base


class BookingDB(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    booking_type = Column(Integer)
