from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, update
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from .database.database import get_db, engine
from .models import booking as booking_models
from .schemas import booking as booking_schemas


app = FastAPI(
    title="Saluni Booking API",
    description="API for managing Salon Bookings",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/bookings/", response_model=booking_schemas.Booking, status_code=201)
async def create_booking(booking: booking_schemas.BookingCreate, db: AsyncSession = Depends(get_db)):
    """
    Creates a new booking.

    Raises:
        HTTPException (400): If a booking of the same type overlaps with an existing booking.
        HTTPException (500): If a database error occurs.
    """
    try:
        overlap_check = await db.execute(
            booking_models.BookingDB.__table__.select().where(
                and_(
                    booking_models.BookingDB.booking_type == booking.booking_type,
                    booking_models.BookingDB.start_time < booking.end_time,
                    booking.start_time < booking_models.BookingDB.end_time,
                )
            )
        )
        overlap_result = overlap_check.scalar_one_or_none()
        if overlap_result:
            raise HTTPException(
                status_code=400,
                detail="Booking overlaps with an existing booking of the same type.",
            )

        db_booking = booking_models.BookingDB(**booking.model_dump())
        db.add(db_booking)
        await db.commit()
        await db.refresh(db_booking)
        return db_booking
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.get("/bookings/{booking_id}", response_model=booking_schemas.Booking)
async def read_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieves a booking by ID."""
    result = await db.execute(booking_models.BookingDB.__table__.select().where(booking_models.BookingDB.id == booking_id))
    db_booking = result.scalar_one_or_none()
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking_schemas.Booking.model_validate(db_booking)


@app.get("/bookings/", response_model=List[booking_schemas.Booking])
async def read_bookings(
    user_id: int = None,
    booking_type: int = None,
    db: AsyncSession = Depends(get_db),
):
    """Retrieves all bookings, or filters by user_id and/or booking_type."""
    try:
        query = select(booking_models.BookingDB)
        conditions = []

        if user_id is not None:
            conditions.append(booking_models.BookingDB.user_id == user_id)
        if booking_type is not None:
            conditions.append(
                booking_models.BookingDB.booking_type == booking_type)

        if conditions:
            query = query.where(and_(*conditions))

        result = await db.execute(query)
        bookings = result.scalars().all()
        return [booking_schemas.Booking.model_validate(booking) for booking in bookings]

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.put("/bookings/{booking_id}", response_model=booking_schemas.Booking)
async def update_booking(
    booking_id: int,
    updated_booking: booking_schemas.BookingCreate,
    db: AsyncSession = Depends(get_db),
):
    """Updates a booking by ID."""
    try:
        # Check if booking exists
        query = select(booking_models.BookingDB).where(
            booking_models.BookingDB.id == booking_id)
        result = await db.execute(query)
        db_booking = result.scalar_one_or_none()

        if db_booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")

        # Check for overlaps
        overlap_query = select(booking_models.BookingDB).where(
            and_(
                booking_models.BookingDB.id != booking_id,
                booking_models.BookingDB.booking_type == updated_booking.booking_type,
                booking_models.BookingDB.start_time < updated_booking.end_time,
                updated_booking.start_time < booking_models.BookingDB.end_time,
            )
        )
        overlap_result = await db.execute(overlap_query)
        if overlap_result.scalar_one_or_none():
            raise HTTPException(
                status_code=400,
                detail="Updated booking overlaps with an existing booking of the same type.",
            )

        # Update the booking
        # only update fields that were sent.
        update_data = updated_booking.model_dump(exclude_unset=True)

        update_query = (
            update(booking_models.BookingDB)
            .where(booking_models.BookingDB.id == booking_id)
            .values(**update_data)
        )

        await db.execute(update_query)
        await db.commit()

        # Refresh the booking to get updated data
        refresh_query = select(booking_models.BookingDB).where(
            booking_models.BookingDB.id == booking_id)
        refresh_result = await db.execute(refresh_query)
        db_booking = refresh_result.scalar_one()

        return booking_schemas.Booking.model_validate(db_booking)
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}")


@app.delete("/bookings/{booking_id}", status_code=204)
async def delete_booking(booking_id: int, db: AsyncSession = Depends(get_db)):
    """Deletes a booking by ID."""
    try:
        query = select(booking_models.BookingDB).where(
            booking_models.BookingDB.id == booking_id)
        result = await db.execute(query)
        db_booking = result.scalar_one_or_none()

        if db_booking is None:
            raise HTTPException(status_code=404, detail="Booking not found")

        await db.delete(db_booking)
        await db.commit()
        return None  # Explicitly return None

    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {str(e)}")
