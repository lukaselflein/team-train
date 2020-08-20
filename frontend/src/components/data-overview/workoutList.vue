<template>
  <!-- <b-card id="trainingCard" title="TRAINING"> -->
  <div id="trainingCard">
    <h1>TRAINING</h1>
    <a href="/new-workout">
      <b-btn variant="success">create workout</b-btn>
    </a>
    <!-- <FilterButtons /> -->
    <b-row>
      <!-- every single Workout in Workoutoverview -->
      <b-card
        class="workoutcard"
        v-for="(item, index) in ALL_WORKOUTS"
        :key="index"
      >
        <!-- Workout Information Name and Time -->
        <div>
          <Time v-bind:time="item.time" />
          <h2>{{ item.name }}</h2>
          <h6>by {{ item.added_by }}</h6>
        </div>

        <b-row>
          <!-- Workout Points Information -->
          <b-col>
            <WorkoutPoints v-bind:item="item.points" />
          </b-col>
          <!-- Start workout Button -->
          <b-col>
            <div class="go-to" @click="startWorkout(item.id)">
              <h3>show</h3>
            </div>
          </b-col>
          <!-- Workout Rounds Information -->
          <b-col>
            <WorkoutRounds v-bind:item="item.rounds" />
          </b-col>
        </b-row>
      </b-card>
    </b-row>
  </div>
  <!-- </b-card> -->
</template>

<script>
import { /*mapActions,*/ mapGetters } from "vuex";
// import FilterButtons from "@/components/controls/filterButtons.vue";
import Time from "@/components/controls/timeConvert";
import WorkoutPoints from "@/components/workout-detail/workoutPoints";
import WorkoutRounds from "@/components/workout-detail/workoutRounds";

export default {
  name: "WorkoutList",

  components: {
    // FilterButtons,
    Time,
    WorkoutPoints,
    WorkoutRounds
  },
  computed: {
    ...mapGetters(["ALL_WORKOUTS"])
  },
  mounted() {
    this.$store.dispatch("GET_ALL_WORKOUTS");
  },
  methods: {
    startWorkout(id) {
      this.$router.push("/workouts/" + id);
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";
#trainingCard {
  // @include cardstyle;
  @include background;
  padding-left: 1em;

  margin: 3em 0em 2em 0em;
  li {
    list-style: none;
  }
  .workoutcard {
    @include cardstyle;
    margin-top: 1em;
    margin-left: auto;
    margin-right: auto;
    max-height: 250px;
    width: 90%;
    .go-to {
      @include square($somegreen);
      margin-top: 1em;
      padding: 0.5em;
      height: 70%;
      width: 100%;
      cursor: pointer;
    }
  }
}

@media only screen and (min-width: 600px) {
  #trainingCard {
    .workoutcard {
      display: grid;
      grid-template-columns: repeat(1fr 1fr);
      grid-template-rows: repeat(1fr 1fr);
      column-gap: 10px;
      row-gap: 20px;
      width: 45%;
      grid-auto-flow: column;
    }
  }
}
@media only screen and (min-width: 900px) {
  #trainingCard {
    .workoutcard {
      grid-template-columns: repeat(1fr 1fr 1fr);
      grid-template-rows: repeat(1fr);

      max-width: 33%;
      grid-auto-flow: column;
    }
  }
  @media only screen and (min-width: 1200px) {
    #trainingCard {
      .workoutcard {
        // grid-template-columns: repeat(1fr 1fr 1fr 1fr);
        max-width: 25%;
        grid-auto-flow: column;
      }
    }
  }
  @media only screen and (min-width: 1400px) {
    #trainingCard {
      .workoutcard {
        // grid-template-columns: repeat(1fr 1fr 1fr 1fr 1fr);
        max-width: 20%;
        grid-auto-flow: column;
      }
    }
  }
  @media only screen and (min-width: 1800px) {
    #trainingCard {
      .workoutcard {
        // grid-template-columns: repeat(1fr 1fr 1fr 1fr 1fr 1fr);
        max-width: 20%;
        grid-auto-flow: column;
      }
    }
  }
}
</style>
