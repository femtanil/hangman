from typing import Annotated

from fastapi import Depends, APIRouter

from app.models import GameStats
from app.dependencies import (
    oauth2_scheme,
    guess_character,
)

router = APIRouter(
    prefix="/logic",
    tags=["logic"],
)


@router.get("/status", response_model=GameStats)
async def read_game_status(token: Annotated[str, Depends(oauth2_scheme)]):
    pass


@router.post("/start", response_model=GameStats)
async def start_game(token: Annotated[str, Depends(oauth2_scheme)]):
    pass


@router.post("/guess", response_model=GameStats)
async def guess_letter(token: Annotated[str, Depends(oauth2_scheme)]):
    pass
