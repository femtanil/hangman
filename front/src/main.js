import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'

import HomeView from '@/views/HomeView.vue'

const pinia = createPinia()
const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '', component: HomeView },
    ]
})

createApp(App).use(router).use(pinia).mount('#app')
