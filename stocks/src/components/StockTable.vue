<template>
  <section>
    <h4>{{ portfolio.name }} (@{{ portfolio.slug }})</h4>
    <article class="container">
      <table class="table table-bordered">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Stock</th>
            <th scope="col">Exchange</th>
            <th scope="col">Active</th>
            <th scope="col">Price</th>
            <th scope="col">Controls</th>
          </tr>
        </thead>
          <tbody>
            <tr v-for="stock in portfolio.stocks" :key="`${portfolio.slug}-${stock.symbol}`">
              <td scope="row">{{ stock.name }} ({{ stock.symbol }})</td>
              <td scope="row">{{ stock.exchange }}</td>
              <td scope="row">
                {{ String(stock.active).slice(0, 1).toUpperCase() + String(stock.active).slice(1) }}
              </td>
              <td scope="row">${{ stock.price }}</td>
              <td scope="row">
                <input type="submit"
                       class="btn btn-outline-danger"
                       value="Remove"
                       @click="removeStockFromPortfolio(portfolio.slug, stock.symbol)"
                >
              </td>
            </tr>
          </tbody>
      </table>
    </article>
    <hr>
  </section>
</template>

<script>
export default {
  name: 'StockTable',
  props: {
    portfolio: {
      type: Object,
      required: true,
    },
  },
  methods: {
    removeStockFromPortfolio(portfolio, stock) {
      this.$emit('removed-stock', portfolio, stock);
    },
  },
};
</script>
