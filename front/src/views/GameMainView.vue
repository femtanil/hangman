<template>
    <div class="grid grid-rows-6">
        <div class="row-span-1">
            <StatusBar class="" />
        </div>
        <div class="row-start-4 row-end-5">
            <WordToGuess />
        </div>
        <div class="row-start-6 row-end-7">
            <div class="flex justify-center">
                <SelectScreenButton class="" />
            </div>
            <div class="flex justify-center">
                <AppButton @click="quitGame">{{ 'Quit game' }}</AppButton>
            </div>
        </div>
    </div>
</template>
<script setup>
import StatusBar from '@/components/GameStatusBar.vue';
import WordToGuess from '@/components/GameWordToGuess.vue';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';
import AppButton from '@/components/AppButton.vue';

import { useGameStore } from '@/stores/game.js';
import { useGameLogicStore } from '@/stores/gameLogic.js';

const gameStore = useGameStore();
const gameLogicStore = useGameLogicStore();

const quitGame = function () {
    gameLogicStore.endGame();
    gameStore.resetChoices();
};
</script>
