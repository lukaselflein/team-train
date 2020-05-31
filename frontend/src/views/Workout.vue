<template>
  <div>
    <WorkoutList />
  </div>
</template>

<script>
import WorkoutList from "@/components/data-overview/workoutList.vue";

export default {
  name: "Workout",
  components: { WorkoutList }
};
</script>

<style scoped>
div {
  justify-items: left;
  text-align: left;
}
</style>
