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
    <!-- </b-navbar> -->
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
// default stylings for elements, fonts and background
#nav-coll {
  border-bottom: none;
}

* {
  margin: 0;
  padding: 0;
  font-family: "Mukata", sans-serif;

  html,
  body {
    margin: 0;
    border: none;
    padding: 0;
    overflow-x: hidden;
    // background-image: linear-gradient(-45deg, #9796f0, #fbc7d4);
    background-image: linear-gradient(145deg, #12c2e9, #c471ed, #f64f59);

    // background-image: url("./assets/background_studio.jpg");
    background-attachment: fixed;
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
    min-width: 100%;
    min-width: 100vw;

    #app {
      padding: 1em 1em 0em 1em;
      h1,
      h2,
      h3,
      h4,
      h5 {
        font-weight: bolder;
      }
      h1 {
        font-size: 1.5rem;
        color: $dark;
      }
      h2 {
        font-size: 1.2rem;
        color: $dark-title;
      }
      h3 {
        font-size: 0.94rem;
        color: white;
      }
      h4 {
        font-size: 1rem;
        color: $dark;
      }
      h5 {
        font-size: 0.94rem;
      }
      h6 {
        font-size: 0.81rem;
        color: $dark;
      }
      p {
        color: $dark;
        font-size: 0.8rem;
      }
      input {
        border-radius: 25px;
        border: 1px solid $dark-title;
        padding-left: 1.5em;
      }
      a {
        color: $greydark;
      }
      button {
        border-radius: 15px;
        border: none;
        // background-color: none;
        // opacity: 1;
      }
      // background-color: rgba($softlight, 0.5);
      background: fixed center center cover;
      min-height: 100vh;
    }
    li {
      list-style: none;
    }
  }
}

@media only screen and (min-width: 701px) {
  #app {
    background-size: 100vw;
  }
}
</style>
