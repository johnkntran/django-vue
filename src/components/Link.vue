<template>
  <div class="links">
    <h2>Add Stock to Portfolio?</h2>
    <form>
      <select name="select-stock" id="select-stock" v-model="payload.stock_id">
        <option disabled :value="0">Select Stock</option>
        <option v-for="stock in props.stocks" :key="stock.id" :value="stock.id">
          {{ stock.exchange }}:{{ stock.symbol }} {{ stock.name }}
        </option>
      </select>
      <select name="select-portfolio" id="select-portfolio" v-model="payload.portfolio_id">
        <option disabled :value="0">Select Portfolio</option>
        <option v-for="portfolio in props.portfolios" :key="portfolio.id" :value="portfolio.id">
          {{ portfolio.name }}
        </option>
      </select>
      <input type="submit" value="Submit" @click.prevent="linkStockToPortfolio()">
    </form>
    <div class="success" v-show="succeeded">
      <strong>Link Successful!</strong>
    </div>
  </div>
</template>


<script setup>
  import { ref, reactive, defineProps, defineEmits } from 'vue';
  import api from '../api.js';

  const props = defineProps({
    stocks: {
      type: Array,
      required: true,
    },
    portfolios: {
      type: Array,
      required: true,
    },
  });

  const payload = reactive({
    stock_id: 0,
    portfolio_id: 0,
  });
  const succeeded = ref(false);

  const emit = defineEmits(['linked']);

  async function linkStockToPortfolio() {
    await api.post('/api/link/', payload);
    succeeded.value = true;
    setTimeout(() => { succeeded.value = false; }, 5000);
    payload.stock_id = 0;
    payload.portfolio_id = 0;
    emit('linked');
  }
</script>


<style lang="scss" scoped>
  label {
    display: block;
  }
  span {
    display: block;
  }
  .success {
    background-color: palegoldenrod;
    color: darkseagreen
  }
</style>
