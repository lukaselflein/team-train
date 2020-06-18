<template>
  <!-- container for Landing Page - overview of user score and data -->
  <div>
    <b-card
      id="upperCard"
      title="OVERVIEW"
      :sub-title="'logged in as ' + LOGGED_USER"
    >
      <b-card sub-title="Team" class="cards">
        <h5>{{ LOGGED_USER }}</h5>
        <div v-if="LOGGED_USER != ''">
          <UserTeam />
        </div>
        <div v-else>
          <p>Not part of a team yet.</p>
          <b-button>Create Team</b-button>
        </div>
        <b-row
          ><b-col>
            <p>POSITION</p>
            <div id="sq_position">
              <h4>#1</h4>
            </div>
          </b-col>
          <b-col>
            <p>SCORE</p>
            <div id="sq_score">
              <h4>12</h4>
            </div>
          </b-col>
        </b-row>
        <a href="/stats">go to team statistics</a>
      </b-card>

      <b-card class="cards" sub-title="Training">
        <b-row
          ><b-col>
            <p>ROLE</p>
            <div id="sq_role">
              <h4>???</h4>
            </div>
            <div v-if="LOGGED_USER">
              <UserRole />
            </div>
            <div v-else><p>No Roles assigned</p></div>
          </b-col>
          <b-col>
            <p>DONE TRAININGS</p>
            <div id="sq_past">
              <h4>14</h4>
            </div>
            <div v-if="LOGGED_USER">
              <b-list-group
                v-for="(workout, index) in LOGGED_USER"
                :key="index"
              >
                <!-- <b-list-group-item>{{ workout }}</b-list-group-item> -->
              </b-list-group>
            </div>
            <div v-else><p>No Workouts created</p></div>
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
import UserRole from "@/components/data-detail/userRoleData";
import UserChart from "@/components/data-detail/userChart";

export default {
  name: "UserHome",
  components: {
    UserChart,
    UserTeam,
    UserRole
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
@import "../../mixins.scss";
#upperCard {
  padding-top: 1em;
  .cards {
    margin: 2em auto;
  }
  a {
    text-decoration: underline;
  }
  #sq_position,
  #sq_score,
  #sq_role,
  #sq_past {
    @include square;
  }
  #sq_position {
    background-color: $dark;
    box-shadow: shade($dark);
  }
  #sq_score {
    background-color: $alarm-title;
    box-shadow: shade($alarm-title);
  }
  #sq_role {
    background-color: $light-title;
    box-shadow: shade($light-title);
    width: 100%;
  }
  #sq_past {
    background-color: $dark-title;
    box-shadow: shade($dark-title);
  }
}
</style>
