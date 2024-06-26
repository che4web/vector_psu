import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Fist from '../views/Fist.vue'
import ProffView from '../views/ProffView.vue'
import ProgramDetail from '../views/ProgramDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Fist
    },
    {
      path: '/proff',
      name: 'proff',
      component: ProffView
    },
    {
      path: '/program/:id/',
      name: 'program-detail',
      component: ProgramDetail
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
