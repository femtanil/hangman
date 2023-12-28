import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGameStore = defineStore('game', () => {
    const newGame = ref(false);
    const loadGame = ref(false);
    const gameStarted = ref(false);

    function setNewGame(value) {
        newGame.value = value;
        loadGame.value = !value;
    }

    function setLoadGame(value) {
        loadGame.value = value;
        newGame.value = !value;
    }

    function setGameStarted(value) {
        gameStarted.value = value;
    }

    function resetNewGame() {
        newGame.value = false;
    }

    function resetLoadGame() {
        loadGame.value = false;
    }

    return {
        newGame,
        loadGame,
        gameStarted,
        setNewGame,
        setLoadGame,
        setGameStarted,
        resetNewGame,
        resetLoadGame,
    }
})

