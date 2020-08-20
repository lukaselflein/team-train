<template>
  <div class="filter-row">
    <b-button class="filter-btn" disabled>last week</b-button>
    <b-button class="filter-btn" disabled>last month</b-button>
    <b-button class="filter-btn" disabled>all</b-button>
  </div>
</template>

<script>
export default {
  name: "FilterButtons"
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
