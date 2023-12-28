import os
from typing import Annotated

from fastapi import Depends, APIRouter, Query, HTTPException
from sqlmodel import Session, select
from dotenv import load_dotenv

from app.dependencies import get_own_player, create_new_player
from app.models import Player, PlayerRead
from app.database import get_session

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

router = APIRouter(
    prefix="/players",
    tags=["players"],
)


@router.post("/", response_model=PlayerRead)
async def create_player(player: Annotated[Player, Depends(create_new_player)]):
    return player


@router.get("/id={player_id}", response_model=PlayerRead)
async def read_player(player_id: int, session: Session = Depends(get_session)):
    player = session.get(Player, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.get("/", response_model=list[PlayerRead])
async def read_players(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: Session = Depends(get_session),
):
    players = session.exec(select(Player).offset(offset).limit(limit)).all()
    return players


@router.get("/me", response_model=PlayerRead)
async def read_players_me(current_player: Annotated[Player, Depends(get_own_player)]):
    return current_player
