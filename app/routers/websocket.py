from typing import Annotated
from fastapi import APIRouter, Security, WebSocket, WebSocketDisconnect

from app.dependencies import validate_token
from app.game import Games
from app.models import TokenData

router = APIRouter(
    prefix="/ws",
    tags=["ws"],
)


@router.websocket("/{player_id}")
async def websocket_endpoint(
    player_id: int,
    websocket: WebSocket,
    token_data: Annotated[TokenData, Security(validate_token, scopes=["websockets"])],
):
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
