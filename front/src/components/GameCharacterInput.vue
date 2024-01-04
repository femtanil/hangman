<template>
    <form @submit.prevent="submitForm" method="post">
        <div class="flex flex-col px-5">
            <AppInput v-model="character" type="text" class="input input-bordered text-xl" placeholder="Type a letter" />
            <AppInput type="submit" value="Submit" class="btn btn-ghost rounded-none text-3xl active:bg-transparent" />
        </div>
    </form>
</template>
<script setup>
import { useGameLogicStore } from '@/stores/gameLogic.js';
import { useGameStore } from '@/stores/game.js';
import { ref } from 'vue';
import AppInput from '@/components/AppInput.vue';

const character = ref('')

const submitForm = function () {
}
</script>
