<template>
    <menu class="">
        <div class="grid grid-flow-row">
            <li class="flex justify-center">
                <AppButton @click="gameStore.setPlayChoice(true)">{{ 'Play' }}</AppButton>
            </li>
            <li class="flex justify-center">
                <AppButton @click="gameStore.setLoginChoice(true)">{{ 'Login' }}</AppButton>
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

const gameStore = useGameStore();
</script>
