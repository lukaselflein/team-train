<template>
  <div>
    <b-tab title="My Training Data" active>
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

<style></style>
