<template>
    <!--
    <div :style="`background-image:url(${background});`" class="h-screen w-screen"></div>
    -->
    <div class="relative">
        <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
        <h1 class="absolute left-1/2 -translate-x-1/2 top-1/4 -translate-y-1/4 text-7xl sm:text-9xl">hangman</h1>
    </div>
    <SelectMenu v-if="showSelectMenu"></SelectMenu>
    <PlayerForm v-if="!showSelectMenu" v-slot:formTitle>{{ gameFormTitle }}</PlayerForm>
</template>

<script setup>
import { useGameStore } from '@/stores/game.js';
import { computed } from 'vue';
import background from '@/assets/background.jpg';
import SelectMenu from '@/components/GameSelectMenu.vue';
import PlayerForm from '@/components/GamePlayerForm.vue';

const gameStore = useGameStore();

const showSelectMenu = computed(() => {
    if (gameStore.newGame == true || gameStore.loadGame == true) {
        return false;
    }
    else {
        return true;
    }
})

const gameFormTitle = computed(() => {
    if (gameStore.newGame == true) {
        return 'Create player';
    }
    else if (gameStore.loadGame == true) {
        return 'Load player';
    }
})
</script>
