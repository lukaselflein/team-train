<template>
  <div>
    <h6>POINTS</h6>
    <div class="workout-points">
      <h3>{{ item }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "WorkoutPoints",
  props: {
    item: {
      type: Number,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";
.workout-points {
  @include square($alarm-title);
  h4 {
    color: white;
  }
}
</style>