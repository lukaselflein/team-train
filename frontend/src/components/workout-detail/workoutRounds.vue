<template>
  <div>
    <h6>
      ROUNDS
    </h6>
    <div class="workout-rounds">
      <h3>{{ item }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "WorkoutRounds",
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

.workout-rounds {
  @include square($highlight);
}
</style>