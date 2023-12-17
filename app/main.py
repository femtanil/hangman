from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import logic

from .routers import tokens, players
from .database import create_db_and_tables

origins = [
    "http://localhost:5173",
    "https://localhost:5173",
    "http://arch-veehaim:5173",
    "https://arch-veehaim:5173",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


api = FastAPI(lifespan=lifespan)

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api.include_router(logic.router)
api.include_router(tokens.router)
api.include_router(players.router)
