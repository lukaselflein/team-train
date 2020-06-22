<template>
  <div>
    <p>ROLE</p>
    <div id="sq_role">
      <div v-if="LOGGED_USER.role">
        <h4>{{ LOGGED_USER.role }}</h4>
      </div>
      <div v-else><h4>no role</h4></div>
    </div>
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

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_role {
  @include square($light-title);
  width: 100%;
}
</style>
