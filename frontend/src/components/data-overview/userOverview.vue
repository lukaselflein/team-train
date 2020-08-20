<template>
  <div>
    <div id="data-row">
      <UserScore />
      <UserPastTraining />
    </div>
    <h4>Overview</h4>
    <UserChart />
  </div>
</template>

<script>
import UserChart from "@/components/data-detail/userChart";
import UserScore from "@/components/data-detail/userScore";
import UserPastTraining from "@/components/data-detail/userPastTraining";

export default {
  name: "UserOverview",
  components: {
    UserChart,
    UserScore,
    UserPastTraining
  }
};
</script>

<style lang="scss" scoped>
#data-row {
  margin-top: 1em;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 0.5fr 0.5fr;
}
</style>
