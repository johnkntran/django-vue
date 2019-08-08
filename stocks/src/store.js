import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';


axios.defaults.headers.common['X-CSRFToken'] = window.csrftoken;
Vue.use(Vuex);


export default new Vuex.Store({
  state: {
    globals: {},
    portfolios: [],
    stocks: [],
  },
  mutations: {
    storeContext(state) {
      state.globals = window.globals;
      delete window.globals;
    },
    storePortfolios(state, payload) {
      state.portfolios = payload;
    },
    storeStocks(state, payload) {
      state.stocks = payload;
    },
  },
  actions: {
    async addStock(context, params) {
      const { portfolio } = params;
      const { data } = await axios.post('/stocks/add_stock_to_portfolio/', params);
      const vmPortfolio = context.state.portfolios.find(p => p.slug === portfolio);
      vmPortfolio.stocks.push(data);
    },
    async removeStock(context, params) {
      const { portfolio, stock } = params;
      await axios.post('/stocks/remove_stock_from_portfolio/', params);
      const vmPortfolio = context.state.portfolios.find(p => p.slug === portfolio);
      const vmStockIndex = vmPortfolio.stocks.map(s => s.symbol).indexOf(stock);
      vmPortfolio.stocks.splice(vmStockIndex, 1);
    },
  },
  getters: {
    csrfToken(state) {
      return window.csrftoken;
    },
  },
});
