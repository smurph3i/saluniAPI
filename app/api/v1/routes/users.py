from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.db.deps import get_db
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered",
        )
    hashed_password = get_password_hash(user_in.password)
    user = crud.create_user(db, user_in, hashed_password)
    return user
