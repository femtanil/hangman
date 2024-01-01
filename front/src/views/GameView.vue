<template>
    <div class="flex flex-col justify-between h-full max-w-full lg:grid lg:grid-cols-12">
        <div class="collapse collapse-arrow bg-base-100 rounded-none lg:col-start-1 lg:col-end-4">
            <input type="checkbox" />
            <div class="collapse-title text-xl">
                first section title
            </div>
            <div class="collapse-content bg-base-200">
                first section content
            </div>
        </div>
        <component :is="visibleComponent" v-bind="currentProps" />
        <div class="collapse collapse-arrow bg-base-100 rounded-none lg:col-start-10 lg:col-end-13">
            <input type="checkbox" />
            <div class="collapse-title text-xl">
                third section title
            </div>
            <div class="collapse-content bg-base-200">
                third section content
            </div>
        </div>
    </div>
</template>
<script setup>
import { useGameStore } from '@/stores/game.js';
import { useAuthenticationStore } from '@/stores/authentication.js'
import { useElementPropertiesStore } from '@/stores/elementProperties.js';
import { ref, computed } from 'vue';
import SelectScreen from '@/views/GameSelectScreenView.vue';
import MainView from '@/views/GameMainView.vue';

const gameStore = useGameStore();
const authStore = useAuthenticationStore();
const elementPropertiesStore = useElementPropertiesStore();
const currentProps = computed(() => {
    if (gameStore.playChoice) {
        return {
            //class: `lg:col-start-4 lg:col-end-10 h-[calc(100vh-${elementPropertiesStore.statusbarHeight}px)]`
            is: MainView,
            class: `lg:col-start-4 lg:col-end-10`
        };
    }
    else if (authStore.tokenData !== null && gameStore.player !== null) {
        return {
            is: MainView,
            class: `lg:col-start-4 lg:col-end-10`
        };
    }
    else {
        return {
            is: SelectScreen,
            class: 'lg:col-start-4 lg:col-end-10'
        };
    }
});

const visibleComponent = computed(() => {
    if (gameStore.playChoice) {
        currentProps.value = {
            //class: `lg:col-start-4 lg:col-end-10 h-[calc(100vh-${elementPropertiesStore.statusbarHeight}px)]`
            class: `lg:col-start-4 lg:col-end-10`
        };
        console.log(elementPropertiesStore.statusbarHeight);
        return MainView;
    }
    else if (authStore.tokenData !== null && gameStore.player !== null) {
        currentProps.value = {
            class: `lg:col-start-4 lg:col-end-10`
        };
        return MainView;
    }
    else {
        return SelectScreen;
    }

})

</script>
