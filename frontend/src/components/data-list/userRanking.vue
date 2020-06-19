<template>
  <div>
    <b-tab title="Ranking" active>
      <TeamTable class="tab" />
    </b-tab>
    <!-- <b-card-footer>(dummy data)</b-card-footer> -->
  </div>
</template>

<script>
import TeamTable from "@/components/data-detail/teamTable.vue";

export default {
  name: "UserRanking",
  components: {
    TeamTable
  }
};
</script>

<style scoped>
.tab {
  margin-top: 1em;
}
</style>