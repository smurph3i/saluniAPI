from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    booking_id: int
    start_time: datetime
    end_time: datetime
    service_type: int
    notes: Optional[str] = None  # Optional notes field


class BookingCreate(BookingBase):
    pass


class Booking(BookingBase):
    id: int

    class Config:
        from_attributes = True
