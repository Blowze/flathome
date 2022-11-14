<template>
    <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
    <router-view v-slot="{ Component }">
        <transition name="scale" mode="out-in">
            <component :is="Component" />
        </transition>
    </router-view>
</template>
<script>
/* eslint-disable no-undef */
export default {
    name: "HomeView",
    mounted() {
        this.$nextTick(() => {
            Telegram.WebApp.ready();
            Telegram.WebApp.MainButton.onClick(Cafe.mainBtnClicked);
        });
    },
};
</script>
<style  lang="scss">
@import "assets/scss/reset";
@import "~assets/scss/config";
@import "~assets/scss/animate";

#app {
    font-family: "Montserrat", sans-serif;
    background: var(--tg-theme-bg-color);
    height: 100%;
}
body,
html {
    height: 100%;
}
.page {
    min-height: 100%;
    &__container {
        width: 100%;
        max-width: 560px;
        margin: 0 auto;
        padding: var(--space-small) var(--space-normal);
        text-align: center;
    }
}
.scrollable::-webkit-scrollbar {
    width: 0;
    height: 0;
    opacity: 0;
    width: 0.375rem;
}

.scrollable::-webkit-scrollbar-thumb {
    width: 0;
    height: 0;
}

::-webkit-scrollbar-thumb {
    opacity: 0;
    -webkit-transition: 0.2s ease-in-out;
    transition: 0.2s ease-in-out;
}

::-webkit-scrollbar-button {
    width: 0;
    height: 0;
    display: none;
}

::-webkit-scrollbar-corner {
    background-color: transparent;
}

.scrollable:hover::-webkit-scrollbar {
    opacity: 1;
}

.scrollable:hover::-webkit-scrollbar-thumb {
    min-height: 5rem;
    max-height: 12.5rem;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.2);
    -webkit-backdrop-filter: blur(100);
    opacity: 1;
}
.scrollable {
    width: 100%;
    height: 100%;
    overflow-y: hidden;
    overflow-x: hidden;
    max-height: 100%;
    position: absolute;
    top: 0px;
    left: 0px;
    bottom: 0px;
    right: 0px;
    -webkit-overflow-scrolling: touch;
}
.scrollable.scrollable-y {
    overflow-y: auto;
    overflow-y: overlay;
    scrollbar-width: thin;
    -ms-overflow-style: none;
    transform: translateZ(0);
}
</style>
