<template>
    <div class="flex flex-col">
        <h3 class="flex justify-center text-2xl">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex flex-col px-5">
                <label for="username" class="text-xl">Username</label>
                <input type="text" id="username" name="username" v-model="username" class="input input-bordered text-xl" />
            </div>
            <div class="flex flex-col px-5">
                <label for="password" class="text-xl">Password</label>
                <input type="password" id="password" name="password" v-model="password"
                    class="input input-bordered text-xl" />
            </div>
            <div v-if="props.confirmPassword" class="flex flex-col px-5">
                <label for="passwordConfirmation" class="text-xl">Confirm password</label>
                <input type="password" id="passwordConfirmation" name="passwordConfirmation" v-model="passwordConfirmation"
                    class="input input-bordered text-xl" />
            </div>
            <div class="flex justify-center">
                <input type="submit" value="Login" class="btn btn-ghost rounded-none text-3xl active:bg-transparent" />
            </div>
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <SelectScreenButton />
                </div>
            </div>
        </form>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import { useAuthenticationStore } from '@/stores/authentication.js';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';

const authenticationStore = useAuthenticationStore();
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
    const formData = new FormData();
    formData.append('username', username.value);
    formData.append('password', password.value);
    formData.append('scope',
        'user.create user:own user:own.write user:own:player user:own:player.write user:others:player:points user:others:player:playername');
    authenticationStore.loginUser(formData);
}

</script>
