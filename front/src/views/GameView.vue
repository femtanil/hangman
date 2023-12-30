<template>
    <component :is="visibleComponent" v-bind="currentProps"></component>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { useAuthenticationStore } from '@/stores/authentication.js';
import { ref, computed } from 'vue';
import SelectScreen from '@/views/GameSelectScreenView.vue';
import MainView from '@/views/GameMainView.vue';

const gameStore = useGameStore();
const authStore = useAuthenticationStore();
const currentProps = ref({});

const visibleComponent = computed(() => {
    if (gameStore.playChoice) {
        return MainView;
    }
    else {
        return SelectScreen;
    }
})
</script>
