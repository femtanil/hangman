import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'

import TitleScreen from '@/components/title_screen/TitleScreen.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '', component: TitleScreen },
    ]
})

createApp(App).use(router).mount('#app')
