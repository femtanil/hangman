<template>
    <menu class="">
        <div class="grid grid-flow-row">
            <li class="flex justify-center">
                <AppButton @click="gameStore.setPlayChoice(true)">{{ 'Play' }}</AppButton>
            </li>
            <li class="flex justify-center">
                <AppButton @click="logChoice">{{ logInOut }}</AppButton>
            </li>
            <li class="flex justify-center">
                <AppButton @click="gameStore.setSettingsChoice(true)">{{ 'Settings' }}</AppButton>
            </li>
        </div>
    </menu>
</template>

<script setup>
import AppButton from '@/components/AppButton.vue';
import { useGameStore } from '@/stores/game.js';
import { useAuthenticationStore } from '@/stores/authentication.js';
import { computed } from 'vue';

const gameStore = useGameStore();
const authStore = useAuthenticationStore();

const logInOut = computed(() => {
    if (authStore.tokenData === null) {
        return 'Connect';
    }
    else {
        return 'Disconnect';
    }
});

const logChoice = function () {
    if (authStore.tokenData === null) {
        gameStore.setLoginChoice(true);
    }
    else {
        authStore.logoutUser();
    }
};
</script>
