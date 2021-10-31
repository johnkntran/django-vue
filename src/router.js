import { createRouter, createWebHashHistory } from 'vue-router';

import Brokerage from './pages/Brokerage.vue';
import About from './pages/About.vue';


const routes = [
  { path: '/', component: Brokerage },
  { path: '/about', component: About },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
