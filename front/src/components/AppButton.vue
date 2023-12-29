<template>
    <button class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full" @click="handleClick">
        <slot></slot>
    </button>
</template>
<script setup>
const emit = defineEmits(['click']);

function handleClick() {
    emit('click')
}
</script>
