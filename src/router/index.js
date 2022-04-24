import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/CityView.vue";
import RegionView from "../views/RegionView.vue";
import FilterView from "../views/FilterView.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/filter",
        name: "about",
        component: FilterView,
    },
    {
        path: "/region",
        name: "region",
        component: RegionView,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
