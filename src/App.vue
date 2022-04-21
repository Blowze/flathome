<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <router-view/>
</template>

<style  lang="scss">
@import "assets/scss/reset";
@import "~assets/scss/config";
#app {
 font-family: 'Montserrat', sans-serif;
 background: var(--color-primary);
 height: 100%;
}
html {
  height: var(--tg-viewport-stable-height);
}
body {
  height: 100%;
}
</style>
