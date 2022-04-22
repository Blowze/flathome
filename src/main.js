import { createApp } from "vue";
import Skeleton from "vue-loading-skeleton";
import App from "./App.vue";
import router from "./router";
import "vue-loading-skeleton/dist/style.css";

createApp(App).use(router).use(Skeleton).mount("#app");
