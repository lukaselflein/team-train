<template>
  <div v-if="LOGGED_USER.team != null">
    <h4>{{ LOGGED_USER.team }}</h4>
  </div>
  <div v-else>
    <p>Not part of a team yet.</p>
    <b-button>Create Team</b-button>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserTeam",
  computed: {
    ...mapGetters(["LOGGED_USER"])
  }
};
</script>

<style lang="scss" scoped></style>
