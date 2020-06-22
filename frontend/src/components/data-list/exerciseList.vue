<template>
  <b-list-group>
    <ul
      class="exList"
      v-for="(exis, index) in ONE_WORKOUT.exercises"
      :key="index"
    >
      <li class="row">
        <b-col class="col">
          <p>{{ index + 1 }}.</p>
        </b-col>
        <b-col class="col">
          <p>{{ exis.name }}</p>
        </b-col>
        <b-col class="col">
          <p>x {{ exis.quantity }}</p>
        </b-col>
      </li>
    </ul>
  </b-list-group>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ExerciseList",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"])
  }
};
</script>

<style scoped lang="scss">
.exList {
  .row {
    text-align: left;
    display: grid;
    margin: 0 1em;
    grid-template-columns: 0.5fr 2fr 1fr;
  }
}
</style>
