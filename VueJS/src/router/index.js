import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'auth',
      component: () => import('../views/AuthView.vue'),
    },
    {
      path: '/reg',
      name: 'reg',
      component: () => import('../views/RegView'),
    },
    {
      path: '/complaints',
      name: 'complaints',
      component: () => import('../views/ComplaintsView'),
    },
    {
      path: '/complaint',
      name: 'complaint',
      component: () => import('../views/ComplaintView'),
    },
    {
      path: '/transactions',
      name: 'transactions',
      component: () => import('../views/TransactionsView.vue'),
    },
    {
      path: '/transaction',
      name: 'transaction',
      component: () => import('../views/TransactionView.vue'),
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
    },
  ],
})

export default router
