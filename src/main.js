import { createApp } from "vue";
import Skeleton from "vue-loading-skeleton";
import { createStore } from "vuex";
import App from "./App.vue";
import router from "./router";
import "vue-loading-skeleton/dist/style.css";

const store = createStore({
    state: {
        city: [
            {
                name: "Москва",
                image: "https://i.pinimg.com/originals/e8/97/68/e89768eb0617f7befeb48736bce12671.png",
                count: "13 Новостроек",
                isActive: false,
            },
            {
                name: "Нижний Новгород",
                image: "https://newsnn.ru/attachments/5850fe322b2c98f3e28e68bd9f9a38ee56c4b3e1/store/fill/1200/630/a7ef409a429eafd92ccf7cdee2984ea77263693c0af3bebc9007cf0b5aad/a7ef409a429eafd92ccf7cdee2984ea77263693c0af3bebc9007cf0b5aad.jpg",
                count: "127 Новостроек",
                isActive: false,
            },
            {
                name: "Санкт Петербург",
                image: "https://regnum.ru/uploads/pictures/news/2016/12/01/regnum_picture_148061156442226_normal.jpg",
                count: "17 Новостроек",
                isActive: false,
            },
        ],
    },
});
const app = createApp(App);
app.use(router);
app.use(Skeleton);
app.use(store);

app.mount("#app");
