from typing import Annotated
from fastapi import Depends, APIRouter, WebSocket, WebSocketDisconnect

from app.game import Games

router = APIRouter(
    prefix="/websocket",
    tags=["websocket"],
)


@router.websocket("/ws/{player_id}")
async def websocket_endpoint(player_id: int, websocket: WebSocket):
    await websocket.accept()
    games = Games()

    try:
        games.create_game_instance(player_id)

        while True:
            data = await websocket.receive_text()
            # Handle messages from the client (e.g., guesses, commands)
            # Update game state and send updates back to the client
            await websocket.send_text(f"Message received: {data}")

    except WebSocketDisconnect:
        games.remove_game_instance(player_id)
        # Handle disconnection (e.g., clean up, notify other players)
