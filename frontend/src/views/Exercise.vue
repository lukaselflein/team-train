<template>
  <!-- overview of a specific excercise -->
  <div class="exercise">
    <BackBtn />
    <!-- <b-card id="exercise-card" :title="ONE_WORKOUT.name"> -->
    <div class="card">
      <h1>{{ ONE_WORKOUT.name }}</h1>
      <h6><Time v-bind:time="ONE_WORKOUT.time" /></h6>
      <p>by {{ ONE_WORKOUT.added_by }}</p>

      <b-row class="btnrw">
        <!-- Workout Points Information -->
        <b-col class="coli">
          <WorkoutPoints v-bind:item="ONE_WORKOUT.points" />
        </b-col>
        <!-- start workout-->
        <b-col class="coli">
          <b-button v-b-modal.modal-workout variant="success"
            >start workout</b-button
          >
        </b-col>
        <!-- Workout Rounds Information -->
        <b-col class="coli">
          <WorkoutRounds v-bind:item="ONE_WORKOUT.rounds" />
        </b-col>
      </b-row>
      <div>
        <!-- Workout Description Information -->
        <WorkoutDescription v-bind:item="ONE_WORKOUT.description" />
        <!-- excercise List -->
        <b-card title="exercises" id="exerciseListCard">
          <ExerciseList class="exerciseList" v-bind:id="id" />
          <!-- claim workout points -->
          <b-btn v-b-modal.modal-claim variant="primary"
            >get workout points</b-btn
          >
        </b-card>
        <!-- Change or Delete Workout, only shown, if logged User = creator -->
        <CreatorTools
          v-bind:creatorTools="[ONE_WORKOUT.added_by, ONE_WORKOUT.id]"
        />
      </div>
    </div>
    <!-- </b-card> -->

    <!-- alter or delete workout -- only visible for workout creator -->
    <b-modal id="modal-claim" title="Get Points" hide-header-close>
      <h5>
        You have already done this workout and forgot to claim the points?
      </h5>

      <template v-slot:modal-footer>
        <b-button size="sm" @click="$bvModal.hide('modal-claim')">
          cancel
        </b-button>
        <b-button variant="outline-success" @click="claimPoints(ONE_WORKOUT.id)"
          >get points</b-button
        >
      </template>
    </b-modal>
    <!-- workout execution here -->
    <WorkoutModal v-bind:id="id" />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import WorkoutModal from "@/components/layout/modalWorkout";
import BackBtn from "@/components/controls/backBtn";
import Time from "@/components/controls/timeConvert";
import ExerciseList from "@/components/data-list/exerciseList";
import CreatorTools from "@/components/controls/creator";
import WorkoutPoints from "@/components/workout-detail/workoutPoints";
import WorkoutRounds from "@/components/workout-detail/workoutRounds";
import WorkoutDescription from "@/components/workout-detail/workoutDescription";

export default {
  name: "Exercise",
  components: {
    WorkoutModal,
    BackBtn,
    Time,
    ExerciseList,
    CreatorTools,
    WorkoutPoints,
    WorkoutRounds,
    WorkoutDescription
  },
  data() {
    return {
      id: this.$route.params.id
    };
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"]),
    ...mapActions(["CLAIM_SCORE"])
  },
  mounted() {
    this.$store.dispatch("GET_WORKOUT", this.id);
  },
  methods: {
    // unauthorized 401 error
    claimPoints(id) {
      this.$store
        .dispatch("CLAIM_SCORE", id)
        .then(() => {
          this.$router.push("/workouts");
        })
        .catch(err => {
          // eslint-disable-next-line no-console
          console.log(err);
        });
    }
  }
};
</script>

<style scoped lang="scss">
@import "../mixins.scss";

.card {
  @include background;
  margin: 1em auto;
  .btnrw {
    display: flex;
    .coli {
      flex-grow: 1fr 2fr 1fr;
    }
  }
}
.workout-points {
  @include square($alarm-title);
}
.workout-rounds {
  @include square($highlight);
}
.exercise {
  margin-top: 2em;
  padding: 1em;

  #exerciseListCard {
    background-color: white;
    .exerciseList {
      margin-top: 1.5em;
    }
  }
  button {
    margin: 0.5em;
  }
}
@media only screen and (min-width: 600px) {
  .card {
    width: 80%;
  }
  #exerciseListCard {
    width: 90%;
  }
}
@media only screen and (min-width: 700px) {
  .card {
    width: 70%;
  }
}
@media only screen and (min-width: 1200px) {
  .card {
    width: 50%;
  }
}
@media only screen and (min-width: 1200px) {
  .card {
    width: 40%;
  }
}

@media only screen and (min-width: 1500px) {
  .card {
    width: 30%;
  }
}
@media only screen and (min-width: 2000px) {
  .card {
    width: 20%;
  }
}
</style>
