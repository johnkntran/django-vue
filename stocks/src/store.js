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
    /**
     * Add a stock to the database. Then push the stock information returned from the server to the
     * list of stocks in that portfolio within the app.
     *
     * @param {Object} context The context object exposing methods/properties on the Vuex store.
     * @param {Object} params The payload object containing parameters dispatched with the action.
     */
    async addStock(context, { portfolio, stock }) {
      const { data } = await axios.post('/stocks/add_stock_to_portfolio/', { portfolio, stock });
      const vmPortfolio = context.state.portfolios.find(p => p.slug === portfolio);
      vmPortfolio.stocks.push(data);
    },
    /**
     * Remove a stock from the database. Then pop that stock out of the list of stocks in that
     * portfolio within the app.
     *
     * @param {Object} context The context object exposing methods/properties on the Vuex store.
     * @param {Object} params The payload object containing parameters dispatched with the action.
     */
    async removeStock(context, { portfolio, stock }) {
      const { data } = await axios.post('/stocks/remove_stock_from_portfolio/', { portfolio, stock });
      const vmPortfolio = context.state.portfolios.find(p => p.slug === portfolio);
      const vmStockIndex = vmPortfolio.stocks.map(s => s.symbol).indexOf(stock);
      vmPortfolio.stocks.splice(vmStockIndex, 1);
    },
  },
  getters: {
    csrfToken(state, getters) {
      return window.csrftoken;
    },
  },
});
