<template>
    <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
    <router-view v-slot="{ Component }">
        <transition name="animation-scale" mode="animation-out-in">
            <component :is="Component" />
        </transition>
    </router-view>
</template>

<style  lang="scss">
@import "assets/scss/reset";
@import "~assets/scss/config";
@import "~assets/scss/animate";

#app {
    font-family: "Montserrat", sans-serif;
    background: var(--tg-theme-bg-color);
    min-height: 100vh;
}
.page {
    &__container {
        width: 100%;
        max-width: 480px;
        margin: 0 auto;
        padding: var(--space-small) var(--space-normal);
        text-align: center;
        margin: auto;
    }
}
</style>
