<template>
    <!--
    <div :style="`background-image:url(${background});`" class="h-screen w-screen"></div>
    -->
    <div class="relative">
        <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
        <h1 class="absolute left-1/2 -translate-x-1/2 top-1/4 -translate-y-1/4 text-7xl sm:text-9xl">hangman</h1>
    </div>
    <SelectMenu v-if="showSelectMenu"></SelectMenu>
    <component :is="gameFormComponent"></component>
</template>

<script setup>
import { useGameStore } from '@/stores/game.js';
import { computed } from 'vue';
import background from '@/assets/background.jpg';
import SelectMenu from '@/components/GameSelectMenu.vue';
import NewGameForm from '@/components/NewGameForm.vue';
import LoadGameForm from '@/components/LoadGameForm.vue';

const gameStore = useGameStore();

const showSelectMenu = computed(() => {
    if (gameStore.newGame == true || gameStore.loadGame == true) {
        return false;
    }
    else {
        return true;
    }
})

const gameFormComponent = computed(() => {
    if (gameStore.newGame == true) {
        return NewGameForm;
    }
    else if (gameStore.loadGame == true) {
        return LoadGameForm;
    }
})
</script>
