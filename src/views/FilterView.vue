<template>
    <div class="page PageFilter">
        <FilterRegion
            :image="citySelect.image"
            :name="citySelect.name"
            @click="buttonBack"
        />
        <div class="FilterBody">
            <div class="scrollable scrollable-y">
                <div class="FilterBody__Item FilterBody__ItemIsList">
                    <div class="Developer">
                        <div class="Developer__Avatar">
                            <img
                                src="https://avatars.mds.yandex.net/get-zen_doc/4387796/pub_602647ddb1a0bb52b47194b2_6026480d331cb763522019d5/scale_1200"
                                alt=""
                            />
                        </div>
                        <div class="Developer__Info">
                            <div class="Developer__Name">ПИК-Застройщик</div>
                            <div class="Developer__Status">Рекомендуемый</div>
                        </div>
                    </div>
                    <h4 class="FilterBody__Title">Застройщик</h4>

                    <CheckboxDefault text="Застройщик Премиум" />
                    <CheckboxDefault text="Застройщик Премиум" />
                    <CheckboxDefault text="Застройщик Премиум" />
                    <Ripple>
                        <div class="ItemLink" @click="selectRegion">
                            <div class="icon-eye"></div>
                            <div class="ItemLink__Title">
                                Показать полный список
                            </div>
                        </div>
                    </Ripple>
                </div>
                <div class="TextHint">в базе 72 застройщика</div>
                <div class="FilterBody__Item FilterBody__ItemIsList">
                    <h4 class="FilterBody__Title">Регион</h4>
                    <CheckboxDefault
                        v-for="item in region"
                        :key="'region-' + item"
                        :text="item.name"
                    />
                    <Ripple>
                        <div class="ItemLink" @click="selectRegion">
                            <div class="icon-eye"></div>
                            <div class="ItemLink__Title">
                                Показать полный список
                            </div>
                        </div>
                    </Ripple>
                    <!-- <button class="FilterBody__ButtonAdd">Показать еще</button> -->
                </div>

                <div class="FilterBody__Item">
                    <h4 class="FilterBody__Title">Тип</h4>
                    <CheckboxDefault text="Жилая" />
                    <CheckboxDefault text="Аппартаменты" />
                </div>
                <div class="FilterBody__Item">
                    <h4 class="FilterBody__Title">Этажность</h4>
                    <div class="Slider">
                        <Slider v-model="floors" :tooltips="false" />
                        <div class="Slider__Footer">
                            <span> {{ floors[0] }}</span>
                            <span>{{ floors[1] }}</span>
                        </div>
                    </div>
                </div>
                <div class="FilterBody__Item">
                    <h4 class="FilterBody__Title">Кол-во комнат</h4>
                    <CheckboxDefault text="1" />
                    <CheckboxDefault text="2" />
                    <CheckboxDefault text="3" />
                    <CheckboxDefault text="4" />
                    <CheckboxDefault text="5+" />
                </div>
                <div class="FilterBody__Item">
                    <h4 class="FilterBody__Title">Площадь</h4>
                    <div class="InputFieldRow">
                        <div class="InputField">
                            <input
                                type="number"
                                autocomplete="off"
                                required=""
                                class="InputField__Input"
                                dir="auto"
                            />
                            <div class="InputField-Border"></div>
                            <label><span class="i18n">От</span></label>
                        </div>
                        <div class="InputField">
                            <input
                                type="number"
                                autocomplete="off"
                                required=""
                                class="InputField__Input"
                                dir="auto"
                            />
                            <div class="InputField-Border"></div>
                            <label><span class="i18n">До</span></label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Slider from "@vueform/slider";
import FilterRegion from "../components/FilterRegion.vue";
import CheckboxDefault from "../components/Checkbox.vue";
import Ripple from "../components/Ripple.vue";

