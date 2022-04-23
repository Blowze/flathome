<template>
    <div class="page-filter">
        <div class="filter">
            <div class="filter__header">
                <div class="filter__header-container">
                    <div class="city-curent">
                        <div class="city-curent__avatar">
                            <img :src="citySelect.image" />
                        </div>
                        <div class="city-curent__info">
                            <div class="city-curent__status status">
                                Ваш город:
                            </div>
                            <div class="city-curent__name title">
                                {{ citySelect.name }}
                            </div>
                        </div>
                    </div>
                    <button class="back-button" @click="buttonBack">
                        <span class="icon-equalizer"></span>
                    </button>
                </div>
            </div>
        </div>
        <div class="page-filter__container"></div>
        <h1>This is an filterView page</h1>
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
            },
        };
    },
    computed: {
        // геттер вычисляемого значения
        citySelect() {
            return this.$store.state.cityCurrent.id
                ? this.$store.state.cityCurrent
                : this.cityCurrent;
        },
    },
    mounted() {
        window.Telegram.WebApp.onEvent("mainButtonClicked", this.routerFilter);
    },
    methods: {
        buttonBack() {
            this.$router.push("/");
        },
    },
};
</script>
<style lang="scss" >
.back-button {
    margin-left: 8px;
    width: 30px;
    height: 30px;

    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: transparent;
    border: none;
    color: var(--tg-theme-hint-color);
    padding: 0;
    min-width: 30px;
    transition: background-color 0.15s, color 0.15s;
    &:hover,
    &:focus {
        background-color: #ffffff14;
    }
}
.city-curent {
    display: flex;
    text-align: left;
    align-items: center;
    width: 100%;
    &__avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        overflow: hidden;
        margin-right: 10px;
        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
    &__name {
        line-height: normal;
        font-size: 14px;
    }
    &__status {
        font-size: 10px;
    }
}
.page-filter {
    &__container {
        width: 100%;
        max-width: 480px;
        margin: 0 auto;
        padding: 4px 16px;
        text-align: center;
        margin: auto;
    }
}
.filter {
    &__header {
        box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25098);
        &-container {
            max-width: 480px;
            margin: auto;
            display: flex;
            align-items: center;
            padding: 8px;
        }
    }
}
</style>
