<template>
  <div>
    <b-list-group
      v-for="(role, index) in LOGGED_USER.user.memberOf"
      :key="index"
    >
      <b-list-group-item>{{ role }}</b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
// Role is not defined in JSON, needs to be corrected
import { mapGetters } from "vuex";

export default {
  name: "UserRole",
  computed: {
    ...mapGetters(["LOGGED_USER"])
  }
};
</script>

<style></style>
