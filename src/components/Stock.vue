<template>
  <main>
    <h2>Create a Stock?</h2>
    <form>
      <label for="stock-exchange">Exchange</label>
      <input type="text" name="stock-exchange" id="stock-exchange" placeholder="e.g. NASDAQ" v-model="stock.exchange">
      <label for="stock-symbol">Symbol</label>
      <input type="text" name="stock-symbol" id="stock-symbol" placeholder="e.g. AAPL" v-model="stock.symbol">
      <label for="stock-name">Name</label>
      <input type="text" name="stock-name" id="stock-name" placeholder="e.g. Apple" v-model="stock.name">
      <input type="submit" value="Submit" @click.prevent="makeStock()">
    </form>
    <h2>Stocks</h2>
    <table>
      <thead>
        <th>ID</th>
        <th>Ticker</th>
        <th>Name</th>
      </thead>
      <tbody>
        <tr v-for="stock in props.stocks" :key="stock.id">
          <td>#{{ stock.id }}</td>
          <td>{{ stock.exchange }}:{{ stock.symbol }}</td>
          <td>{{ stock.name }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>


<script setup>
  import { reactive, defineProps, defineEmits } from 'vue';
  import api from '../api.js';

  const props = defineProps({
    stocks: {
      type: Array,
      required: true,
    },
  });

  const emit = defineEmits(['made']);

  const stock = reactive({
    exchange: '',
    symbol: '',
    name: '',
  });

  async function makeStock() {
    const data = await api.createStock(stock);
    stock.exchange = '';
    stock.symbol = '';
    stock.name = '';
    emit('made', data);
  }
</script>


<style lang="scss" scoped>
  label {
    display: block;
  }
  table {
    border-style: solid;
  }
  th,td {
    border-style: solid;
    border-width: 1px;
  }
</style>
