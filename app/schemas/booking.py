from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    booking_id: int
    start_time: datetime
    end_time: datetime
    booking_type: int


class BookingCreate(BookingBase):
    pass
