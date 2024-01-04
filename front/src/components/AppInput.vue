<template>
    <label v-if="label">{{ label }}</label>
    <input type="text" :value="modelValue" @input="emit('update:modelValue', $event.target.value)" v-bind="$attrs" />
</template>
<script setup>
const props = defineProps({
    label: {
        type: [String, Boolean],
    },
    modelValue: {
        type: String,
        default: '',
    }
})

const emit = defineEmits(['update:modelValue']);
</script>
