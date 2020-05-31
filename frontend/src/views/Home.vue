<template>
  <div class="home">
    <!-- <WorkoutList /> -->
    <Statistic />
  </div>
</template>

<script>
// import axios from "axios";
import Statistic from "@/components/data-overview/statistic";

export default {
  name: "Home",
  components: {
    Statistic
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
