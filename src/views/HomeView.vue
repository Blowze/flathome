<template>
  <div class="app-loader">
      првиет {{ userName }}
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
  computed: {
    // геттер вычисляемого значения
    userName: function () {
      // `this` указывает на экземпляр vm
      return  window.Telegram.WebApp.expand();
    }
  },
  mounted() {
    window.Telegram.WebApp.MainButton.setParams({
      text: 'Давайте начнем',
      is_active:true,
      is_visible: true
    })
  }
}
</script>
<style lang="scss" scoped>

.home {
  padding: 0 16px;
}

</style>