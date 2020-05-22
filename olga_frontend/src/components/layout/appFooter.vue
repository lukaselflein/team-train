<template>
  <div class="appFooter">
    <b-navbar
      class="foo"
      fixed="bottom"
      toggleable="sm"
      type="light"
      variant="light"
      ><b-list-group v-for="author in authors" :key="author.name">
        {{ author.name }}
      </b-list-group>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "appFooter",
  data() {
    return {
      authors: [{ name: "Linus" }, { name: "Lukas" }, { name: "Olga" }]
    };
  }
};
</script>

<style>
.appFooter {
}
.foo {
  text-align: center;
}
</style>