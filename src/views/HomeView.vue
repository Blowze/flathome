<template>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>

</template>

<script>
export default {
  name: 'HomeView',
   data() {
            return {
                    options: [
      'Москва',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',

      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Нижний Новгород',
      'Казань'
    ]
            }
        },

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

</style>