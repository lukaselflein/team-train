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
        <b-col v-if="exis.description">
          <b-icon id="info" v-b-modal.modal-info icon="question-circle-fill">
          </b-icon>
        </b-col>
        <b-modal
          :title="exis.name + ' description'"
          size="sm"
          hide-header-close
          centered
          ok-only
          id="modal-info"
        >
          <p>{{ exis.description }}</p></b-modal
        >
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
    margin: 0 0.2em;
    grid-template-columns: 1fr 5fr 3fr 1fr;
  }
}
</style>