export default {
    name: "HomeView",
    components: {
        FilterRegion,
        CheckboxDefault,
        Slider,
        Ripple,
    },
    data() {
        return {
            search: "",
            searchInput: "",
            floors: [0, 50],
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
        // геттер вычисляемого значения
        citySelect() {
            const isCityCurrent = this.$store.state.city.curent.id
                ? this.$store.state.city.curent
                : this.cityCurrent;
            return isCityCurrent;
        },
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
            return isCityCurrent.region.slice(1);
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
                    text: "Выбрать регион",
                    is_active: true,
                    is_visible: true,
                });
            } else {
                window.Telegram.WebApp.MainButton.setParams({
                    text: "Выбрать регион",
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
    },
};
</script>
<style src="@vueform/slider/themes/default.css"></style>
<style lang="scss" >
.TextHint {
    font-size: 14px;
    color: var(--tg-theme-hint-color);
    padding-left: var(--space-normal);
    margin-bottom: var(--space-normal);
}
.ItemLink {
    padding: 11px 16px;
    margin-left: -16px;
    margin-right: -16px;
    color: var(--tg-theme-text-color);
    border-top: 1px solid var(--color-border-item);
    display: flex;
    align-items: center;
    position: relative;
    color: var(--tg-theme-button-color);
    text-align: center;
    height: 44px;
    [class^="icon-"] {
        position: absolute;
        font-size: 18px;
        left: 32px;
    }
    &__Title {
        width: 100%;
    }
}
.PageFilter {
    background: var(--color-background-secondary);
    flex-direction: column;
    grid-row-start: 1;
    grid-column-start: 1;
    overflow: hidden;
    display: flex;
}
.FilterBody {
    width: 100%;
    max-width: 480px;
    margin: 0 auto;
    max-height: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    position: relative;
    flex: 1 1 auto;

    &__Item {
        background: var(--tg-theme-bg-color);
        margin-bottom: 12px;

        padding-top: var(--space-small);
        padding-bottom: var(--space-small);
        box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.12);
        &:first-child {
            padding-top: 0;
        }
    }
    &__ItemIsList {
        padding-bottom: 0;
    }
    &__Title {
        padding-top: var(--space-small);
        padding-bottom: var(--space-small);
        color: var(--tg-theme-button-color);
        margin: 0;
        line-height: 24px;
        padding-left: var(--space-normal);
        padding-right: var(--space-normal);
    }
}
.Slider {
    margin-top: var(--space-normal);
    margin-bottom: var(--space-normal);
    padding-left: var(--space-normal);
    padding-right: var(--space-normal);

    &__Footer {
        display: flex;
        justify-content: space-between;
        color: var(--tg-theme-hint-color);
        padding-top: 24px;
    }
}
.InputField {
    position: relative;
    border-radius: 10px;
    height: 50px;
    flex: 1 1 auto;
    &:last-child {
        margin-left: 20px;
    }
    &__Input {
        padding: 14px;
        border: 1px solid var(--color-border-input);
        border-radius: 10px;
        background-color: transparent;
        box-sizing: border-box;
        width: 100%;
        min-height: 50px;
        transition: 0s border-color;
        position: relative;
        z-index: 1;
        line-height: 1.3125;
        outline: none;
        color: var(--tg-theme-text-color);
        &:focus {
            border-color: var(--tg-theme-button-color);
            & ~ label {
                color: var(--tg-theme-button-color);
                font-weight: bold;
            }
            & ~ .InputField-Border {
                opacity: 1;
                border-color: var(--tg-theme-button-color);
            }
        }
    }
    label {
        position: absolute;
        color: var(--tg-theme-hint-color);
        top: 0;
        left: 1rem;
        right: auto;
        z-index: 2;
        height: 1.5rem;
        transform: translate(0, 0);
        background-color: #fff;
        background-color: var(--tg-theme-bg-color);
        transform-origin: left center;
        pointer-events: none;
        margin-top: calc((51px - 1.5rem) / 2);
        padding: 0 6px;
        font-weight: 500;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        white-space: nowrap;
        transform: translate(-0.25rem, calc(50px / -2 + 0.125rem)) scale(0.75);
    }
    &-Border {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        border: 2px solid var(--tg-theme-bg-color);
        opacity: 0;
        border-radius: 10px;
        pointer-events: none;
        z-index: 2;
    }
}

.InputFieldRow {
    display: flex;
    margin-top: 16px;
    margin-bottom: 16px;
    padding-left: var(--space-normal);
    padding-right: var(--space-normal);
}

.Developer {
    height: 240px;
    position: relative;
    margin-bottom: 8px;
    &__Avatar {
        position: relative;
        height: 100%;
        &:before {
            content: ""; /* отображает псевдоэлемент */
            position: absolute; /* абсолютное позиционирование */
            top: 0; /* верхняя координата */
            left: 0; /* левая координата */
            width: 100%; /* относительная ширина */
            height: 100%; /* высота как у оригинала */
            background-color: rgba(
                255,
                255,
                255,
                0.1
            ); /* белый цвет с полупрозрачностью */
            transform: translateX(-130%) skewX(-45deg);
            animation: moveLight 5s infinite linear;
        }
        &:after {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: 140px;
            background: linear-gradient(
                360deg,
                rgb(0 0 0 / 57%) 8.98%,
                rgba(0, 0, 0, 0) 100%
            );
        }
    }
    &__Info {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 16px;
    }
    &__Name {
        color: #fff;
        font-weight: bold;
        margin-bottom: 6px;
    }
    &__Status {
        color: #0ac630;
    }
    img {
        width: 100%;
        height: 100%;
        display: flex;
        flex-wrap: nowrap;
        object-fit: cover;
    }
}
</style>
