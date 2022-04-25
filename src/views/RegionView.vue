<template>
    <div class="page">
        <div class="page__container">
            <SearchHeader
                :back-button="true"
                placeholder="Поиск региона"
                @keyup="submitSearch"
            />
        </div>
        <div class="SearchBody">
            <template v-if="region.length === 0">
                <div class="page__container">
                    <div class="SearchBody__noFound">Ничего не найдено</div>
                </div>
            </template>
            <div
                v-for="item in region"
                :key="'region-' + item"
                class="SearchBody__SearchCards"
            >
                <CheckboxDefault :text="item.name" />
            </div>
        </div>
    </div>
</template>

<script>
import SearchHeader from "../components/SearchHeader.vue";
import CheckboxDefault from "../components/Checkbox.vue";

export default {
    name: "HomeView",
    components: {
        SearchHeader,
        CheckboxDefault,
    },
    data() {
        return {
            searchInput: "",
            // delete if possible
            cityCurrent: {
                name: "Москва",
                image: "https://i.pinimg.com/originals/e8/97/68/e89768eb0617f7befeb48736bce12671.png",
                count: "13 Новостроек",
                id: 1,
                region: [
                    {
                        name: "Автозаводский",
                        id: 1,
                    },
                    {
                        name: "Канавинский",
                        id: 2,
                    },
                    {
                        name: "Московский",
                        id: 3,
                    },
                    {
                        name: "Лененский ",
                        id: 4,
                    },
                    {
                        name: "Балашиха",
                        id: 5,
                    },
                ],
            },
        };
    },
    computed: {
        region() {
            const isCityCurrent = this.$store.state.city.curent.name
                ? this.$store.state.city.curent
                : this.cityCurrent;
            if (this.searchInput) {
                return isCityCurrent.region.filter((item) =>
                    this.searchInput
                        .toLowerCase()
                        .split(" ")
                        .every((v) => item.name.toLowerCase().includes(v))
                );
            }
            return isCityCurrent.region;
        },
    },
    "$route.path": function () {
        window.Telegram.WebApp.offEvent("mainButtonClicked");
    },
    mounted() {
        window.Telegram.WebApp.onEvent("mainButtonClicked", this.backButton);
    },
    methods: {
        backButton() {
            this.$router.push("/filter");
        },
        submitSearch(e) {
            this.searchInput = e.target.value;
        },
        isActive(id) {
            return this.$store.state.city.regionCurrent.id === id;
        },
        setActiveRegion(item) {
            this.$store.commit("city/SET_SELECT_REGION", item);
            window.Telegram.WebApp.MainButton.setParams({
                text: "Выбрать регион",
                is_active: true,
                is_visible: true,
            });
        },
    },
};
</script>
