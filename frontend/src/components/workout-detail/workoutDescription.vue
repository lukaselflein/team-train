<template>
  <div>
    <h6>
      DESCRIPTION
    </h6>
    <div v-if="item != ''">
      <p>{{ item }}</p>
    </div>
    <div v-else><p>No description.</p></div>
  </div>
</template>

<script>
export default {
  name: "WorkoutDescrition",
  props: {
    item: {
      type: String,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";
h6 {
  margin-top: 1em;
}
</style>