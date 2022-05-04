<template>
    <div class="page">
        <FilterRegion
            :image="citySelect.image"
            :name="citySelect.name"
            @click="buttonBack"
        />
        <div class="page__container">
            <div class="ListItem">
                <div class="ListItem__image">
                    <img
                        src="https://cdn-p.cian.site/images/38/473/121/beketov-park-nizhniy-novgorod-jk-1213748318-7.jpg"
                        alt=""
                    />
                </div>
                <div class="ListItem__Info">
                    <div class="ListItem__Name"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import FilterRegion from "../components/FilterRegion.vue";

export default {
    name: "HomeView",
    components: {
        FilterRegion,
    },
    data() {
        return {
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
        citySelect() {
            const isCityCurrent = this.$store.state.city.curent.id
                ? this.$store.state.city.curent
                : this.cityCurrent;
            return isCityCurrent;
        },
    },
    methods: {
        buttonBack() {
            this.$router.push("/filter");
        },
    },
};
</script>
<style lang="scss" >
.SearchBody {
}
</style>
