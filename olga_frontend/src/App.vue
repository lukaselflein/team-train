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

    <!-- <AppFooter /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import appFooter from "@/components/layout/appFooter";
import Navigation from "@/components/layout/appNavbar";
import un_Navigation from "@/components/layout/appNavbar_unlogged";

export default {
  components: {
    // AppFooter: appFooter,
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

<style lang="scss">
@import "./mixins.scss";

* {
  margin: 0;
  padding: 0;
  font-family: "Mukata", sans-serif;

  html {
    overflow: auto;
  }
  html,
  body {
    margin: 0;
    border: none;
    padding: 0;
    min-width: 100%;
    #app {
      h1,
      h2,
      h3,
      h4 {
        font-weight: bolder;
        color: $dark;
      }
      p {
        color: $dark;
        font-size: 1em;
      }
      input {
        border-radius: 25px;
        border: 1px solid $dark-title;
        // box-shadow: inset 0px 0px 10px $light-title;
        padding-left: 1.5em;
      }
      button {
        border-radius: 25px;
        border: none;
        background-color: none;
        opacity: 1;
      }

      background-image: url("./assets/background_studio.jpg");
      background-attachment: fixed;
      background-position: center;
      background-size: cover;
      min-width: 100%;
      min-height: 100vh;
      min-width: 100vw;
    }
  }
}

@media only screen and (min-width: 701px) {
  #app {
    background-size: 100vw;
  }
}
</style>
