<template>
 <div class="logo">
      <span>flat</span>
      <b>House</b>
    </div>
</template>

<script>
export default {
  name: 'LogoMain',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped  lang="scss">
.logo {
  font-size: 40px;
  color: #fff;
  transition: transform 300ms linear;
  will-change: transform;
}
</style>
