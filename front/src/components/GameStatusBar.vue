<template>
    <div ref="statusBar" class="stats shadow flex rounded-none">
        <div class="stat">
            <div class="stat-title text-sm">Guessed words</div>
            <div class="stat-value text-secondary text-base">1</div>
        </div>
        <div class="stat">
            <div class="stat-title text-sm">Word to guess</div>
            <div class="stat-value text-primary text-base">someword</div>
        </div>
        <div class="stat">
            <div class="stat-title text-sm">Highscore</div>
            <div class="stat-value text-base">1337</div>
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted, onUpdated } from 'vue';
import { useElementPropertiesStore } from '@/stores/elementProperties.js';

const elementPropertiesStore = useElementPropertiesStore();
const statusBar = ref(null);

const storeStatusBarHeight = () => {
    const height = parseFloat(window.getComputedStyle(statusBar.value).height);
    elementPropertiesStore.statusbarHeight = height;
}

onMounted(() => {
    storeStatusBarHeight();
});

onUpdated(() => {
    storeStatusBarHeight();
});
</script>
