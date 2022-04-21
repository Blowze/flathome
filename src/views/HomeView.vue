<template>
  <div class="app-loader">

  </div>
  <div class="home">
  <div class="home__button" @click="getWindowWidth">sdf</div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',

   methods: {
    getWindowWidth() {
        return window.Telegram.WebApp.expand();
      },
  },
}
</script>
<style lang="scss" scoped>
div {
  height: 150px;
  width: 150px;
  margin-bottom: 20px;
  background: #ccc;
}

.home {
  padding: 0 16px;
}

</style>