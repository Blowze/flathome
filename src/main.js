import { createApp } from "vue";
import Skeleton from "vue-loading-skeleton";
import Vue3TouchEvents from "vue3-touch-events";
import App from "./App.vue";
import router from "./router";
import "vue-loading-skeleton/dist/style.css";

createApp(App).use(router).use(Skeleton).use(Vue3TouchEvents).mount("#app");
