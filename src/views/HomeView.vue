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
            <button
                v-for="item in city"
                :key="'city-' + item"
                class="item ripple ripple-js"
                :class="{ active: isActive(item.id) }"
                data-ripple-color="#FFF"
                @touchstart="setActive(item)"
                @click="setActive(item), animateButton($event)"
                @mousedown="setActive(item)"
            >
                <div class="avatar">
                    <img :src="item.image" alt="" />
                </div>
                <div class="info">
                    <div class="title">{{ item.name }}</div>
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
            activeItem: false,
            search: "",
        };
    },
    computed: {
        // геттер вычисляемого значения
        userName() {
            return this.$store.state.cityCurrent[0];
        },
        city() {
            if (this.search) {
                return this.$store.state.city.filter((item) =>
                    this.search
                        .toLowerCase()
                        .split(" ")
                        .every((v) => item.name.toLowerCase().includes(v))
                );
            }
            return this.$store.state.city;
        },
    },
    methods: {
        isActive(id) {
            return this.$store.state.cityCurrent.id === id;
        },
        setActive(item) {
            this.$store.commit("setCurentCity", item);
            window.Telegram.WebApp.MainButton.setParams({
                text: "Выбрать город",
                is_active: true,
                is_visible: true,
            });
        },
        animateButton(e) {
            const ripple = document.createElement("span");
            const rippleOffset = e.target.getBoundingClientRect();

            const rippleY = e.pageY - rippleOffset.top;
            const rippleX = e.pageX - rippleOffset.left;

            // eslint-disable-next-line no-sequences
            (ripple.style.top = `${rippleY}px`),
                (ripple.style.left = `${rippleX}px`),
                (ripple.style.background =
                    e.target.getAttribute("data-ripple-color"));

            e.target.appendChild(ripple);

            setTimeout(() => {
                ripple.parentNode.removeChild(ripple);
            }, 450);
        },
    },
};
</script>
<style lang="scss" >
.ripple {
    overflow: hidden;
    position: relative;
    z-index: 1;
    span {
        animation: ink 0.5s;
        border-radius: 100%;
        background: #ffffff;
        height: 12px;
        position: absolute;
        width: 12px;
    }
}
@keyframes ink {
    0% {
        opacity: 0.2;
        transform: scale(1);
    }
    100% {
        opacity: 0;
        transform: scale(40);
    }
}
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
    background: transparent;
    width: 100%;

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
