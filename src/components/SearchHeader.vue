<template>
    <div class="SearchHeader" :class="{ 'SearchHeader-Flex': backButton }">
        <button
            v-if="backButton"
            class="SearchHeader__BackButton"
            @click="backButtonRouter"
        >
            <span class="icon-arrow-left2"></span>
        </button>
        <div class="SearchHeader__input">
            <input class="input" :placeholder="placeholder" />
            <i class="input__icon icon-search"></i>
        </div>
    </div>
</template>

<script>
export default {
    name: "SearchHeader",
    props: {
        backButton: Boolean,
        placeholder: String,
    },
    methods: {
        backButtonRouter() {
            this.$router.push("/filter");
        },
    },
};
</script>

<style scoped lang="scss" >
.SearchHeader {
    margin-bottom: var(--space-normal);
    &-Flex {
        display: flex;
        align-items: center;
    }
    &__input {
        position: relative;
        color: rgba(var(--color-text-secondary-rgb), 0.5);
        display: flex;
        align-items: center;
        width: 100%;
        position: relative;
    }
    &__BackButton {
        margin-right: var(--space-small);
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
        &:hover,
        &:focus,
        &:active {
            background: var(--item-hover-bg);
        }
    }
}
.input {
    width: 100%;
    border-radius: 50%;
    height: 40px;
    border-radius: 22px;
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
        left: var(--space-normal);
        font-size: 16px;
        pointer-events: none;
    }
}
</style>
