import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const ax = axios.create({
  headers: { 'X-CSRFToken': window.csrftoken },
});


export default new Vuex.Store({
  state: {
    globals: {},
  },
  mutations: {
    storeContext(state) {
      state.globals = window.globals;
      delete window.globals;
    },
  },
  actions: {
    // Asyc methods go here
  },
  getters: {
    csrfToken(state) {
      return window.csrftoken;
    },
  },
});
