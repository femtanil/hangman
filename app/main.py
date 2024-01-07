import os
import json
from contextlib import asynccontextmanager

from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import logic, tokens, users, players
from .database import create_db_and_tables
from .models import create_fake_player, create_unauthenticated_user, create_admin_user


ORIGINS: list = json.loads(os.getenv("ORIGINS"))  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_admin_user()
    create_fake_player()
    create_unauthenticated_user()
    yield


api = FastAPI(lifespan=lifespan)

api.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(tokens.router)
api.include_router(logic.router)
api.include_router(players.router)
api.include_router(users.router)
