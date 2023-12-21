import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePlayerStore = defineStore('player', () => {
    const tokenData = ref(null);

    return {
        tokenData,
    }
})
