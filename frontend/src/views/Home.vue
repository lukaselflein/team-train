<template>
  <!-- container for Landing Page - overview of user score and data -->
  <div class="home">
    <div id="upperCard">
      <!-- <b-card
      id="upperCard"
      title="OVERVIEW"
      :sub-title="'logged in as ' + LOGGED_USER.username"
    > -->
      <h1>OVERVIEW</h1>
      <h5>logged in as {{ LOGGED_USER.username }}</h5>
      <a href="/workouts">
        <b-btn id="trainingLink" variant="success"> go to Trainings</b-btn></a
      >
      <b-row>
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
          <a href="/stats" v-bind:activeTab="team">go to rank list</a>
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
          <b-row>
            <b-col>
              <p>STATISTICS</p>
              <userChart />
            </b-col>
          </b-row>
        </b-card>
      </b-row>
      <!-- </b-card> -->
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UserTeam from "@/components/data-detail/userTeamData";
import UserRank from "@/components/data-detail/userRanking";
import UserScore from "@/components/data-detail/userScore";
import UserRole from "@/components/data-detail/userRoleData";
import UserChart from "@/components/data-detail/userChart";
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
  data() {
    return {
      user: "user",
      team: "team"
    };
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
  padding: 3em 0 2em 0;
  min-height: 100%;
  border: none;
  #upperCard {
    justify-content: center;
    @include background;

    #trainingLink {
      margin: 0.5em auto;
    }
    .cards {
      width: 90%;
      margin: 0.5em auto;
      @include cardplain;
      padding: 0;
    }
    a {
      text-decoration: underline;
    }
  }
}
@media only screen and (min-width: 700px) {
  .home {
    margin: 1em auto;
    #upperCard {
      .cards {
        max-width: 45%;
        margin: 1em auto;
      }
    }
  }
}
</style>
