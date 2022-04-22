<template>
    <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
    <router-view />
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
</style>
