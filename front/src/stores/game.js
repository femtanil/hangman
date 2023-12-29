import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useGameStore = defineStore('game', () => {
    const playChoice = ref(false);
    const loginChoice = ref(false);
    const settingsChoice = ref(false);
    const player = ref(null);

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

    function resetChoices() {
        playChoice.value = false;
        loginChoice.value = false;
        settingsChoice.value = false;
    }

    async function createPlayer(playername) {
        try {
            const response = await axios.post(`${import.meta.env.VITE_BACKEND_URL}/players/`,
                {
                    "playername": playername,
                });
            player.value = response.data;
        }
        catch (error) {
            console.error(error);
        }
    }

    async function getOwnPlayer() {
        try {
            const response = await axios.get(`${import.meta.env.VITE_BACKEND_URL}/players/me`);
            player.value = response.data;
        }
        catch (error) {
            if (error.response.status === 404) {
                throw error;
            }
            else {
                console.log(error);
            }
        }
    }

    return {
        playChoice,
        loginChoice,
        settingsChoice,
        setPlayChoice,
        setLoginChoice,
        setSettingsChoice,
        resetChoices,
        createPlayer,
        getOwnPlayer,
    }
})

