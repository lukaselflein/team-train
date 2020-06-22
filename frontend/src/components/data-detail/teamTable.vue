<template>
  <div>
    <b-table :items="items" :fields="fields" id="tile"></b-table>
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

<style lang="scss" scoped>
@import "../../mixins.scss";

#tile {
  @include cardstyle;
  background-color: white;
}
</style>
