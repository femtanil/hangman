from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, Session, SQLModel

from .database import engine


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: str | None = None
    scopes: list[str] = []


class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    player_id: int | None = Field(default=None, foreign_key="player.id")


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    banned: bool = Field(default=False)
    roles: str = Field(
        default="user.create user:own user:own.write user:own:player user:own:player.write user:others:player:points user:others:player:playername"
    )


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class PlayerBase(SQLModel):
    playername: str = Field(index=True, unique=True)
    user_id: int = Field(index=True, default=None, foreign_key="user.id")
    points: int = 0
    games_played: int = 0
    games_won: int = 0


class Player(PlayerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class PlayerCreate(PlayerBase):
    pass


class PlayerRead(PlayerBase):
    id: int


class Administration(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")


def create_fake_player():
    player: Player = Player(
        playername="a-player-name",
        user_id=0,
        points=1337,
        games_played=1,
        games_won=1,
        id=0,
    )
    db_player = Player.model_validate(player)
    session = Session(engine)
    session.add(db_player)
    try:
        session.commit()
    except IntegrityError:
        pass


def create_unauthenticated_user():
    user: User = User(
        id=1,
        username="unauthenticated",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        player_id=0,
    )
    db_user = User.model_validate(user)
    session = Session(engine)
    session.add(db_user)
    try:
        session.commit()
    except IntegrityError:
        pass


def create_admin_user():
    user: User = User(
        id=0,
        username="admin",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        roles="admin",
    )
    db_user = User.model_validate(user)
    session = Session(engine)
    session.add(db_user)
    try:
        session.commit()
    except IntegrityError:
        pass
