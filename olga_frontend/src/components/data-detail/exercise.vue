<template>
  <div class="exercise">
    <b-card :header="`Workout: ` + ONE_WORKOUT.name">
      {{ ONE_WORKOUT.exercises.length }}
      <b-carousel
        v-for="exercise in ONE_WORKOUT.exercises"
        :key="exercise.length"
        id="carousel-1"
        :interval="0"
        controls
        indicators
      >
        <b-carousel-slide>{{ exercise }}</b-carousel-slide>
      </b-carousel>
    </b-card>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Exercise",
  data() {
    return {
      id: this.$route.params.id,
      workout: []
    };
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"])
  },
  methods: {
    ...mapActions(["getWorkout"])
  },
  created() {
    this.getWorkout(this.id);
  }
};
</script>

<style>
</style>