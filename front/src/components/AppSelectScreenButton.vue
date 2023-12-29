<template>
    <AppButton @click="backToSelectScreen">{{ 'Select Screen' }}</AppButton>
</template>
<script setup>
import AppButton from '@/components/AppButton.vue';
import { useGameStore } from '@/stores/game.js';
const gameStore = useGameStore();

const backToSelectScreen = function () {
    if (gameStore.newGame == true) {
        gameStore.resetNewGame();
    }
    else if (gameStore.loadGame == true) {
        gameStore.resetLoadGame();
    }
}
</script>

