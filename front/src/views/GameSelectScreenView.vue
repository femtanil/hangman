<template>
    <!--
    <div :style="`background-image:url(${background});`" class="h-screen w-screen"></div>
    -->
    <div class="grid grid-rows-4 h-full">
        <div class="row-span-1 row-end-3 text-7xl sm:text-9xl">
            <h1 class="flex justify-center">hangman</h1>
        </div>
        <component class="row-start-3 row-end-4" :is="visibleComponent" v-bind="currentProps">{{ currentSlot }}</component>
    </div>
    <!--
    <SelectMenu v-if="showSelectMenu"></SelectMenu>
    <PlayerForm v-if="!showSelectMenu" :confirmPassword=gameStore.newGame v-slot:formTitle>
        {{ playerFormTitle }}
    </PlayerForm>
    -->
</template>

<script setup>
import { useGameStore } from '@/stores/game.js';
import { ref, computed } from 'vue';
import SelectMenu from '@/components/GameSelectMenu.vue';
import AuthForm from '@/components/GameAuthenticationForm.vue';

const gameStore = useGameStore();
const currentSlot = ref('');
const currentProps = ref({});

const visibleComponent = computed(() => {
    if (gameStore.loginChoice) {
        currentSlot.value = 'Login';
        currentProps.value = { confirmPassword: false };
        return AuthForm;
    }
    else {
        return SelectMenu;
    }
})
</script>
