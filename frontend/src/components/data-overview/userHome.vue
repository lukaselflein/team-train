<template>
  <div>
    <b-card sub-title="logged in as"
      ><h4>{{ LOGGED_USER.user.name }}</h4>
      <b-row>
        <h5>Team:</h5>
        <div v-if="LOGGED_USER.user.memberOf != ''">
          <UserTeam />
        </div>
        <div v-else>
          <p>Not part of a team yet.</p>
          <b-button>Create Team</b-button>
        </div>
      </b-row>
      <b-row>
        <h5>Role:</h5>
        <div v-if="LOGGED_USER.user.roles">
          <UserRole />
        </div>
        <div v-else><p>No Roles assigned</p></div></b-row
      >

      <b-row>
        <h5>created Workouts:</h5>
        <div v-if="LOGGED_USER.user.ownerOf">
          <b-list-group
            v-for="(workout, index) in LOGGED_USER.user.ownerOf"
            :key="index"
          >
            <b-list-group-item>{{ workout }}</b-list-group-item>
          </b-list-group>
        </div>
        <div v-else><p>No Workouts created</p></div></b-row
      >
    </b-card>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import UserTeam from "@/components/data-detail/userTeamData";
import UserRole from "@/components/data-detail/userRoleData";
export default {
  name: "UserHome",
  components: {
    UserTeam,
    UserRole
  },
  computed: {
    ...mapGetters(["LOGGED_USER"])
  },
  methods: {
    ...mapActions(["getWorkout"])
  }
};
</script>

<style></style>
