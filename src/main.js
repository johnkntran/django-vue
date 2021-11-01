import { createApp } from 'vue';
import router from './router.js';
import { store } from './store.js';

import App from './App.vue';


const vm = createApp(App);
const routed = vm.use(router);
const stored = vm.use(store);


export default { vm, routed, stored };
