<template>
  <div>
    <!--  unnused -->
    <b-tab title="Ranking" active>
      <UserData />
      <UserChart />
    </b-tab>
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

<style scoped></style>
