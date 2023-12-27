import os
from typing import Annotated

from fastapi import Depends, HTTPException, Security, status
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
        "user:own": "Access information about the current user.",
        "user": "Read only acces to full user information.",
        "user.write": "The ability to create, update or delete an entire user.",
        "user:player": "Read only access to details about user's players.",
        "user:player.write": "The ability to change player details for a user.",
        "admin": "Full access to all information.",
    },
    auto_error=True,
)


async def validate_token(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
) -> (TokenData):
    """Validate token and check if it has the required scopes.
    Args:
        security_scopes: Required scopes.
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

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return token_data


async def get_current_user(
    token_data: Annotated[TokenData, Security(validate_token, scopes=["user:own"])]
) -> User:
    """Get current user.
    Args:
        token_data: Token data.
    Returns:
        A User instance representing the current user.
    """
    with Session(engine) as session:
        try:
            user = session.exec(
                select(User).where(User.username == token_data.username)
            ).one()
            return user
        except AttributeError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="No current user"
            )


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    """Get current active user.
    Args:
        current_user: Current user.
    Returns:
        A User instance representing the current active user.
    """
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not authenticated"
        )
    elif current_user.banned:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Banned user"
        )
    return current_user


async def create_new_user(
    token_data: Annotated[TokenData, Depends(validate_token)], user: UserCreate
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
    elif current_player.banned:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Banned player"
        )
    return current_player


async def create_new_player(
    token_data: Annotated[TokenData, Depends(validate_token)], player: PlayerCreate
):
    if token_data.username != player.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Player in token and body do not match",
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
    new_player = Player(playername=player.username)
    db_player = Player.model_validate(new_player)
    with Session(engine) as session:
        session.add(db_player)
        session.commit()
        session.refresh(db_player)
    return db_player
