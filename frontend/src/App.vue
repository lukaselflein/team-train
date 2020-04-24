<template>
  <div id="app">
    <Navigation />
    <AppFooter />
    <router-view />
  </div>
</template>

<script>
// @ is an alias to /src
import appFooter from "@/components/layout/appFooter";
import Navigation from "@/components/layout/appNavbar";

export default {
  components: {
    AppFooter: appFooter,
    Navigation
  }
};
</script>

<style scoped></style>
