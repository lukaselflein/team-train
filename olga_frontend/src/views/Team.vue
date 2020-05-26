<template>
  <div class="stati">
    <b-card class="card">
      <h4>Team statistics</h4>
      <p>you will find the scores of your teammembers here</p>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "Team"
};
</script>

<style lang="scss" scoped>
.stati {
  text-align: center;
  margin: 5em 1em 1em 1em;
  min-height: 100vh;
  .card {
    opacity: 0.9;
  }
}
</style>
