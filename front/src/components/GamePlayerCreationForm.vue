<template>
    <div class="grid grid-flow-row">
        <h3 class="flex justify-center text-4xl xs:text-5xl pb-9">
            Choose your player name
        </h3>
        <form @submit.prevent="submitForm" method="post">
            <div class="flex flex-col px-5">
                <AppInput v-model="playername" type="text" class="input input-bordered text-xl" :label="'Playername'" />
            </div>
            <div class="flex justify-center">
                <div class="grid grid-flow-row">
                    <SelectScreenButton />
                </div>
            </div>
        </form>
    </div>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { ref } from 'vue';
import SelectScreenButton from '@/components/AppSelectScreenButton.vue';
import AppInput from '@/components/AppInput.vue';

const gameStore = useGameStore();
const playername = ref('');

async function submitForm() {
    gameStore.createPlayer(playername.value);
}
</script>
