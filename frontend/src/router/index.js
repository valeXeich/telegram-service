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
    component: Login,
    beforeEnter: (to, from, next) => {
      if(store.state.auth === true) {
          next('/cabinet');
      } else {
          next();
      }
  }
  },
  {
    path: '/cabinet',
    component: Cabinet,
    beforeEnter: (to, from, next) => {
      if(store.state.auth === true) {
          next();
      } else {
          next('/login');
      }
  }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
