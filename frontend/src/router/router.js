import Main from "@/pages/Main"
import { createRouter, createWebHistory } from "vue-router"
import ForVk from "@/pages/ForVk"
import ForTelegram from "@/pages/ForTelegram"

const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/for-vk',
        component: ForVk
    },
    {
        path: '/for-tg',
        component: ForTelegram
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;