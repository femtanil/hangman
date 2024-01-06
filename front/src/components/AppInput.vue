<template>
    <label v-if="label" class="label-text">{{ label }}</label>
    <input :value="modelValue" @input="emit('update:modelValue', $event.target.value)" v-bind="{ ...$attrs, ...classes }"/>
</template>
<script setup>
import { computed } from 'vue';

const props = defineProps({
    label: {
        type: [String, Boolean],
    },
    class: {
        type: [String, Boolean],
    },
    modelValue: {
        type: String,
        default: '',
    }
})

const classes = computed(() => {
    if (props.class) {
        return { class: props.class };
    }
    else {
        return { class: 'input input-bordered text-xl' };
    }
})

const emit = defineEmits(['update:modelValue']);
</script>
