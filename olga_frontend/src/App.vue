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

<style scoped>
* {
  font-family: "Red Hat Display", sans-serif;
}
html {
  overflow: auto;
}
html,
body {
  margin: 0;
  border: none;
  padding: 0;
  min-width: 100%;
}
#app {
  margin: 0;
  padding: 0;
  background-image: url("./assets/background_studio.jpg");
  /* background-repeat: repeat-y; */
  /* background-size: 100vh; */
  background-attachment: fixed;
  background-position: center;
  background-size: cover;
  /* background-color: cadetblue; */
  min-width: 100%;
  /* height: 100vh; */
  /* max-height: 100%; */
}

@media only screen and (min-width: 701px) {
  #app {
    background-size: 100vw;
  }
}
</style>
