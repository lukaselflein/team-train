<template>
  <div class="exercise">
    <router-link to="/workouts" id="backLink">back to workouts</router-link>
    <b-card
      id="outerCard"
      :title="ONE_WORKOUT.name"
      :sub-title="'points: ' + ONE_WORKOUT.points + ' / 100'"
      ><div>
        <b-card header="description" id="firstCard">
          <p>{{ ONE_WORKOUT.description }}</p>
        </b-card>
        <b-card header="exercises" id="sndCard">
          <!-- {{ workoutDetail }} -->
          <ul
            v-for="(item, index) in ONE_WORKOUT.exercises"
            :key="index"
            class="ex-list"
          >
            <li>
              <p>{{ index + 1 }}. {{ item.quantity }}x {{ item.name }}</p>
            </li>
          </ul>
        </b-card>
        <b-button v-b-modal.modal-workout variant="primary"
          >start workout</b-button
        >
      </div>
    </b-card>

    <WorkoutModal v-bind:id="id" />
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import WorkoutModal from "@/components/layout/modalWorkout";

export default {
  name: "Exercise",
  components: {
    WorkoutModal
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

.exercise {
  padding: 1em;
  #backLink {
    text-decoration: underline;
    cursor: pointer;
    color: $alarm-title;
    font-size: 1.2rem;
    font-weight: bold;
  }
  #outerCard {
    text-align: center;
    margin: 1em auto;
  }
  #firstCard,
  #sndCard {
    color: $dark-title;
    margin: 1em 0;

    ul {
      list-style: none;
      .ex-list {
        margin-left: auto;
        margin-right: auto;
        text-align: left;
      }
    }
    p {
      text-align: left;
    }
  }
  button {
    margin: 0.5em;
  }
}
@media only screen and (min-width: 500px) {
  #outerCard {
    max-width: 90%;
  }
}
@media only screen and (min-width: 700px) {
  #outerCard {
    max-width: 80%;
  }
}
@media only screen and (min-width: 900px) {
  #outerCard {
    max-width: 60%;
  }
}
</style>
