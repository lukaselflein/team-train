<template>
  <b-card title="TEAM OVERVIEW" class="overviewTab">
    <b-tabs
      align="center"
      class="tab"
      active-nav-item-class="font-weight-bold text-dark"
    >
      <UserRanking />
      <TeamOverview />
    </b-tabs>
  </b-card>
</template>

<script>
import UserRanking from "@/components/data-list/userRanking.vue";
import TeamOverview from "@/components/data-overview/teamOverview.vue";
export default {
  name: "Statistic",
  components: {
    UserRanking,
    TeamOverview
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.overviewTab {
  @include cardstyle;
  text-align: center;
  padding-top: 1em;
  margin-top: 4em;
  .tab {
    padding-top: 1em;
  }
}
</style>
