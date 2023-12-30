import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'

import GameMenuView from '@/views/GameMenuView.vue'

const pinia = createPinia()
const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '', component: GameMenuView },
    ]
})

createApp(App).use(router).use(pinia).mount('#app')
