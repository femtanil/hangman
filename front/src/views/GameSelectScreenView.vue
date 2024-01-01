<template>
    <div class="flex flex-col">
        <h1 class="flex justify-center text-7xl pb-8">hangman</h1>
        <component class="" :is="visibleComponent" v-bind="currentProps">{{ currentSlot }}</component>
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
import { useAuthenticationStore } from '@/stores/authentication.js'
import { ref, computed } from 'vue';
import SelectMenu from '@/components/GameSelectMenu.vue';
import AuthForm from '@/components/GameAuthenticationForm.vue';
import PlayerCreation from '@/components/GamePlayerCreationForm.vue';

const gameStore = useGameStore();
const authStore = useAuthenticationStore();
const currentSlot = ref('');
const currentProps = ref({});

const visibleComponent = computed(() => {
    // User chose to log in but isn't authenticated.
    if (gameStore.loginChoice && authStore.tokenData === null) {
        currentSlot.value = 'Login';
        currentProps.value = { confirmPassword: false };
        return AuthForm;
    }
    // User chose to log in and is authenticated.
    else if (gameStore.loginChoice && authStore.tokenData !== null) {
        try {
            gameStore.getOwnPlayer();
        }
        catch (error) {
            currentSlot.value = '';
            currentProps.value = {};
            return PlayerCreation;
        }
    }
    else {
        return SelectMenu;
    }
})

</script>
