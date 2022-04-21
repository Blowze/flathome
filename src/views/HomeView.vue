<template>
  <div class="app-loader">

  </div>
  <div class="home">
  <div class="home__button" @click="window.Telegram.WebApp.expand()">sdf</div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
   methods: {
    dropdownShouldOpen(VueSelect) {
      console.log()
      return  VueSelect.open = true
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