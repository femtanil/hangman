from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, Session, SQLModel

from .database import engine


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None


class PlayerBase(SQLModel):
    username: str = Field(index=True, unique=True)
    points: int = 0
    games_played: int = 0
    games_won: int = 0
    banned: bool = False


class Player(PlayerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str


class PlayerCreate(PlayerBase):
    password: str


class PlayerRead(PlayerBase):
    id: int


class Administration(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    player_id: int = Field(foreign_key="player.id")


class Game(SQLModel):
    word_to_guess: str
    word_progress: str
    tries_left: int


def create_fake_player():
    player: Player = Player(
        username="femtanil",
        points=1337,
        games_played=1,
        games_won=1,
        banned=False,
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        id=0,
    )
    db_player = Player.model_validate(player)
    session = Session(engine)
    session.add(db_player)
    try:
        session.commit()
    except IntegrityError:
        pass
