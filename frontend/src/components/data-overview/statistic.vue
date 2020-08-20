<template>
  <b-card title="TEAM OVERVIEW" class="overviewTab">
    <b-tabs
      align="center"
      class="tab"
      active-nav-item-class="font-weight-bold text-dark"
    >
      <div>
        {{ activeTab }}
        <b-tab title="Ranking" :active="activeA">
          <TeamTable class="rankTab" />
        </b-tab>
        <b-tab title="My Stats" :active="activeB">
          <UserOverview />
        </b-tab>
        <div v-if="LOGGED_USER.role == 'owner'">
          <b-tab title="Team" class="teamTab">
            <TeamOverview />
          </b-tab>
        </div>
      </div>
    </b-tabs>
  </b-card>
</template>

<script>
import { mapGetters } from "vuex";

import TeamTable from "@/components/data-detail/teamTable.vue";
import TeamOverview from "@/components/data-overview/teamOverview";
import UserOverview from "@/components/data-overview/userOverview";
export default {
  name: "Statistic",
  components: {
    TeamOverview,
    UserOverview,
    TeamTable
  },
  data() {
    return {
      activeA: false,
      activeB: false
    };
  },
  props: {
    activeTab: {
      type: String
      // required: true
    }
  },
  computed: {
    ...mapGetters(["LOGGED_USER"])
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
    min-width: 100%;
    margin-top: 1em;
    border-radius: 20px;
  }
}
@media only screen and (min-width: 700px) {
  .overviewTab {
    @include centralPosition;
  }
}
</style>
