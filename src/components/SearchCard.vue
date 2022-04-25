<template>
    <Ripple>
        <div class="SearchCard" :class="{ 'SearchCard-Active': active }">
            <div v-if="image" class="SearchCard__avatar">
                <img :src="image" />
            </div>
            <div class="SearchCard__info">
                <div class="SearchCard__title">
                    {{ name }}
                </div>
                <div v-if="status" class="SearchCard__status">{{ status }}</div>
            </div>
        </div>
    </Ripple>
</template>

<script>
import Ripple from "./Ripple.vue";

export default {
    name: "SearchHeader",
    components: {
        Ripple,
    },
    props: {
        image: String,
        status: String,
        name: String,
        active: Boolean,
    },
};
</script>

<style scoped lang="scss" >
.SearchCard {
    padding: var(--space-small);
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
    &-Active {
        background: var(--tg-theme-button-color) !important;
        .SearchCard__status,
        .SearchCard__title {
            color: #fff;
        }
    }
    &__avatar {
        width: 54px;
        height: 54px;
        border-radius: 50%;
        margin-right: 16px;
        overflow: hidden;
        position: relative;
        background: var(--color-background);
        img {
            width: 100%;
            object-fit: cover;
            height: 100%;
        }
    }

    &__title {
        font-weight: bold;
        color: var(--tg-theme-text-color);
        line-height: 27px;
    }
    &__status {
        font-size: 14px;
        color: var(--tg-theme-hint-color);
    }
}
</style>
