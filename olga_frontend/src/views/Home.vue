<template>
  <div class="home">
    <createWorkout class="newWK" />
    <WorkoutList />
  </div>
</template>

<script>
// import axios from "axios";
import ModalWorkout from "@/components/layout/modalWorkout";
import WorkoutList from "@/components/data-overview/workoutList";

export default {
  name: "Home",
  components: {
    createWorkout: ModalWorkout,
    WorkoutList
  }
};
</script>

<style scoped>
.home {
  text-align: center;
  padding: 1em;
}
.newWK {
  margin-top: 3.5em;
  margin-bottom: 2em;
}
</style>
