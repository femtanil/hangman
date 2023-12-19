<template>
    <!--
    <div :style="`background-image:url(${background});`" class="h-screen w-screen"></div>
    -->
    <div class="relative">
        <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
        <h1 class="absolute left-1/2 -translate-x-1/2 top-1/4 -translate-y-1/4 text-7xl sm:text-9xl">hangman</h1>
    </div>
    <HomeMenu v-if="showMenu"></HomeMenu>
</template>

<script setup>
import background from '@/assets/background.jpg';
import HomeMenu from '@/components/HomeMenu.vue';
import { useGameStore } from '@/stores/game.js';
import { computed } from 'vue';

const gameStore = useGameStore();

const showMenu = computed(() => {
    if (gameStore.newGame == true || gameStore.loadGame == true){
        return false;
    }
    else {
        return true;
    }
})

</script>
