from sqlalchemy import Column, Integer, DateTime, String
from ..database.database import Base


class BookingDB(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    booking_type = Column(Integer)
    notes = Column(String, nullable=True)  # Optional notes field
