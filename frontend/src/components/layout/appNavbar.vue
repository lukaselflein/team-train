<template>
  <div>
    <b-navbar fixed="top" toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="/">Train</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/">My Workouts</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
          <b-nav-item href="/about">Über uns</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item @click="logout" right>
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

<style>
.navbar {
  border-bottom: solid 1px black;
}
</style>
