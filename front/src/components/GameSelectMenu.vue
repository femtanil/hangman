<template>
    <menu class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <div class="grid grid-flow-row">
            <li>
                <AppButton @click="gameStore.setPlayChoice(true)">{{ 'Play' }}</AppButton>
            </li>
            <li>
                <AppButton @click="gameStore.setLoginChoice(true)">{{ 'Login' }}</AppButton>
            </li>
            <li>
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
