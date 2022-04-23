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

<style  lang="scss">
@import "assets/scss/reset";
@import "~assets/scss/config";
#app {
    font-family: "Montserrat", sans-serif;
    background: var(--tg-theme-bg-color);
    height: 100%;
}
.page {
    background: var(--tg-theme-bg-color);
    height: 100%;
}
body,
html {
    height: 100%;
    background: var(--tg-theme-bg-color);
}
.scale-enter-active,
.scale-leave-active {
    transition: all 0.2s ease;
}

.scale-enter-from,
.scale-leave-to {
    opacity: 0;
    transform: scale(0.9);
}
</style>
