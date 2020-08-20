<template>
  <div class="navigation" id="nav-coll">
    <b-navbar fixed="top" toggleable="sm" small type="light" variant="light">
      <b-navbar-brand href="/">Train</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse">
        <template v-slot:default="{ expanded }">
          <b-icon v-if="expanded" icon="x-square"></b-icon>
          <b-icon v-else icon="grid"></b-icon>
        </template>
      </b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/stats">Statiscics</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
          <b-nav-item href="/workouts">Workouts</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
          <b-nav-item href="/new-workout">Create New Workout</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
          <b-nav-item href="/about">About Us</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item class="signout" @click="logout" right>
            Sign Out
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Navigation",
  methods: {
    logout: function() {
      this.$store.dispatch("LOGOUT").then(() => {
        this.$router.push("/login");
      });
    }
  }
};
</script>

<style scoped lang="scss">
.navigation {
  border-bottom: solid 1px black;
}
</style>
