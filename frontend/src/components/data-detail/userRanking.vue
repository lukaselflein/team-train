<template>
  <div>
    <p>POSITION</p>
    <div id="sq_rank">
      <h4>#1</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserRanking"
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_rank {
  @include square($dark);
}
</style>
