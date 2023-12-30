<template>
    <div id="page" class="h-screen">
        <Menu />
        <main class="">
            <div class="flex flex-row flex-nowrap">
                <div class="box-border w-full flex-none">
                    <img :src="background" alt="Montreuil, Japan" class="object-cover h-screen w-screen">
                </div>
                <div class="box-border w-full flex-none ml-[-100%]">
                    <router-view></router-view>
                </div>
            </div>
        </main>
        <Footer />
    </div>
</template>

<script setup>
import Menu from '@/components/MenuBar.vue'
import Footer from '@/components/Footer.vue'
import background from '@/assets/background.jpg';
</script>
