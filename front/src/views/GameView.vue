<template>
    <!--
    <div :style="`background-image:url(${background});`" class="h-screen w-screen"></div>
    -->
    <div class="relative">
        <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
        <h1 class="absolute left-1/2 -translate-x-1/2 top-1/4 -translate-y-1/4 text-7xl sm:text-9xl">hangman</h1>
    </div>
    <!--
    <SelectMenu v-if="showSelectMenu"></SelectMenu>
    <PlayerForm v-if="!showSelectMenu" :confirmPassword=gameStore.newGame v-slot:formTitle>
        {{ playerFormTitle }}
    </PlayerForm>
    -->
    <component :is="visibleComponent" v-bind="currentProps">{{ currentSlot }}</component>
</template>

<script setup>
import { useGameStore } from '@/stores/game.js';
import { ref, computed } from 'vue';
import background from '@/assets/background.jpg';
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
