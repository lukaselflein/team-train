<template>
  <div>
    <p>SCORE</p>
    <div id="sq_score">
      <h4>12</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserScore"
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_score {
  @include square($alarm-title);
}
</style>
