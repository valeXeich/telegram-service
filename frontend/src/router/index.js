import { createRouter, createWebHistory } from 'vue-router';
import Main from '@/components/Main.vue';
import Login from '@/components/Login.vue';
import Cabinet from '@/components/Cabinet.vue';

const routes = [
  {
    path: '/',
    component: Main
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/cabinet',
    component: Cabinet
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
