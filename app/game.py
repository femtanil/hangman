from fastapi import WebSocket, WebSocketDisconnect


class Game:
    MAX_TRIES: int = 5

    def __init__(self):
        self.word_to_guess: str = ""
        self.word_progress: str = ""
        self.guessed_positions: list[int] = []
        self.tries_left: int = Game.MAX_TRIES


class Games:
    """
    Main game logic.
    """

    def __init__(self):
        self.games: dict[int, Game] = {}
        self.active_connections: dict[int, WebSocket] = {}

    def create_game_instance(self, player_id: int) -> None:
        """
        Creates a game instance for a player.

        Args:
            player_id: The id of the player.
        """
        self.games[player_id] = Game()

    def remove_game_instance(self, player_id: int) -> None:
        """
        Removes a game instance of a player.

        Args:
            player_id: The id of the player.
        """
        try:
            self.games.pop(player_id)
        except KeyError:
            pass

    def get_game_instance(self, player_id: int) -> Game | None:
        """
        Gets the game instance of a player.

        Args:
            player_id: The id of the player.

        Returns:
            The game instance of the player. None if the player has no game instance.
        """
        return self.games.get(player_id, None)

    async def connect_game(self, websocket: WebSocket, player_id: int) -> None:
        """
        Connects a websocket to a player.

        Args:
            websocket: The websocket to connect.
            player_id: The id of the player.
        """
        await websocket.accept()
        self.active_connections[player_id] = websocket

    def disconnect_game(self, player_id: int) -> None:
        """
        Disconnects a websocket from a player.
        Args:
            player_id: The id of the player.
        """
        self.active_connections.pop(player_id)

    def construct_word_progress(self, player_id: int) -> None:
        """
        Contructs the word in its current state of discovery.

        Only the correctly guessed letters are present. Other letters are replaced with '*'.

        Args:
            player_id: The id of the player.
        """

        game: Game | None = self.get_game_instance(player_id)

        assert game is not None
        if not game.word_progress:
            game.word_progress = "*" * len(game.word_to_guess)
        else:
            word_progress_split: list[str] = game.word_progress.split()  # type: ignore
            for pos in game.guessed_positions:
                word_progress_split[pos] = game.word_to_guess[pos]
            game.word_progress = "".join(word_progress_split)

    def update_word_to_guess(self, player_id: int) -> None:
        """
        Updates the word to guess.

        Args:
            player_id: The id of the player.
        """
        game: Game | None = self.get_game_instance(player_id)

        assert game is not None
        game.word_to_guess = ""

    def update_guessed_positions(self, player_id: int, character: str) -> list[int]:
        """
        Updates the positions of guessed characters.

        After updating the guessed_positions list this method calls construct_word_progress() and
        updates tries_left.

        Args:
            player_id: The id of the player.
            character: The guessed character.

        Returns:
            Guessed positions list.
        """

        game: Game | None = self.get_game_instance(player_id)
        guessed_corretly: bool = False

        assert game is not None
        for pos, car in enumerate(game.word_to_guess):
            if character == car:
                game.guessed_positions.append(pos)
                guessed_corretly = True
        self.construct_word_progress(player_id)

        if not guessed_corretly:
            game.tries_left -= 1

        return game.guessed_positions

    def you_are_winrar(self, player_id: int) -> bool:
        """
        Checks the status of the game.

        Args:
            player_id: The id of the player.

        Returns:
            True when player has won, false otherwise.
        """

        game: Game | None = self.get_game_instance(player_id)

        assert game is not None
        return game.word_to_guess == game.word_progress
