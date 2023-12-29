<template>
    <AppButton @click="gameStore.resetChoices()">{{ 'Select Screen' }}</AppButton>
</template>
<script setup>
import AppButton from '@/components/AppButton.vue';
import { useGameStore } from '@/stores/game.js';
const gameStore = useGameStore();
</script>

