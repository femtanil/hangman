import os
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dotenv import load_dotenv
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from .models import Player, PlayerCreate, TokenData
from .database import engine
from .authentication import get_password_hash

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


async def validate_token(token: Annotated[str, Depends(oauth2_scheme)]):
    if token is None:
        return None

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_player(token_data: Annotated[TokenData, Depends(validate_token)]):
    with Session(engine) as session:
        try:
            player = session.exec(
                select(Player).where(Player.username == token_data.username)
            ).one()
            return player
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No current player"
            )


async def get_current_active_player(
    current_player: Annotated[Player, Depends(get_current_player)]
):
    if current_player is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Player not authenticated"
        )
    elif current_player.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive player"
        )
    return current_player


async def create_new_player(
    token_data: Annotated[str, Depends(validate_token)], player: PlayerCreate
):
    if token_data is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authenticated players cannot create new players",
        )

    with Session(engine) as session:
        try:
            # Should not be possible, but better be bulletproof.
            session.exec(select(Player).where(Player.username == player.username)).one()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Player with this username already exists",
            )
        except NoResultFound:
            pass
    hashed_password: str = get_password_hash(player.password)
    new_player = Player(username=player.username, hashed_password=hashed_password)
    db_player = Player.model_validate(new_player)
    with Session(engine) as session:
        session.add(db_player)
        session.commit()
        session.refresh(db_player)
    return db_player
