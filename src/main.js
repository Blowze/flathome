import { createApp } from "vue";
import { createStore } from "vuex";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const storeCreate = createStore({
    ...store,
});
const app = createApp(App);

app.use(router);
app.use(storeCreate);

app.mount("#app");
