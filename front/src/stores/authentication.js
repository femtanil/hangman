import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useAuthenticationStore = defineStore('authentication', () => {
    const tokenData = ref(null); // The token data of the logged in user.

    // This function is called when the user logs in.
    async function loginUser(formData) {
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_API_URL}/login/`,
                formData,
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    }
                },
            );
            tokenData.value = response.data;
        }
        catch (error) {
            console.log(error);
        }
    }

    async function logoutUser() {
        try {
            // No endpoint yet.
            /*
            await axios.post(
                `${import.meta.env.VITE_API_URL}/logout/`,
                {},
                {
                    headers: {
                        accept: 'application/json',
                        Authorization: `Bearer ${tokenData.value.access_token}`,
                    }
                }
            );
            */
            tokenData.value = null;
        }
        catch (error) {
            console.log(error);
        }
    }

    // This function is called when the user registers.
    async function registerUser(formData) {
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_API_URL}/register/`,
                formData);
            tokenData.value = response.data;
        }
        catch (error) {
            console.log(error);
        }
    }

    return {
        tokenData,
        loginUser,
        logoutUser,
        registerUser,
    }
})
