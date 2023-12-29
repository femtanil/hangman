<template>
    <div class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="grid grid-flow-row">
                <label for="username" class="text-3xl xs:text-4xl">Username</label>
                <input type="text" id="username" name="username" v-model="username" class="text-3xl xs:text-4xl" />
                <label for="password" class="text-3xl xs:text-4xl">Password</label>
                <input type="password" id="password" name="password" v-model="password" class="text-3xl xs:text-4xl" />
                <div v-if="props.confirmPassword">
                    <label for="passwordConfirmation" class="text-3xl xs:text-4xl">Confirm password</label>
                    <input type="password" id="passwordConfirmation" name="passwordConfirmation"
                        v-model="passwordConfirmation" class="text-3xl xs:text-4xl" />
                </div>
                <!-- Very unsafe, but it's just a demo -->
                <input type="submit" value="Login"
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
import { useUserStore } from '@/stores/user.js';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';

const gameStore = useGameStore();
const userStore = useUserStore();
const username = ref('')
const password = ref('')
const passwordConfirmation = ref('')
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

    if (gameStore.loginChoice) {
        try {
            const response = await axios.post(
                `${import.meta.env.VITE_BACKEND_URL}/login/`,
                loginFormData);
            userStore.tokenData = response.data;
        }
        catch (error) {
            console.log(error);
        }
    }
}

</script>
