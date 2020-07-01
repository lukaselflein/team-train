<template>
  <!-- Landing page team data -->
  <div v-if="LOGGED_USER.team != null">
    <h3>{{ LOGGED_USER.team }}</h3>
  </div>
  <div v-else>
    <p>Not part of a team yet.</p>
    <b-button class="buttonstyle">Create Team</b-button>
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

<style lang="scss" scoped>
@import "../../mixins.scss";
.buttonstyle {
  @include btnstyle($dark-title);
}
</style>
