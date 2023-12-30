import { defineStore } from 'pinia';
import { useAuthenticationStore } from '@/stores/authentication.js';
import { ref, watch } from 'vue';
import axios from 'axios';

export const useGameStore = defineStore('game', () => {
    const gameStarted = ref(false); // The game has started.
    const playChoice = ref(false); // The user has chosen to play.
    const loginChoice = ref(false); // The user has chosen to login.
    const settingsChoice = ref(false); // The user has chosen to go to settings.
    const player = ref(null); // The player object of the logged in user.
    const authenticationStore = useAuthenticationStore();

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

    // This function is called when the user logs in.
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

    watch(authenticationStore.tokenData, async (tokenData) => {
        if (tokenData) {
            await getOwnPlayer();
        }
        else {
            player.value = null;
        }
    });

    return {
        playChoice,
        loginChoice,
        settingsChoice,
        setPlayChoice,
        setLoginChoice,
        setSettingsChoice,
        resetChoices,
        createPlayer,
        gameStarted,
    }
})

