<template>
    <div class="grid grid-flow-row">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            Choose your player name
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <label for="playername" class="text-3xl xs:text-4xl">Player name</label>
                    <input type="text" id="playername" name="username" v-model="playername" class="text-3xl xs:text-4xl" />
                </div>
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
