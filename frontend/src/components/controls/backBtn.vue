<template>
  <div>
    <router-link to="/workouts" id="backLink">back to workouts</router-link>
  </div>
</template>

<script>
export default {
  name: "BackBtn"
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#backLink {
  text-decoration: underline;
  cursor: pointer;
  color: $alarm-title;
  font-size: 1rem;
  font-weight: bold;
}
</style>
