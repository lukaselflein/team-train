<template>
  <div id="notFound">
    <b-card class="card">
      <h4>Page not found...</h4>
      <p>And no Training here ;(</p>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  components: {}
};
</script>
<style scoped>
#notFound {
  display: flex;
  justify-content: center;
  text-align: center;
}
.card {
  min-width: 400px;
  margin: 8em 2em 0 2em;
  opacity: 0.9;
}
@media only screen and (min-width: 701px) {
  .card {
    max-width: 500px;
    min-width: 500px;
  }
}
</style>
