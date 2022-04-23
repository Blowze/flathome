<template>
    <div class="page-filter">
        <div class="filter">
            <div
                class="filter__header ripple ripple-js"
                @click="buttonBack(), animateButton($event)"
            >
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
                    <button class="back-button">
                        <span class="icon-cog"></span>
                    </button>
                </div>
            </div>
        </div>
        <div class="page-filter__container">
            <div class="filter__item flex hover" @click="selectRegion">
                <div class="filter__info">{{ regionCurent }}</div>
                <div class="icon-arrow-right2"></div>
                <!-- <button type="button" class="button button-filter">
                    Добавить
                </button> -->
            </div>
            <div class="filter__item">
                <h4 class="filter__title">Тип</h4>
                <div class="filter__body">
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Жилая </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Апартаменты </span>
                        </div>
                    </label>
                </div>
            </div>
            <div class="filter__item">
                <h4 class="filter__title">Количество комнат</h4>
                <div class="filter__body room-grid">
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> 1 </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> 2 </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> 3 </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> 4 </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> 5+ </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="room" />
                        <div class="checkbox-main">
                            <span class="label"> Студия </span>
                        </div>
                    </label>
                </div>
            </div>
            <div class="filter__item">
                <h4 class="filter__title">Площадь</h4>
                <div class="filter__body">
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Жилая </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Апартаменты </span>
                        </div>
                    </label>
                </div>
            </div>
            <div class="filter__item">
                <h4 class="filter__title">Этажность</h4>
                <div class="filter__body">
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Жилая </span>
                        </div>
                    </label>
                    <label class="checkbox">
                        <input type="checkbox" name="peas" />
                        <div class="checkbox-main">
                            <span class="label"> Апартаменты </span>
                        </div>
                    </label>
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
        regionCurent() {
            return this.$store.state.regionCurrent.lenght
                ? this.$store.state.regionCurrent.name
                : "Ваш регион не указан";
        },
    },
    mounted() {
        window.Telegram.WebApp.onEvent("mainButtonClicked", this.routerFilter);
        window.Telegram.WebApp.MainButton.setParams({
            text: "Поиск",
            is_active: true,
            is_visible: true,
        });
    },
    methods: {
        selectRegion() {
            this.$router.push("/region");
            if (this.$store.state.regionCurrent) {
                window.Telegram.WebApp.MainButton.setParams({
                    text: "Выбрать город",
                    is_active: true,
                    is_visible: true,
                });
            } else {
                window.Telegram.WebApp.MainButton.setParams({
                    text: "Выбрать город",
                    is_active: false,
                    is_visible: false,
                });
            }
        },
        buttonBack() {
            this.$router.push("/");
            if (this.$store.state.cityCurrent) {
                window.Telegram.WebApp.MainButton.setParams({
                    text: "Выбрать город",
                    is_active: true,
                    is_visible: true,
                });
            } else {
                window.Telegram.WebApp.MainButton.setParams({
                    text: "Выбрать город",
                    is_active: false,
                    is_visible: false,
                });
            }
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
.checkbox {
    display: block;
    position: relative;
    padding-left: calc(20px + 18px);
    text-align: left;
    margin-bottom: 12px;
    line-height: 22px;
    color: var(--tg-theme-text-color);
    font-size: 14px;
    cursor: pointer;
    input {
        position: absolute;
        z-index: -1;
        opacity: 0;
    }
    .checkbox-main {
        &::before,
        &::after {
            content: "";
            display: block;
            position: absolute;
            left: 0;
            top: 0;
            width: 18px;
            height: 18px;
        }

        &::before {
            border: 2px solid var(--color-border-input);
            border-radius: 0.25rem;
            background-color: var(--color-background);
            transition: border-color 0.1s ease, background-color 0.1s ease;
        }

        &::after {
            /* stylelint-disable-next-line scss/operator-no-unspaced */
            background: center no-repeat
                url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEzLjkuOEw1LjggOC45IDIuMSA1LjJjLS40LS40LTEuMS0uNC0xLjYgMC0uNC40LS40IDEuMSAwIDEuNkw1IDExLjJjLjQuNCAxLjEuNCAxLjYgMGw4LjktOC45Yy40LS40LjQtMS4xIDAtMS42LS41LS40LTEuMi0uNC0xLjYuMXoiIGZpbGw9IiNGRkYiIGZpbGwtcnVsZT0ibm9uemVybyIvPjwvc3ZnPg==);
            background-size: 0.875rem;
            opacity: 0;
            transition: opacity 0.1s ease;
            width: 22px;
            height: 22px;
        }

        .label {
            display: block;
            text-align: initial;
        }
    }

    input:checked ~ .checkbox-main {
        &::before {
            border-color: var(--tg-theme-link-color);
            background-color: var(--tg-theme-button-color);
        }

        &::after {
            opacity: 1;
        }
    }

    &[dir="rtl"] {
        padding-left: 0;
        padding-right: 4.5rem;

        &.loading {
            .Spinner {
                left: auto;
                right: 0.375rem;
            }
        }

        .label,
        .subLabel {
            text-align: right;
        }

        .checkbox-main {
            &::before,
            &::after {
                left: auto;
                right: 1.1875rem;
            }
        }
    }
}
.button-filter {
    padding: 0 15px;
    font-size: 12px;
    height: 32px;
    border-radius: 1.25rem;
    width: auto;
    background: var(--tg-theme-button-color);
    color: var(--tg-theme-button-text-color);
    border: none;
    display: flex;
    align-items: center;
}

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
    cursor: pointer;
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
    background: var(--color-background-secondary);

    &__container {
        width: 100%;
        max-width: 480px;
        margin: 0 auto;
        text-align: center;
        margin: auto;
        & > div {
            background: var(--tg-theme-bg-color);
        }
    }
}
.filter {
    // box-shadow: 0 2px 2px rgba(0, 0, 0, 0.25098);
    &__title {
        margin-top: 8px;
        margin-bottom: 24px;
    }
    &__info {
        font-size: 14px;
    }
    &__item {
        text-align: left;
        color: var(--tg-theme-hint-color);
        margin-top: 8px;
        padding: 16px;
        &.flex {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        &.hover {
            cursor: pointer;
            &:hover,
            &:focus,
            &:active {
                background: var(--color-background);
            }
        }
        &:first-child {
            margin-top: 0;
            border-top: 1px solid var(--color-border-item);
        }
    }
    &__header {
        &-container {
            max-width: 480px;
            margin: auto;
            display: flex;
            align-items: center;
            padding: 8px;
            padding-left: 16px;
            padding-right: 10px;
            background: var(--tg-theme-bg-color);
            cursor: pointer;
            &:hover,
            &:focus,
            &:active {
                background: var(--color-background);
            }
        }
    }
}
</style>
