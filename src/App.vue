<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <div>
    <router-link to="/">Go to Brokerage</router-link> |
    <router-link to="/about">Go to About</router-link>
  </div>
  <router-view></router-view>
</template>


<script setup>
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  // for more details.
  import { onMounted } from 'vue';
  import { useStore } from 'vuex';

  const store = useStore();

  onMounted(async function appMounted() {
    store.commit('addCount', 1);
    console.debug('store.state.count', store.state.count);
    await store.dispatch('fetchDataThenAddCount');
    console.debug('store.getters.getCount', store.getters.getCount);
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
