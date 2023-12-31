<template>
    <div class="grid grid-flow-row">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <label for="username" class="flex justify-text-3xl xs:text-4xl">Username</label>
                    <input type="text" id="username" name="username" v-model="username"
                        class="text-3xl xs:text-4xl w-fit" />
                </div>
            </div>
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <label for="password" class="text-3xl xs:text-4xl">Password</label>
                    <input type="password" id="password" name="password" v-model="password"
                        class="text-3xl xs:text-4xl w-fit" />
                </div>
            </div>
            <div v-if="props.confirmPassword" class="flex justify-center">
                <div class="grid grid-flow-row">
                    <label for="passwordConfirmation" class="text-3xl xs:text-4xl">Confirm password</label>
                    <input type="password" id="passwordConfirmation" name="passwordConfirmation"
                        v-model="passwordConfirmation" class="text-3xl xs:text-4xl w-fit" />
                </div>
            </div>
            <!-- Very unsafe, but it's just a demo -->
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <input type="submit" value="Login"
                        class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-fit" />
                </div>
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
