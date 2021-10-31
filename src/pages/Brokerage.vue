<template>
  <h1>Brokerage</h1>
  <div class="brokerage">
    <Stock :stocks="stocks" @made="stockCreated" />
    <Portfolio :portfolios="portfolios" @made="portfolioCreated" />
    <Link :stocks="stocks" :portfolios="portfolios" @linked="fetchData()"/>
  </div>
</template>


<script setup>
  import { ref, onMounted } from 'vue';
  import api from '../api.js';
  import Stock from '../components/Stock.vue';
  import Portfolio from '../components/Portfolio.vue';
  import Link from '../components/Link.vue';

  const stocks = ref([]);
  const portfolios = ref([]);

  function stockCreated(payload) {
    stocks.value.push(payload);
  }

  function portfolioCreated(payload) {
    portfolios.value.push(payload);
  }

  async function fetchData() {
    const promises = [
      api.getStocks().then(data => { stocks.value = data; }),
      api.getPortfolios().then(data => { portfolios.value = data; }),
    ];
    await Promise.all(promises);
  }

  onMounted(async () => {
    await fetchData();
  });
</script>


<style lang="scss" scoped>
  .brokerage {
    display: grid;
    grid-template-columns: auto auto auto;
  }
</style>
