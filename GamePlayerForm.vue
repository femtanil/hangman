<template>
    <div class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="grid grid-flow-row">
                <label for="username" class="text-3xl xs:text-4xl">Player name</label>
                <input type="text" id="username" name="username" v-model="username" class="text-3xl xs:text-4xl" />
                <label for="password" class="text-3xl xs:text-4xl">Password</label>
                <input type="password" id="password" name="password" v-model="password" class="text-3xl xs:text-4xl" />
                <div v-if="props.confirmPassword">
                    <label for="password2" class="text-3xl xs:text-4xl">Confirm password</label>
                    <input type="password" id="password2" name="password2" v-model="password2"
                        class="text-3xl xs:text-4xl" />
                </div>
                <!-- Very unsafe, but it's just a demo -->
                <input type="submit" value="Start"
                    class=" btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full" />
                <SelectScreenButton />
            </div>
        </form>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useGameStore } from '@/stores/game.js';
import { usePlayerStore } from '@/stores/player.js';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';

const gameStore = useGameStore();
const playerStore = usePlayerStore();
const username = ref('')
const password = ref('')
const props = defineProps({
    confirmPassword: {
        type: Boolean,
        required: true
    }
})

async function submitForm() {
    const loginFormData = new FormData();
    loginFormData.append('username', username.value);
    loginFormData.append('password', password.value);

    if (gameStore.newGame == true) {
        try {
            playerStore.tokenData = await axios.post(
                `${import.meta.env.VITE_BACKEND_URL}/signup/`,
                loginFormData);
        }
        catch (error) {
            console.log(error);
        }
    }
    else if (gameStore.loadGame == true) {
        try {
            playerStore.tokenData = await axios.post(
                `${import.meta.env.VITE_BACKEND_URL}/login/`,
                loginFormData);
        }
        catch (error) {
            console.log(error);
        }
    }
}

</script>
