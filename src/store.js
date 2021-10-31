import { createStore } from "vuex";
import api from './api.js';

const store = createStore({
  state() {
    return {
      count: 0,
    };
  },
  mutations: {
    addCount(state, n) {
      state.count += n;
    },
  },
  actions: {
    async fetchDataThenAddCount({ commit }) {
      const stock = await api.getStock(1);
      commit('addCount', stock.id ? stock.id : 0);
    }
  },
  getters: {
    getCount(state) {
      return state.count;
    },
  },
});

export default store;
