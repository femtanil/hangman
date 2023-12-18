<template>
    <menu class="absolute left-1/2 -translate-x-1/2 top-2/3 -translate-2/3">
        <div class="grid grid-flow-row">
            <li><button @click="newGame"
                    class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full">New
                    game</button>
            </li>
            <li><button @click="loadGame"
                    class="btn btn-ghost rounded-none text-3xl xs:text-4xl active:bg-transparent w-full">Load
                    game</button>
            </li>
        </div>
    </menu>
</template>
<script setup>
const emit = defineEmits(['newGame', 'loadGame'])
const newGame = () => emit('newGame', true)
const loadGame = () => emit('loadGame', true)
//import { useGameStore } from '@/stores/game.js'
</script>
