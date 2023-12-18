import { defineStore } from 'pinia'

export const useGameStore = defineStore('game', () => {
    const newGame = ref(false);
    const loadGame = ref(false);

    function setNewGame() {
        newGame.value = true;
    }
    function setLoadGame() {
        loadGame.value = true;
    }

    return {
        newGame,
        loadGame,
        setNewGame,
        setLoadGame,
    }
})

