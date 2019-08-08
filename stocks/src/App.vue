<template>
<main class="container-fluid">
  <h1>TMF Portfolio Management Tool</h1>
  <h2 class="subtitle text-success">(Vue.js Single-File Components and NPM)</h2>
  <stock-table v-for="portfolio in $store.state.portfolios"
               :key="portfolio.slug"
               :portfolio="portfolio"
               @removed-stock="$store.dispatch('removeStock', $event)"
  />
  <add-stock-form :portfolios="$store.state.portfolios"
                  :stocks="$store.state.stocks"
                  @added-stock="$store.dispatch('addStock', $event)"
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
  created() {
    this.$store.commit('storeContext');
  },
  async mounted() {
    const { data } = await axios.get('/stocks/');
    this.$store.commit('storeStocks', data);
    const response = await axios.get('/stocks/portfolios/');
    this.$store.commit('storePortfolios', response.data);
  },
};
</script>

<style lang="scss" scoped>
.subtitle {
  margin-bottom: 3rem;
}
</style>
