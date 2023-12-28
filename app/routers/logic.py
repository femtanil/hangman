from typing import Annotated

from fastapi import Depends, APIRouter

from app.models import Game
from app.dependencies import oauth2_scheme

router = APIRouter(
    prefix="/logic",
    tags=["logic"],
)


@router.get("/status", response_model=Game)
async def read_game_status(token: Annotated[str, Depends(oauth2_scheme)]):
    pass
