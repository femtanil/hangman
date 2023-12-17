class Game:
    """
    Main game logic.
    """

    MAX_TRIES: int = 5

    def __init__(self):
        self.word_to_guess: str = ""
        self.word_progress: str = ""
        self.guessed_positions: list[int] = []
        self.tries_left: int = Game.MAX_TRIES

    def construct_word_progress(self) -> None:
        """
        Contructs the word in its current state of discovery.

        Only the correctly guessed letters are present. Other letters are replaced with '*'.
        """

        if not self.word_progress:
            self.word_progress = "*" * len(self.word_to_guess)
        else:
            word_progress_split: list[str] = self.word_progress.split()  # type: ignore
            for pos in self.guessed_positions:
                word_progress_split[pos] = self.word_to_guess[pos]
            self.word_progress = "".join(word_progress_split)

    def update_word_to_guess(self) -> None:
        """
        Updates the word to guess.
        """
        self.word_to_guess = ""

    def update_guessed_positions(self, character: str) -> list[int]:
        """
        Updates the positions of guessed characters.

        After updating the guessed_positions list this method calls construct_word_progress() and
        updates tries_left.

        Args:
            character: The guessed character.

        Returns:
            Guessed positions list.
        """

        guessed_corretly: bool = False
        for pos, car in enumerate(self.word_to_guess):
            if character == car:
                self.guessed_positions.append(pos)
                guessed_corretly = True
        self.construct_word_progress()

        if not guessed_corretly:
            self.tries_left -= 1

        return self.guessed_positions

    def you_are_winrar(self) -> bool:
        """
        Checks the status of the game.

        Returns:
            True when player has won, false otherwise.
        """

        return self.word_to_guess == self.word_progress
