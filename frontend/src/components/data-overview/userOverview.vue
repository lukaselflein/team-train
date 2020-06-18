<template>
  <div>
    <b-tab title="Ranking" active>
      <UserData />
      <UserChart />
    </b-tab>
    <b-card-footer>(dummy data)</b-card-footer>
  </div>
</template>

<script>
import UserData from "@/components/data-detail/userData.vue";
import UserChart from "@/components/data-detail/userChart.vue";

export default {
  name: "UserOverview",
  components: {
    UserData,
    UserChart
  }
};
</script>

<style scoped>
</style>
