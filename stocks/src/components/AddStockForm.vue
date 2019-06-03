<template>
  <div class="row add-form">
    <div class="col-sm">
      <h6 class="float-right" style="margin-top: 10px;">Add a Stock:</h6>
    </div>
    <select name="choose-portfolio" class="custom-select col-sm" v-model="selectedPortfolio">
      <option value="" disabled selected>Choose a portfolio</option>
      <option v-for="portfolio in portfolios" :key="portfolio.slug" :value="portfolio.slug">
        {{ portfolio.name }} ({{ portfolio.slug }})
      </option>
    </select>
    <select name="choose-stock" class="custom-select col-sm" v-model="selectedStock">
      <option value="" disabled selected>Choose a stock</option>
      <option v-for="stock in stocks" :key="stock.symbol" :value="stock.symbol">
        {{ stock.name }} ({{ stock.symbol }})
      </option>
    </select>
    <div class="col-sm">
      <input type="submit"
             class="btn btn-outline-info"
             value="Add"
             @click="saveStockToPortfolio"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddStockForm',
  props: {
    portfolios: {
      type: Array,
      required: true,
    },
    stocks: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      selectedPortfolio: '',
      selectedStock: '',
    };
  },
  methods: {
    saveStockToPortfolio() {
      this.$emit('added-stock', this.selectedPortfolio, this.selectedStock);
      this.selectedPortfolio = '';
      this.selectedStock = '';
    },
  },
}
</script>

<style lang="scss" scoped>
.add-form {
  margin: 0px;
  padding: 1rem;
  border: 1px solid black;
  background-color: whitesmoke;
}
</style>
