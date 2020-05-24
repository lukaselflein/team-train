<template>
  <div class="home">
    <!-- <createWorkout class="newWK" /> -->
    <WorkoutList />
  </div>
</template>

<script>
// import axios from "axios";
// import ModalWorkout from "@/components/layout/modalWorkout";
import WorkoutList from "@/components/data-overview/workoutList";

export default {
  name: "Home",
  components: {
    // createWorkout: ModalWorkout,
    WorkoutList
  }
};
</script>
<style scoped></style>

<style scoped>
.home {
  text-align: center;
  padding-top: 3.5em;
  padding-bottom: 3.5em;
  min-height: 100vh;
}
</style>
