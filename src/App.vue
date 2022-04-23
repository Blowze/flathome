<template>
    <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
    <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
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
body,
html {
    height: 100%;
    background: var(--tg-theme-bg-color);
}
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>
