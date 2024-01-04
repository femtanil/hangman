<template>
    <div class="flex flex-col">
        <h3 class="flex justify-center text-2xl">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex flex-col px-5">
                <AppInput v-model="username" type="text" class="input input-bordered text-xl" :label="'Username'" />
            </div>
            <div class="flex flex-col px-5">
                <AppInput v-model="password" type="password" class="input input-bordered text-xl" :label="'Password'" />
            </div>
            <div v-if="props.confirmPassword" class="flex flex-col px-5">
                <AppInput v-model="passwordConfirmation" type="password" class="input input-bordered text-xl"
                    :label="'Confirm password'" />
            </div>
            <div class="flex justify-center">
                <AppInput type="submit" value="Login" class="btn btn-ghost rounded-none text-3xl active:bg-transparent" />
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
import AppInput from '@/components/AppInput.vue';
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
