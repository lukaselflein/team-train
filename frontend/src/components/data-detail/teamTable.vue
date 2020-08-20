<template>
  <div class="ranking">
    <b-table :items="LOGGED_USER.workouts" :fields="fields" id="tile">
      <template v-for="index in LOGGED_USER" v-slot:cell(Rank)="data">
        {{ data.index + 1 }}
      </template>
      <template v-for="index in LOGGED_USER" v-slot:cell(Teammember)="data">
        {{ data.name + 1 }}
      </template>
    </b-table>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "TeamTable",
  data() {
    return {
      fields: ["Rank", "Teammember", "Points"],
      items: []
      // [{ Rank: 1, Teammember: "Johan", Points: 20 }]
    };
  },
  computed: {
    ...mapGetters(["LOGGED_USER"])
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#tile {
  @include cardstyle;
  background-color: white;
}
@media only screen and (min-width: 700px) {
  .ranking {
    margin-top: 1em;
    @include centralPosition;
  }
}
</style>
