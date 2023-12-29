import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGameStore = defineStore('game', () => {
    const playChoice = ref(false);
    const loginChoice = ref(false);
    const settingsChoice = ref(false);
    const playerId = ref(null);

    function setPlayChoice(value) {
        playChoice.value = value;
        loginChoice.value = !value;
        settingsChoice.value = !value;
    }

    function setLoginChoice(value) {
        playChoice.value = !value;
        loginChoice.value = value;
        settingsChoice.value = !value;
    }

    function setSettingsChoice(value) {
        playChoice.value = !value;
        loginChoice.value = !value;
        settingsChoice.value = value;
    }

    function setPlayerId(id) {
        playerId.value = id;
    }

    function resetChoices() {
        playChoice.value = false;
        loginChoice.value = false;
        settingsChoice.value = false;
    }

    return {
        playChoice,
        loginChoice,
        settingsChoice,
        setPlayChoice,
        setLoginChoice,
        setSettingsChoice,
        resetChoices,
        setPlayerId,
    }
})

