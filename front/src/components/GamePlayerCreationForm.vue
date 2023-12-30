<template>
    <div class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            Choose your player name
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="grid grid-flow-row">
                <label for="playername" class="text-3xl xs:text-4xl">Player name</label>
                <input type="text" id="playername" name="username" v-model="playername" class="text-3xl xs:text-4xl" />
            </div>
        </form>
    </div>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { ref } from 'vue';

const gameStore = useGameStore();
const playername = ref('');

async function submitForm() {
    gameStore.createPlayer(playername.value);
}
</script>
