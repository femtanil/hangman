import { defineStore } from 'pinia';
import { useAuthenticationStore } from '@/stores/authentication.js';
import { useGameStore } from '@/stores/game.js';
import { ref } from 'vue';

export const useWebsocketsStore = defineStore('websockets', () => {
    const authenticationStore = useAuthenticationStore();
    const gameStore = useGameStore();
    const socket = ref(null); // The websocket connection.
    const socketConnected = ref(false); // Whether the websocket is connected.
    const socketError = ref(null); // The error that occurred on the websocket.
    const socketMessage = ref(null); // The message that was received on the websocket.
    const socketReconnectAttempts = ref(0); // The number of times the websocket has tried to reconnect.
    const socketReconnectTimeout = ref(null); // The timeout that is used to reconnect the websocket.
    const socketReconnectTimeoutTime = ref(1000); // The time between reconnection attempts.
    const socketReconnectMaxAttempts = ref(10); // The maximum number of reconnection attempts.
    const socketReconnectMaxTimeoutTime = ref(10000); // The maximum time between reconnection attempts.

    function connectSocket() {
        socket.value = new WebSocket(`${import.meta.env.VITE_API_URL}/ws/game/id=${gameStore.player.value.id}/)}`);
        socket.value.onopen = () => {
            socketConnected.value = true;
            socketReconnectAttempts.value = 0;
        };
        socket.value.onerror = (error) => {
            socketError.value = error;
            console.log(error);
        };
        socket.value.onmessage = (message) => {
            socketMessage.value = message;
        };
        socket.value.onclose = () => {
            socketConnected.value = false;
            socketReconnectAttempts.value += 1;
            if (socketReconnectAttempts.value < socketReconnectMaxAttempts.value) {
                socketReconnectTimeout.value = setTimeout(
                    connectSocket,
                    Math.min(socketReconnectTimeoutTime.value * socketReconnectAttempts.value, socketReconnectMaxTimeoutTime.value),
                );
            }
        };
    }

    function disconnectSocket() {
        socket.value.close();
    }

    function sendSocketMessage(message) {
        socket.value.send(message);
    }

    function resetSocket() {
        socket.value = null;
        socketConnected.value = false;
        socketError.value = null;
        socketMessage.value = null;
        socketReconnectAttempts.value = 0;
        clearTimeout(socketReconnectTimeout.value);
    }

    function setSocketReconnectTimeoutTime(value) {
        socketReconnectTimeoutTime.value = value;
    }

    function setSocketReconnectMaxAttempts(value) {
        socketReconnectMaxAttempts.value = value;
    }

    function setSocketReconnectMaxTimeoutTime(value) {
        socketReconnectMaxTimeoutTime.value = value;
    }

    function resetSocketReconnectTimeoutTime() {
        socketReconnectTimeoutTime.value = 1000;
    }

    function resetSocketReconnectMaxAttempts() {
        socketReconnectMaxAttempts.value = 10;
    }

    function resetSocketReconnectMaxTimeoutTime() {
        socketReconnectMaxTimeoutTime.value = 10000;
    }

    function resetSocketReconnectSettings() {
        resetSocketReconnectTimeoutTime();
        resetSocketReconnectMaxAttempts();
        resetSocketReconnectMaxTimeoutTime();
    }

    function resetSocketSettings() {
        resetSocketReconnectSettings();
    }

    function resetWebsocketsStore() {
        resetSocket();
        resetSocketSettings();
    }

    return {
        socket,
        socketConnected,
        socketError,
        socketMessage,
        socketReconnectAttempts,
        socketReconnectTimeout,
        socketReconnectTimeoutTime,
        socketReconnectMaxAttempts,
        socketReconnectMaxTimeoutTime,
        connectSocket,
        disconnectSocket,
        sendSocketMessage,
        resetSocket,
        setSocketReconnectTimeoutTime,
        setSocketReconnectMaxAttempts,
        setSocketReconnectMaxTimeoutTime,
        resetSocketReconnectTimeoutTime,
        resetSocketReconnectMaxAttempts,
        resetSocketReconnectMaxTimeoutTime,
        resetSocketReconnectSettings,
        resetSocketSettings,
        resetWebsocketsStore,
    }
})
