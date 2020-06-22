<template>
  <!-- container for Landing Page - overview of user score and data -->
  <div class="home">
    <b-card
      id="upperCard"
      title="OVERVIEW"
      :sub-title="'logged in as ' + LOGGED_USER.username"
    >
      <b-card sub-title="Team" class="cards">
        <UserTeam />
        <b-row
          ><b-col>
            <UserRank />
          </b-col>
          <b-col>
            <UserScore />
          </b-col>
        </b-row>
        <a href="/stats">go to team statistics</a>
      </b-card>
      <b-card class="cards" sub-title="Training">
        <b-row>
          <b-col>
            <UserRole />
          </b-col>
          <b-col>
            <UserPastTraining />
          </b-col>
        </b-row>
        <b-col>
          <p>STATISTICS</p>
          <userChart />
        </b-col>
        <a href="/stats">go to user statistics</a>
      </b-card>
    </b-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UserTeam from "@/components/data-detail/userTeamData";
import UserScore from "@/components/data-detail/userScore";
import UserRole from "@/components/data-detail/userRoleData";
import UserChart from "@/components/data-detail/userChart";
import UserRank from "@/components/data-detail/userRanking";
import UserPastTraining from "@/components/data-detail/userPastTraining";

export default {
  name: "UserHome",
  components: {
    UserChart,
    UserTeam,
    UserRole,
    UserScore,
    UserRank,
    UserPastTraining
  },
  computed: {
    ...mapGetters(["LOGGED_USER"])
  },
  mounted() {
    this.$store.dispatch("WHOAMI");
  }
};
</script>

<style lang="scss" scoped>
@import "../mixins.scss";
.home {
  text-align: center;
  padding-top: 3.5em;
  padding-bottom: 3.5em;
  min-height: 100vh;

  #upperCard {
    padding-top: 1em;
    @include cardstyle;

    .cards {
      margin: 2em auto;
      @include cardstyle;
    }
    a {
      text-decoration: underline;
    }
  }
}
</style>
