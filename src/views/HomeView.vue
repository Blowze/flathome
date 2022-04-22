<template>
    <div class="welcome">
        <div class="form">
            <div class="form__input">
                <input
                    v-model="search"
                    type="text"
                    class="input"
                    placeholder="Поиск города"
                    @keyup="submitSearch"
                />
                <i class="input__icon icon-search"></i>
            </div>
        </div>
        <div class="form__body">
            <template v-if="city.length === 0">
                <div class="noFound">Ничего не найдено</div>
            </template>
            <div
                v-for="(item, index) in city"
                :key="'city-' + item"
                class="item"
                :class="{ active: isActive(index) }"
                @touchstart="setActive(index)"
                @click.prevent="setActive(index)"
            >
                <div class="avatar">
                    <img :src="item.image" alt="" />
                </div>
                <div class="info">
                    <div class="title">{{ item.name }}</div>
                    <div class="status">{{ item.count }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomeView",
    data() {
        return {
            activeItem: false,
            search: "",
        };
    },
    computed: {
        // геттер вычисляемого значения
        userName() {
            // `this` указывает на экземпляр vm
            return window.Telegram.WebApp.initDataUnsafe.user;
        },
        city() {
            return this.$store.state.city.filter(
                (item) => item.name.indexOf(this.search) !== -1
            );
        },
    },
    methods: {
        isActive(menuItem) {
            return this.activeItem === menuItem;
        },
        submitSearch() {
            this.activeItem = false;
            window.Telegram.WebApp.MainButton.setParams({
                text: "Выбрать город",
                is_active: false,
                is_visible: false,
            });
        },
        setActive(menuItem) {
            this.activeItem = menuItem;
            window.Telegram.WebApp.MainButton.setParams({
                text: "Выбрать город",
                is_active: true,
                is_visible: true,
            });
        },
    },
};
</script>
<style lang="scss" scoped>
.noFound {
    color: var(--tg-theme-hint-color);
}
.title {
    font-weight: bold;
    color: var(--tg-theme-text-color);
    line-height: 27px;
}
.status {
    font-size: 14px;
    color: var(--tg-theme-hint-color);
}
.item {
    padding: 9px;
    overflow: hidden;
    border-radius: 0.75rem;
    display: flex;
    align-items: center;
    text-align: left;
    cursor: pointer;
    touch-action: manipulation;
    border: none;

    &.active {
        background: var(--tg-theme-button-color) !important;
        .title,
        .status {
            color: #fff;
        }
    }
}
.avatar {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    margin-right: 16px;
    overflow: hidden;
    img {
        width: 100%;
        object-fit: cover;
        height: 100%;
    }
}
.form {
    margin-bottom: 16px;
    &__input {
        position: relative;
        color: rgba(var(--color-text-secondary-rgb), 0.5);
        display: flex;
        align-items: center;
    }
    &__icon {
    }
}
.input {
    width: 100%;
    border-radius: 50%;
    height: 2.5rem;
    border-radius: 1.25rem;
    background: var(--color-background);
    border: 2px solid var(--color-background);
    outline: none;
    transition: border-color 0.15s ease;
    color: rgba(var(--tg-theme-hint-color-rgb), 0.5);
    padding-left: 40px;
    &:focus,
    &:active {
        border-color: var(--tg-theme-link-color);
        caret-color: var(--tg-theme-link-color);
        color: var(--tg-theme-text-color);
        & + [class^="icon-"],
        & + [class*=" icon-"] {
            color: var(--tg-theme-link-color);
        }
    }
    &__icon {
        position: absolute;
        left: 16px;
        font-size: 16px;
        pointer-events: none;
    }
}
.welcome {
    width: 100%;
    max-width: 480px;
    margin: 0 auto;
    padding: 4px 16px;
    text-align: center;
    margin: auto;
}
</style>
