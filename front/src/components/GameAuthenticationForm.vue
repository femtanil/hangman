<template>
    <div class="flex flex-col">
        <h3 class="flex justify-center text-2xl">
            <slot name="formTitle"></slot>
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex flex-col px-5">
                <AppInput v-model="username" v-bind="usernameAttrs" type="text" class="input input-bordered text-xl"
                    :label="'Username'" />
            </div>
            <div class="flex flex-col px-5">
                <AppInput v-model="password" type="password" v-bind="passwordAttrs" class="input input-bordered text-xl"
                    :label="'Password'" />
            </div>
            <div v-if="props.confirmPassword" class="flex flex-col px-5">
                <AppInput v-model="passwordConfirmation" v-bind="passwordConfirmationAttrs" type="password"
                    class="input input-bordered text-xl" :label="'Confirm password'" />
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
import { useAuthenticationStore } from '@/stores/authentication.js';
import { useForm } from 'vee-validate';
import { toTypedSchema } from '@vee-validate/yup';
import { object, string } from 'yup';
import AppInput from '@/components/AppInput.vue';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';

const authenticationStore = useAuthenticationStore();
const props = defineProps({
    confirmPassword: {
        type: Boolean,
        required: true
    }
})

const schema = toTypedSchema(
    object({
        username: string().required().min(3).max(20),
        password: string().required().min(1).max(20),
        passwordConfirmation: string().required().min(8).max(20)
    }),
);
const { values, errors, defineField } = useForm({
    validationSchema: schema,
});

const [username, usernameAttrs] = defineField('username');
const [password, passwordAttrs] = defineField('password');
const [passwordConfirmation, passwordConfirmationAttrs] = defineField('passwordConfirmation');

async function submitForm() {
    const data = new FormData();
    data.append('username', values.username);
    data.append('password', values.password);
    data.append('scope',
        'user.create user:own user:own.write user:own:player user:own:player.write user:others:player:points user:others:player:playername');
    authenticationStore.loginUser(data);
}

</script>
