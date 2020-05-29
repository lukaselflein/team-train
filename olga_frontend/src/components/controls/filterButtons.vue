<template>
  <div class="filter-row">
    <b-button class="filter-btn" @click="nothing">last week</b-button>
    <b-button class="filter-btn" @click="nothing">last month</b-button>
    <b-button class="filter-btn" @click="nothing">all workouts</b-button>
  </div>
</template>

<script>
export default {
  name: "FilterButtons",
  methods: {
    nothing() {
      alert("Hey, I'm not doing anything yet :)");
    }
  }
};
</script>

<style lang="scss" scoped>
.filter-row {
  min-width: 100%;

  .filter-btn {
    margin: 0 0.25em;
  }
}
</style>
