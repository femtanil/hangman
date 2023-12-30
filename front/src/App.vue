<template>
    <div id="page" class="h-screen">
        <Menu />
        <main>
            <div class="relative">
                <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
            </div>
            <router-view></router-view>
        </main>
        <Footer />
    </div>
</template>

<script setup>
import Menu from '@/components/MenuBar.vue'
import Footer from '@/components/Footer.vue'
import background from '@/assets/background.jpg';
</script>
