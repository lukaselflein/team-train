<template>
  <div>
    <b-table striped :items="items" :fields="fields"></b-table>
  </div>
</template>

<script>
export default {
  name: "TeamTable",
  data() {
    return {
      fields: ["Rank", "Teammember", "Points"],
      items: [
        { Rank: 1, Teammember: "Johan", Points: 50 },
        { Rank: 2 },
        { Rank: 3 },
        { Rank: 4 },
        { Rank: 5 }
      ]
    };
  }
};
</script>

<style scoped></style>
