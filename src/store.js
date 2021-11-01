import { createPinia, defineStore } from 'pinia';
import api from './api.js';


const store = createPinia();

const useStore = defineStore('app', {
  state() {
    return {
      count: 0,
    };
  },
  getters: {
    getCount(state) {
      return state.count;
    },
  },
  actions: {
    async fetchDataThenIncrement() {
      const stock = await api.getStock(1);
      this.count += stock.id ? stock.id : 0;
    }
  },
});

export { store, useStore };
