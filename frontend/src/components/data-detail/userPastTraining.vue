<template>
  <div>
    <p>PAST TRAININGS</p>
    <div id="sq_past">
      <h4>14</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserPastTraining"
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_past {
  @include square($dark-title);
}
</style>
