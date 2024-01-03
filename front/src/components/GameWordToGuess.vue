<template>
    <div class="flex justify-center text-white text-3xl">
        st_llm_n
    </div>
</template>
<script setup>
import { useGameLogicStore } from '@/stores/gameLogic.js';
import { ref } from 'vue';

const gameLogicStore = useGameLogicStore();
</script>
