<template>
    <div class="page">
        <div class="page__container">
            <SearchHeader
                placeholder="Поиск города"
                @keyup="submitSearchCity"
            />
            <div class="SearchBody">
                <template v-if="city.length === 0">
                    <div class="SearchBody__noFound">Ничего не найдено</div>
                </template>
                <div
                    v-for="item in city"
                    :key="'city-' + item"
                    class="SearchBody__SearchCards"
                >
                    <SearchCard
                        :name="item.name"
                        :image="item.image"
                        :status="item.count"
                        :active="isActive(item.id)"
                        @touchstart="setActiveCity(item)"
                        @click="setActiveCity(item)"
                        @mousedown="setActiveCity(item)"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SearchHeader from "../components/SearchHeader.vue";
import SearchCard from "../components/SearchCard.vue";

export default {
    name: "HomeView",
    components: {
        SearchCard,
        SearchHeader,
    },
    data() {
        return {
            searchInput: "",
            buttonParams: {
                text: "Выбрать город",
                is_active: true,
                is_visible: true,
            },
        };
    },
    computed: {
        city() {
            if (this.searchInput) {
                return this.$store.state.city.items.filter((item) =>
                    this.searchInput
                        .toLowerCase()
                        .split(" ")
                        .every((v) => item.name.toLowerCase().includes(v))
                );
            }
            return this.$store.state.city.items;
        },
    },
    watch: {
        "$route.path": function () {
            window.Telegram.WebApp.offEvent("mainButtonClicked");
        },
    },
    mounted() {
        window.Telegram.WebApp.onEvent("mainButtonClicked", this.routerFilter);
    },
    methods: {
        submitSearchCity(e) {
            this.searchInput = e.target.value;
        },
        routerFilter() {
            this.$router.push("/filter");
        },

        isActive(id) {
            return this.$store.state.city.curent.id === id;
        },
        setActiveCity(item) {
            this.$store.commit("city/SET_SELECT", item);
            this.$store.commit("city/SET_SELECT_REGION", {});

            window.Telegram.WebApp.MainButton.setParams(this.buttonParams);
        },
    },
};
</script>
<style lang="scss" >
.SearchBody {
    &__noFound {
        color: var(--tg-theme-hint-color);
    }
}
</style>
