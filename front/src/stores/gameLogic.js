import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGameLogicStore = defineStore('gameLogic', () => {
    const gameStarted = ref(false); // The game has started.
    const wordToGuess = ref(null); // The word to guess.

    const startGame = function() {
        gameStarted.value = true;
    }

    const endGame = function() {
        gameStarted.value = false;
    }

    return {
        startGame,
        endGame,
        gameStarted,
        wordToGuess,
    }
})
