<template>
    <div class="welcome page home">
        <div class="form">
            <div class="form__input">
                <input
                    v-model="search"
                    class="input"
                    placeholder="Поиск региона"
                    @keyup="submitSearch"
                />

                <i class="input__icon icon-search"></i>
            </div>
        </div>

        <div class="form__body">
            <template v-if="region.length === 0">
                <div class="noFound">Ничего не найдено</div>
            </template>
            <button
                v-for="item in region"
                :key="'region-' + item"
                class="item ripple ripple-js"
                :class="{ active: isActive(item.id) }"
                data-ripple-color="#FFF"
                @touchstart="setActive(item)"
                @click="setActive(item), animateButton($event)"
                @mousedown="setActive(item)"
            >
                <div class="info">
                    <div class="title">
                        {{ item.name }}
                    </div>
                    <div class="status">{{ item.count }}</div>
                </div>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomeView",
    data() {
        return {
            search: "",
            searchInput: "",
            cityCurrent: {
                name: "Москва",
                image: "https://i.pinimg.com/originals/e8/97/68/e89768eb0617f7befeb48736bce12671.png",
                count: "13 Новостроек",
                isActive: false,
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
            if (this.searchInput) {
                return this.cityCurrent.region.filter((item) =>
                    this.searchInput
                        .toLowerCase()
                        .split(" ")
                        .every((v) => item.name.toLowerCase().includes(v))
                );
            }
            return this.cityCurrent.region;
        },
    },
    mounted() {
        window.Telegram.WebApp.onEvent("mainButtonClicked", this.routerFilter);
    },
    methods: {
        routerFilter() {
            this.$router.push("/filter");
        },
        submitSearch(e) {
            this.searchInput = e.target.value;
        },
        isActive(id) {
            return this.cityCurrent.region.id === id;
        },
        setActive(item) {
            this.$store.commit("setCurentCity", item);
            window.Telegram.WebApp.MainButton.setParams({
                text: "Выбрать регион",
                is_active: true,
                is_visible: true,
            });
        },
        animateButton(e) {
            const ripple = document.createElement("i");
            const rippleOffset = e.currentTarget.getBoundingClientRect();

            const rippleY = e.pageY - rippleOffset.top;
            const rippleX = e.pageX - rippleOffset.left;

            // eslint-disable-next-line no-sequences
            (ripple.style.top = `${rippleY}px`),
                (ripple.style.left = `${rippleX}px`),
                (ripple.style.background =
                    e.currentTarget.getAttribute("data-ripple-color"));

            e.currentTarget.appendChild(ripple);

            setTimeout(() => {
                ripple.parentNode.removeChild(ripple);
            }, 300);
        },
    },
};
</script>
<style lang="scss" >

</style>
