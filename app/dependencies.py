import os
from typing import Annotated

from fastapi import Depends, HTTPException, Query, Security, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt
from dotenv import load_dotenv
from pydantic import ValidationError
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from .models import Player, PlayerCreate, User, UserCreate, TokenData
from .database import engine
from .authentication import get_password_hash

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={
        "user.create": "The ability to create a new user.",
        "user:own": "Read only access to the current user's information.",
        "user:own.write": "The ability to change the current user's information.",
        "user:own:player": "Read only access to the current user's player.",
        "user:own:player.write": "The ability to change the current user's player.",
        "user:others:player:points": "Read only access to players' points.",
        "user:others:player:playername": "Read only access to players' playernames.",
        "admin": "Full access to all information.",
    },
    auto_error=True,
)


async def get_user_by_username(username: str) -> User:
    with Session(engine) as session:
        try:
            user = session.exec(select(User).where(User.username == username)).one()
            return user
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )


async def validate_token(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
) -> TokenData:
    """Validate token and check if it has the required scopes.
    Args:
        security_scopes: Scopes required by the dependent.
        token: Token to validate.
    Returns:
        A TokenData instance representing the token data.
    """
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    permissions_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not enough permissions",
        headers={"WWW-Authenticate": authenticate_value},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception

    try:
        assert token_data.username is not None
        user = await get_user_by_username(token_data.username)
        user_scopes: list[str] = user.roles.split(" ")
        # Iterating through token scopes against scopes defined in user instance.
        for scope in token_data.scopes:
            if scope not in user_scopes:
                print(f"scope {scope} not in {user_scopes}")
                raise permissions_exception
    except HTTPException as e:
        raise e

    # Iterating through dependent's scopes against scopes defined in token.
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise permissions_exception
    return token_data


async def get_own_user(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["user:own"])]
) -> User:
    """Get own user.
    Args:
        token_data: Token data.
    Returns:
        A User instance representing own user.
    """
    assert token_data.username is not None
    user: User = await get_user_by_username(token_data.username)

    if user.banned:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Banned user"
        )
    return user


async def create_new_user(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["user.create"])],
    user: UserCreate,
) -> User:
    """Create new user.
    Args:
        token_data: Token data.
        user: User to create.
    Returns:
        A User instance representing the created user.
    """
    if token_data.username != user.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username in token and body do not match",
        )

    with Session(engine) as session:
        try:
            # Should not be possible, but better be bulletproof.
            session.exec(select(User).where(User.username == user.username)).one()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this username already exists",
            )
        except NoResultFound:
            pass
    hashed_password: str = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db_user = User.model_validate(new_user)
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
    return db_user


async def get_users(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["admin"])],
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    with Session(engine) as session:
        users = session.exec(select(User).offset(offset).limit(limit)).all()
        return users


async def get_user_by_id(user_id: int) -> User:
    with Session(engine) as session:
        try:
            user = session.exec(select(User).where(User.id == user_id)).one()
            return user
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )


async def get_user(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["admin"])],
    user_id: int,
) -> User:
    return await get_user_by_id(user_id)


async def remove_user_by_id(user_id: int) -> User:
    with Session(engine) as session:
        try:
            user = session.exec(select(User).where(User.id == user_id)).one()
            session.delete(user)
            session.commit()
            return user
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )


async def remove_user(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["admin"])],
    user_id: int,
) -> User:
    return await remove_user_by_id(user_id)


async def remove_own_user(user: Annotated[User, Depends(get_own_user)]) -> User:
    assert user.id is not None
    return await remove_user_by_id(user.id)


async def get_own_player(
    token_data: Annotated[
        TokenData, Security(validate_token, scopes=["user:own:player"])
    ]
) -> Player:
    with Session(engine) as session:
        try:
            player = session.exec(
                select(Player).where(Player.username == token_data.username)
            ).one()
            return player
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User has no player"
            )


async def create_new_player(
    token_data: Annotated[
        TokenData, Security(validate_token, scopes=["user:own.write"])
    ],
    player: PlayerCreate,
):
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
    new_player = Player(playername=player.username)
    db_player = Player.model_validate(new_player)
    with Session(engine) as session:
        session.add(db_player)
        session.commit()
        session.refresh(db_player)
    return db_player


async def remove_player_by_id(player_id: int) -> Player:
    with Session(engine) as session:
        try:
            player = session.exec(select(Player).where(Player.id == player_id)).one()
            session.delete(player)
            session.commit()
            return player
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Player does not exist"
            )


async def remove_player(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["admin"])],
    player_id: int,
) -> Player:
    return await remove_player_by_id(player_id)


async def remove_own_player(user: Annotated[User, Depends(get_own_user)]) -> Player:
    assert user.player_id is not None
    return await remove_player_by_id(user.player_id)
