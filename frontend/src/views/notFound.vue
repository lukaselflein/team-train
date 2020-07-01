<template>
  <div id="notFound">
    <h3>Page not found...</h3>
    <p>And no Training here ;(</p>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  components: {}
};
</script>
<style lang="scss" scoped>
@import "../mixins.scss";

#notFound {
  @include background;
  min-width: 400px;
  margin: 8em auto 0 auto;
  max-width: 50%;
  opacity: 0.9;
  justify-content: center;
  text-align: center;
}

@media only screen and (min-width: 701px) {
  .card {
    max-width: 500px;
    min-width: 500px;
  }
}
</style>
