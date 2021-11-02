<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <div>
    <router-link to="/">Go to Brokerage</router-link> |
    <router-link to="/about">Go to About</router-link>
  </div>
  <router-view></router-view>
</template>


<script setup>
  import { onMounted } from 'vue';
  import { useStore } from './store.js';

  const store = useStore();

  onMounted(async function appMounted() {
    store.count += 1;
    console.debug('store.count', store.count);
    await store.fetchDataThenIncrement();
    console.debug('store.getCount', store.getCount);
  });

</script>


<style lang="scss">
  /* Global Styles */
  #app {
    font-family: Avenir, Segoe UI, Helvetica, sans-serif;
    text-align: center;
    color: #2c3e50;
  }
  h1 {
    color: #42b983;
  }
  h2 {
    color: #39596C;
  }
</style>
