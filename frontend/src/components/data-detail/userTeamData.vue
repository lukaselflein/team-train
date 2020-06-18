<template>
  <div>
    <b-list-group v-for="(team, index) in LOGGED_USER" :key="index">
      <!-- <b-list-group-item>{{ workout }}</b-list-group-item> -->
    </b-list-group>
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

<style></style>
