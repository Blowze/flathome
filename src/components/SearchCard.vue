<template>
    <div
        class="SearchCard SearchCard-Ripple"
        data-ripple-color="#FFF"
        :class="{ 'SearchCard-Active': active }"
        @click="animateButton($event)"
    >
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
</template>

<script>
export default {
    name: "SearchHeader",
    props: {
        image: String,
        status: String,
        name: String,
        active: Boolean,
    },
    methods: {
        animateButton(e) {
            // If possible, correct
            const ripple = document.createElement("i");
            ripple.classList.add("animation-ripple");
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
    &-Ripple {
        overflow: hidden;
        position: relative;
        z-index: 1;
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
