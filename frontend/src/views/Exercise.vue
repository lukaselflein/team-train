<template>
  <div class="exercise">
    <BackBtn />
    <b-card id="exercise-card" :title="ONE_WORKOUT.name"
      ><h6><Time v-bind:time="ONE_WORKOUT.time" /></h6>
      <p>by {{ ONE_WORKOUT.added_by }}</p>

      <b-row>
        <b-col>
          <h6>POINTS</h6>
          <div class="workout-points">
            <h4>{{ ONE_WORKOUT.points }}</h4>
          </div>
        </b-col>
        <b-col>
          <h6>ROUNDS</h6>
          <div class="workout-rounds">
            <h4>{{ ONE_WORKOUT.points }}</h4>
          </div>
        </b-col>
      </b-row>

      <div>
        <h6>DESCRIPTION</h6>
        <p>{{ ONE_WORKOUT.description }}</p>
        <b-card sub-title="exercises" id="exerciseListCard">
          <ExerciseList class="exerciseList" v-bind:id="id" />
          <b-button v-b-modal.modal-workout>start workout</b-button>
        </b-card>

        <CreatorTools
          v-bind:creatorTools="[ONE_WORKOUT.added_by, ONE_WORKOUT.id]"
        />
      </div>
    </b-card>

    <WorkoutModal v-bind:id="id" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import WorkoutModal from "@/components/layout/modalWorkout";
import BackBtn from "@/components/controls/backBtn";
import Time from "@/components/controls/timeConvert";
import ExerciseList from "@/components/data-list/exerciseList";
import CreatorTools from "@/components/controls/creator";

export default {
  name: "Exercise",
  components: {
    WorkoutModal,
    BackBtn,
    Time,
    ExerciseList,
    CreatorTools
  },
  data() {
    return {
      id: this.$route.params.id
    };
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"])
  },
  mounted() {
    this.$store.dispatch("GET_WORKOUT", this.id);
  }
};
</script>

<style scoped lang="scss">
@import "../mixins.scss";

.workout-points {
  @include square($alarm-title);
}
.workout-rounds {
  @include square($highlight);
}
.exercise {
  margin-top: 2em;
  padding: 1em;
  #exercise-card {
    @include cardstyle;
    text-align: center;
    margin: 1em auto;
  }
  #exerciseListCard {
    color: $dark-title;
    margin: 1em 0;
    @include cardstyle;
    .exerciseList {
      margin-top: 1.5em;
    }
  }
  button {
    margin: 0.5em;
  }
}
@media only screen and (min-width: 500px) {
  #exercise-card {
    max-width: 90%;
  }
}
@media only screen and (min-width: 700px) {
  #exercise-card {
    max-width: 80%;
  }
}
@media only screen and (min-width: 900px) {
  #exercise-card {
    max-width: 60%;
  }
}
</style>
