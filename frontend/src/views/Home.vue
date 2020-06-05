<template>
  <div class="home">
    <!-- <WorkoutList /> -->
    <UserHome />
  </div>
</template>

<script>
// import axios from "axios";
import UserHome from "@/components/data-overview/userHome";

export default {
  name: "Home",
  components: {
    UserHome
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
