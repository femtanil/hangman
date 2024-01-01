<template>
    <div class="flex flex-col justify-between h-full max-w-full lg:grid lg:grid-cols-12">
        <div
            class="collapse collapse-arrow bg-base-100 rounded-none lg:col-start-1 lg:col-end-4 outline outline-yellow-500">
            <input type="checkbox" />
            <div ref="firstSectionTitle" class="collapse-title text-xl text-indigo-500 outline outline-indigo-500">
                first section title
            </div>
            <div class="collapse-content bg-base-200 text-rose-500 outline outline-rose-500">
                first section content
            </div>
        </div>
        <component :is="visibleComponent" v-bind="currentProperties" />
        <div
            class="collapse collapse-arrow bg-base-100 rounded-none lg:col-start-10 lg:col-end-13 outline outline-yellow-500">
            <input type="checkbox" />
            <div class="collapse-title text-xl text-indigo-500 outline outline-indigo-500">
                third section title
            </div>
            <div class="collapse-content bg-base-200 outline text-rose-500 outline-rose-500">
                third section content
            </div>
        </div>
    </div>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { useAuthenticationStore } from '@/stores/authentication.js'
import { computed, ref } from 'vue';
import SelectScreen from '@/views/GameSelectScreenView.vue';
import MainView from '@/views/GameMainView.vue';

const gameStore = useGameStore();
const authStore = useAuthenticationStore();
const firstSectionTitle = ref(null);

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
        return MainView;
    }
    else if (authStore.tokenData !== null && gameStore.player !== null) {
        return MainView;
    }
    else {
        return SelectScreen;
    }

});

</script>
