<template>
  <div id="app">
    <div class="authcheck" v-if="IS_LOGGED_IN">
      <Navigation class="navi" />
      <router-view />
    </div>
    <div class="unAuth" v-else>
      <unNavigation />
      <router-view />
    </div>

    <AppFooter />
  </div>
</template>

<script>
// @ is an alias to /src
import appFooter from "@/components/layout/appFooter";
import Navigation from "@/components/layout/appNavbar";
import un_Navigation from "@/components/layout/appNavbar_unlogged";

export default {
  components: {
    AppFooter: appFooter,
    Navigation,
    unNavigation: un_Navigation
  },
  computed: {
    // check for authentification bearer token
    IS_LOGGED_IN: function() {
      return this.$store.getters.IS_LOGGED_IN;
    }
  }
};
</script>

<style>
body {
  overflow: auto;
}
</style>
