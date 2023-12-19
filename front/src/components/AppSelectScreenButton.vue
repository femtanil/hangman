<template>
    <button @click="gameStore.resetNewGame()"
        class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full">Select Screen
    </button>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
const gameStore = useGameStore();
</script>

