<template>
    <menu class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <div class="grid grid-flow-row">
            <li><button @click="gameStore.setNewGame(true);"
                    class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full">New
                    game</button>
            </li>
            <li><button @click="gameStore.setLoadGame(true);"
                    class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full">Load
                    game</button>
            </li>
        </div>
    </menu>
</template>

<script setup>
import { useGameStore } from '@/stores/game.js';

const gameStore = useGameStore();
</script>
