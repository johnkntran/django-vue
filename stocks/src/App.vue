<template>
<main class="container-fluid">
  <h1>TMF Portfolio Management Tool</h1>
  <h2 class="subtitle text-success">(Vue.js Single-File Components and NPM)</h2>
  <stock-table v-for="portfolio in portfolios"
               :key="portfolio.slug"
               :portfolio="portfolio"
               @removed-stock="handleRemovedStock"
  />
  <add-stock-form :portfolios="portfolios"
                  :stocks="stocks"
                  @added-stock="handleAddedStock"
  />
</main>
</template>

<script>
import axios from 'axios';
import StockTable from './components/StockTable.vue';
import AddStockForm from './components/AddStockForm.vue';

export default {
  name: 'Main',
  components: { StockTable, AddStockForm },
  data() {
    return {
      portfolios: [],
      stocks: [],
    };
  },
  methods: {
    handleAddedStock(portfolio, stock) {
      axios.post('/stocks/add_stock_to_portfolio/', { portfolio, stock })
      .then((response) => {
        const { data } = response;
        const vmPortfolio = this.portfolios.find(p => p.slug === portfolio);
        vmPortfolio.stocks.push(data);
      });
    },
    handleRemovedStock(portfolio, stock) {
      axios.post('/stocks/remove_stock_from_portfolio/', { portfolio, stock })
      .then((response) => {
        const vmPortfolio = this.portfolios.find(p => p.slug === portfolio);
        const vmStockIndex = vmPortfolio.stocks.map(s => s.symbol).indexOf(stock);
        vmPortfolio.stocks.splice(vmStockIndex, 1);
      });
    },
  },
  created() {
    this.$store.commit('storeContext');
  },
  mounted() {
    axios.get('/stocks/')
    .then((response) => {
      this.stocks = response.data;
    });
    axios.get('/stocks/portfolios/')
    .then((response) => {
      this.portfolios = response.data;
    });
  },
};
</script>

<style lang="scss" scoped>
.subtitle {
  margin-bottom: 3rem;
}
</style>
