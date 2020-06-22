<template>
  <div>
    <b-tab title="Ranking" class="uppertab" active>
      <TeamTable class="tab" />
    </b-tab>
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
  border-radius: 20px;
}
</style>
