import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import vSelect from "vue-select";

createApp(App).use(router).component("v-select", vSelect).mount('#app')
