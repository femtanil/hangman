<template>
    <form @submit.prevent="submitForm" method="post">
        <div class="flex flex-col px-5">
            <label for="character" class="text-xl" />
            <input type="text" id="character" name="character" v-model="character" class="input input-bordered text-xl"
                placeholder="Type a letter" />
            <input type="submit" value="Submit" class="btn btn-ghost rounded-none text-3xl active:bg-transparent" />
        </div>
    </form>
</template>
<script setup>
import { useGameLogicStore } from '@/stores/gameLogic.js';
import { useGameStore } from '@/stores/game.js';
import { ref } from 'vue';

const character = ref('')

const submitForm = function () {
}
</script>
