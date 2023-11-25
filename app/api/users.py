from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.db import get_db
import app.schemas.user as userSchema
import app.cruds.user as userCruds

router = APIRouter()


@router.get("/", response_model=list[userSchema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCruds.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userCruds.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userCruds.create_user(db=db, user=user)
