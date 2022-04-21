<template>
  <div class="home">

    <div class="container">
      <div class="form">
       
        <div class="form__body">
            <v-select class="input" :options="options"   :dropdown-should-open="dropdownShouldOpen"
                             placeholder="Поиск ">
                                </v-select>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


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
<style lang="scss">

.container {
  padding: 24px 16px 16px;
  padding-top: 0;
  width: 100%;
}
.home {
  height: 100%;
}

.v-select {
  position: relative;

}
$base-color: var(--tg-theme-bg-color);
.vs__search {
  padding: 0 16px;
  height: 42px;
  width: 100%;
  border-radius: 4px;
  border: 1px solid #c9c9c9;
  outline: none;
}
.vs__search:focus {
    z-index: 1000;
    position: relative;
}
.vs__actions {
  position: absolute;
      top: 0;
    right: 0;
    width: 42px;
    height: 42px;
  svg {
    fill: #3c3c3c80;
  }
}
.vs__clear {
      width: 100%;
    height: 100%;
    background: none;
    border: none;
    display: block !important;
    cursor: pointer;
}

.vs__dropdown-menu {
  position: relative;
    margin: 0;
    padding: 0;
    list-style: none;
    margin: 0 -16px;
    height: calc(100vh - 58px);
    overflow: auto;
}
.vs__dropdown-toggle {
  padding-bottom: 16px;
    background: var(--tg-theme-bg-color);
    
}

.vs__dropdown-option {
    display: block;
    padding: 14px 16px;
    color: var(--tg-theme-text-color);
    text-decoration: none;
    cursor: pointer;
}
.vs__dropdown-option:active,
.vs__dropdown-option:hover {
  background: var(--tg-theme-hint-color);
}
.vs__dropdown-option--selected {
  background: var(--tg-theme-hint-color);
}
.vs__selected {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 16px;
  color: #152242;
}

.vs__open-indicator {
  display: none;
}
.vs__no-options {
  padding: 8px 16px;
  font-size: 0;
}
.vs__no-options::after {
    content: "Ничего не найдено";
    font-size: 16px;
    text-align: center;
    width: 100%;
    display: block;
    color: #a1a7b3;
    font-size: 14px;
}

.vs__selected-options {
  position: relative;
}

</style>