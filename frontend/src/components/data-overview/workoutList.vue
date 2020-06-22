<template>
  <b-card id="trainingCard" title="TRAINING">
    <FilterButtons />
    <b-row>
      <b-card
        class="workoutcard"
        v-for="(item, index) in ALL_WORKOUTS"
        :key="index"
      >
        <div>
          <Time v-bind:time="item.time" />
          <!-- <h6>{{ convertTime(item.time) }}</h6> -->
          <h5>{{ item.name }}</h5>
          <h6>by {{ item.added_by }}</h6>
        </div>

        <b-row>
          <b-col>
            <h6>POINTS</h6>
            <div class="workout-points">
              <h4>{{ item.points }}</h4>
            </div>
          </b-col>
          <b-col>
            <div class="go-to" @click="startWorkout(item.id)">
              <h4>show</h4>
            </div>
          </b-col>
          <b-col>
            <h6>ROUNDS</h6>
            <div class="workout-rounds">
              <h4>{{ item.points }}</h4>
            </div>
          </b-col>
        </b-row>
      </b-card>
    </b-row>
  </b-card>
</template>

<script>
import { /*mapActions,*/ mapGetters } from "vuex";
import FilterButtons from "@/components/controls/filterButtons.vue";
import Time from "@/components/controls/timeConvert";

export default {
  name: "WorkoutList",

  components: {
    FilterButtons,
    Time
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
  text-align: center;
  padding-top: 1em;
  @include cardstyle;
  margin: 4em -0.5em 0 -1em;
  li {
    list-style: none;
  }
  .workoutcard {
    @include cardstyle;
    margin: 1em auto;
    width: 400px;
    max-height: 250px;

    .workout-points {
      @include square($alarm-title);
    }
    .workout-rounds {
      @include square($highlight);
    }
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

@media only screen and (min-width: 700px) {
  #trainingCard {
    .workoutcard {
      display: grid;
      grid-template-columns: repeat(1fr);
      grid-template-rows: repeat(1fr);
      column-gap: 10px;
      row-gap: 20px;
    }
  }
}
</style>
