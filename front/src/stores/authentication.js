import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useAuthenticationStore = defineStore('authentication', () => {
    const tokenData = ref(null);

    async function loginUser(formData) {
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_BACKEND_URL}/login/`,
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
    }
})