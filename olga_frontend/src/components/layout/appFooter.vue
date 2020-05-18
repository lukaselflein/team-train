<template>
  <div class="appFooter">
    <footer>
      <li v-for="author in authors" :key="author.id">{{ author }}</li>
    </footer>
  </div>
</template>

<script>
export default {
  name: "appFooter",
  data() {
    return {
      authors: {
        item1: "Linus",
        item2: "Lukas",
        item3: "Olga"
      }
    };
  }
};
</script>

<style>
.appFooter {
  position: fixed;
  text-align: center;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 1.5rem;
  border-top: 1px solid black;
  font-size: 0.75rem;
  background-color: white;
}
footer {
  padding: 0.25em;
}
footer li {
  list-style: none;
  display: inline;
  padding: 1em;
}
</style>