<template>
    <form @submit="onSubmit" method="post">
        <div class="flex flex-col px-5">
            <AppInput v-model="character" v-bind="characterAttrs" placeholder="Type a letter" type="text" />
        </div>
        <div class="flex justify-center">
            <AppButton :disabled="isSubmitting" type="submit">{{ 'Confirm' }}</AppButton>
        </div>
    </form>
</template>
<script setup>
import { useForm } from 'vee-validate';
import { toTypedSchema } from '@vee-validate/yup';
import { object, string } from 'yup';
import AppInput from '@/components/AppInput.vue';
import AppButton from '@/components/AppButton.vue';

const schema = toTypedSchema(
    object({
        character: string().required().min(1).max(1).default(''),
    }),
);
const { errors, handleSubmit, isSubmitting, defineField } = useForm({
    validationSchema: schema,
});
const [character, characterAttrs] = defineField('character');

const onSubmit = handleSubmit(async (values, { resetForm }) => {
    const response = {};
    resetForm();
    return response;
});
</script>
