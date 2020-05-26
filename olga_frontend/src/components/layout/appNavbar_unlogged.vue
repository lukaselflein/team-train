<template>
  <div class="navigation">
    <b-navbar fixed="top" toggleable="lg" type="light" variant="light">
      <b-navbar-brand href="/">Train</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse">
        <template v-slot:default="{ expanded }">
          <b-icon v-if="expanded" icon="x-square"></b-icon>
          <b-icon v-else icon="grid"></b-icon>
        </template>
      </b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/about">Über uns</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item right href="/signup">
            Sign Up
          </b-nav-item>

          <!-- Right aligned nav items -->

          <b-nav-item right href="/login">
            Login
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "un_Navigation",
  data: function() {
    return {
      isActive: false
    };
  }
};
</script>

<style>
.navigation {
  border-bottom: solid 1px black;
}
</style>
