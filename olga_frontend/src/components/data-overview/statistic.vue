<template>
  <div class="tab-container">
    <b-tabs
      align="center"
      class="tab-nav"
      active-nav-item-class="font-weight-bold"
    >
      <UserOverview />
      <TeamOverview />
    </b-tabs>
  </div>
</template>

<script>
import UserOverview from "@/components/data-overview/userOverview.vue";
import TeamOverview from "@/components/data-overview/teamOverview.vue";
export default {
  name: "Statistic",
  components: {
    UserOverview,
    TeamOverview
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.tab-container {
  .tab-nav {
    @include background;
  }
}
</style>
