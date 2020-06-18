<template>
  <div id="content">
    <h1>Workouts</h1>
    <FilterButtons />
    <b-row>
      <b-card
        :sub-title="
          'by' +
            ' ' +
            ALL_WORKOUTS[index].added_by +
            ' on ' +
            convertTime(ALL_WORKOUTS[index].time)
        "
        class="cardy"
        v-for="(item, index) in ALL_WORKOUTS"
        :key="index"
      >
        <div class="workout-title">
          <h4>{{ item.name }}</h4>
          <p>({{ item.points }} Points)</p>
          <p>Description: {{ item.description }}</p>
        </div>

        <div class="workout-btn">
          <b-button
            size="sm"
            @click="startWorkout(item.id)"
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
      </b-card>
    </b-row>
  </div>
</template>

<script>
import { /*mapActions,*/ mapGetters } from "vuex";
import FilterButtons from "@/components/controls/filterButtons.vue";

export default {
  name: "WorkoutList",

  components: {
    FilterButtons
  },
  computed: {
    ...mapGetters(["ALL_WORKOUTS"])
  },
  mounted() {
    this.$store("GET_ALL_WORKOUTS");
  },
  methods: {
    // unix time convert
    convertTime(unix) {
      let timestamp = Date.parse(unix);
      let date = new Date(timestamp);
      const options = {
        weekday: "short",
        year: "numeric",
        month: "2-digit",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit"
      };
      return date.toLocaleString("en-US", options);
    },

    startWorkout(id) {
      this.$router.push("/workouts/" + id);
    },
    removeWorkout(id) {
      this.$store
        .dispatch("DELETE_WORKOUT", id)
        .then(() => {})
        .catch(err => {
          // alert("Workout was not deleted.");
          // eslint-disable-next-line no-console
          console.log(err);
        });
      this.$router.push("/workouts");
      // this.deleteWorkout(id);
      // // patch for state.workoutList undefined after creating new workout
    }
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
  li {
    list-style: none;
  }
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
