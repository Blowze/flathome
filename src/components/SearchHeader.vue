<template>
    <div class="SearchHeader">
        <div class="SearchHeader__input">
            <input class="input" placeholder="Поиск города" />
            <i class="input__icon icon-search"></i>
        </div>
    </div>
</template>

<script>
export default {
    name: "SearchHeader",
};
</script>

<style scoped lang="scss" >
.SearchHeader {
    margin-bottom: var(--space-normal);

    &__input {
        position: relative;
        color: rgba(var(--color-text-secondary-rgb), 0.5);
        display: flex;
        align-items: center;
        width: 100%;
    }
}
.input {
    width: 100%;
    border-radius: 50%;
    height: 40px;
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
        left: var(--space-normal);
        font-size: 16px;
        pointer-events: none;
    }
}
</style>
