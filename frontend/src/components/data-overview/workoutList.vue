<template>
  <div id="content">
    <h1>Workouts</h1>
    <FilterButtons />
    <b-row>
      <b-card
        sub-title="added by"
        class="cardy"
        v-for="(item, index) in ALL_WORKOUTS"
        :key="index"
      >
        <b-row>
          <p>{{ ALL_WORKOUTS[index].added_by }} at</p>
          <p>{{ convertTime(ALL_WORKOUTS[index].time) }}</p>
        </b-row>
        <div class="workout-title">
          <h4>{{ item.name }}</h4>
          <p>({{ item.points }} Points)</p>
        </div>

        <div class="workout-content">
          <div class="exercise-list">
            <ul
              v-for="(exercise, number) in ALL_WORKOUTS[index].exercises"
              :key="number"
            >
              <li v-if="number <= 2">
                - {{ exercise.name }} x {{ exercise.quantity }}
              </li>
            </ul>
            <p
              v-if="ALL_WORKOUTS[index].exercises.length > 2"
              @click="showModal(item)"
            >
              ... show more
            </p>
          </div>
          <div class="workout-btn">
            <b-button
              size="sm"
              @click="startWorkout(item._id)"
              class="mr-1"
              variant="success"
            >
              Go to
            </b-button>
            <b-button
              disabled
              class="mr-1"
              variant="info"
              size="sm"
              @click="nothing()"
              >change
            </b-button>
            <b-button
              size="sm"
              @click="removeWorkout(item.id)"
              class="mr-1"
              variant="danger"
            >
              Delete
            </b-button>
          </div>
        </div>
      </b-card>
    </b-row>

    <b-modal ref="my-modal" hide-footer title="Workout">
      <h5>{{ modaldata.name }}</h5>
      <ul v-for="(ex, index) in modaldata.exercises" :key="index">
        <li>- {{ ex.name }} x {{ ex.quantity }}</li>
      </ul>
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import FilterButtons from "@/components/controls/filterButtons.vue";

export default {
  name: "WorkoutList",
  data() {
    return {
      modaldata: {}
    };
  },
  components: {
    FilterButtons
  },
  computed: {
    ...mapGetters(["ALL_WORKOUTS"])
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.ALL_WORKOUTS.length;
  },
  methods: {
    ...mapActions(["getAllWorkouts", "getWorkout", "deleteWorkout"]),

    convertTime(unix) {
      let timestamp = Date.parse(unix);
      let newTime = new Date(timestamp * 1000);
      const options = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
      };

      return newTime.toLocaleDateString("en-US", options);
      // expected output: Donnerstag, 20. Dezember 2012
    },

    startWorkout(id) {
      this.$router.push("/workouts/" + id);
    },
    showModal(index) {
      this.modaldata = index;
      // alert(this.modaldata);
      this.$refs["my-modal"].show();
    },

    removeWorkout(id) {
      /* eslint-disable-next-line*/
      console.log(id);
      this.deleteWorkout(id);
      // // patch for state.workoutList undefined after creating new workout
      // window.location.reload();
      this.getAllWorkouts();
    }
  },
  created() {
    this.getAllWorkouts();
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";
#content {
  text-align: left;
  padding-top: 1em;
  // text-align: center;
  margin: auto;
  .cardy {
    margin: 1em auto;
    min-width: 400px;
    max-height: 400px;
  }
}

@media only screen and (min-width: 700px) {
  #content {
    .cardy {
      display: grid;
      grid-template-columns: repeat(1fr);
      grid-template-rows: repeat(1fr);
      column-gap: 10px;
      row-gap: 20px;
    }
  }
}
</style>
