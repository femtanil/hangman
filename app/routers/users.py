import os
from typing import Annotated

from fastapi import Depends, APIRouter, Query, HTTPException
from sqlmodel import Session, select
from dotenv import load_dotenv

from app.dependencies import get_own_user, create_new_user
from app.models import User, UserRead
from app.database import get_session

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=UserRead)
async def create_user(user: Annotated[User, Depends(create_new_user)]):
    return user


@router.get("/id={user_id}", response_model=UserRead)
async def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[UserRead])
async def read_users(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: Session = Depends(get_session),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@router.get("/me", response_model=UserRead)
async def read_own_user(
    current_user: Annotated[User, Depends(get_own_user)]
):
    return current_user
