<template>
  <div class="home">
    <div class="header">
        Введите регион или город
    </div>
    <div class="container">
      <div class="form">
       
        <div class="form__body">
            <v-select class="input" :options="options"
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
      'Казань'
    ]
            }
        },
  components: {
  }
}
</script>
<style lang="scss">
.header {
    padding: 12px 16px;
    height: 54px;
    border-bottom: 1px solid #e8e9ec36;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    color: var(--tg-theme-text-color);
    width: 100%;
}
.container {
  padding: 24px 16px 16px;
  width: 100%;
}
.home {
  height: 100%;
}

.v-select {
  position: relative;
}
.vs__search {
  padding: 0 16px;
  height: 44px;
  width: 100%;
  border-radius: 4px;
  border: 1px solid #c9c9c9;
  outline: none;
}
.vs__actions {
  position: absolute;
      top: 0;
    right: 0;
    width: 44px;
    height: 100%;
  svg {
    fill: #3c3c3c80;
  }
}
.vs__clear {
      width: 100%;
    height: 100%;
    background: none;
    border: none;
}

.vs__dropdown-menu {
    position: absolute;
    right: 0;
    left: 0;
    background: #fff;
  border: 1px solid #c9c9c9;

    margin: 0;
    padding: 0;
    list-style: none;
        border-radius: 4px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    margin-top: -1px;
}
.vs__dropdown-option {
    padding: 16px;
}
.vs__selected {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 16px;
  color: #152242;
}
.vs--open .vs__search {
  border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
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
</style>