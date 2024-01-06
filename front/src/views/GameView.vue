<template>
    <div class="flex flex-col justify-between h-full max-w-full lg:grid lg:grid-cols-12">
        <ProfileInformation v-if="visibleComponent == SelectScreen" />
        <component :is="visibleComponent" v-bind="currentProperties" />
        <MiscInformation v-if="visibleComponent == SelectScreen" />
    </div>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { useGameLogicStore } from '@/stores/gameLogic.js';
import { useAuthenticationStore } from '@/stores/authentication.js'
import { computed } from 'vue';
import SelectScreen from '@/views/GameSelectScreenView.vue';
import MainView from '@/views/GameMainView.vue';
import ProfileInformation from '@/components/GameProfileInformation.vue';
import MiscInformation from '@/components/GameMiscInformation.vue';

const gameStore = useGameStore();
const gameLogicStore = useGameLogicStore();
const authStore = useAuthenticationStore();

const currentProperties = computed(() => {
    if (gameStore.playChoice) {
        return {
            class: `lg:col-start-4 lg:col-end-10 flex flex-grow`
        };
    }
    else if (authStore.tokenData !== null && gameStore.player !== null) {
        return {
            class: `lg:col-start-4 lg:col-end-10 flex flex-grow`
        };
    }
    else {
        return {
        };
    }
});

const visibleComponent = computed(() => {
    if (gameStore.playChoice) {
        gameLogicStore.startGame();
        return MainView;
    }
    else if (gameStore.loginChoice) {
        return SelectScreen;
    }
    else {
        return SelectScreen;
    }

});

</script>
