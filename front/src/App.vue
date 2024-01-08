<template>
    <NavBar />
    <main>
        <div class="flex flex-row flex-nowrap">
            <div class="w-full flex-none">
                <img v-bind="backgroundProperties">
            </div>
            <div class="w-full flex-none ml-[-100%]">
                <router-view></router-view>
            </div>
        </div>
    </main>
    <AppFooter />
</template>

<script setup>
import NavBar from '@/components/AppNavBar.vue'
import AppFooter from '@/components/AppFooter.vue'
import background from '@/assets/background.jpg';
import { computed } from 'vue';
import { useElementPropertiesStore } from '@/stores/elementProperties.js';

const elementPropertiesStore = useElementPropertiesStore();
const backgroundImageClass = computed(() => {
    return `object-cover h-[calc(100vh-${elementPropertiesStore.navbarHeight}px)] w-screen`;
});

const backgroundProperties = computed(() => {
    return {
        src: background,
        alt: 'Montreuil, Japan',
        class: `${backgroundImageClass.value}`
    };
});
</script>
