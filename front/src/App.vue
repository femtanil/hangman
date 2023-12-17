<template>
    <div id="page" class="h-screen">
        <Menu />
        <main>
            <router-view></router-view>
        </main>
        <Footer />
    </div>
</template>

<script setup>
import Menu from '@/components/MenuBar.vue'
import Footer from '@/components/Footer.vue'
</script>
