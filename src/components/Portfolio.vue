<template>
  <main>
    <h2>Create a Portfolio?</h2>
    <form>
      <label for="portfolio-name">Name</label>
      <input type="text" name="portfolio-name" id="portfolio-name" placeholder="e.g. Rule Breakers" v-model="portfolio.name">
      <input type="submit" value="Submit" @click.prevent="makePortfolio()">
    </form>
    <h2>Portfolios</h2>
    <table>
      <thead>
        <th>ID</th>
        <th>Name</th>
        <th>Constituents</th>
      </thead>
      <tbody>
        <tr v-for="portfolio in props.portfolios" :key="portfolio.id">
          <td>#{{ portfolio.id }}</td>
          <td>{{ portfolio.name }}</td>
          <td>
            <ul>
              <li v-for="stock in portfolio.stocks" :key="stock.id">
                {{ stock.exchange }}:{{ stock.symbol }} {{ stock.name }}
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>


<script setup>
  import { reactive, defineProps, defineEmits } from 'vue';
  import api from '../api.js';

  const portfolio = reactive({ name: '' });

  const props = defineProps({
    portfolios: {
      type: Array,
      required: true,
    },
  });

  const emit = defineEmits(['made']);

  async function makePortfolio() {
    const data = await api.createPortfolio(portfolio);
    portfolio.name = '';
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
