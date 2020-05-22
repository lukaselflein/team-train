<template>
  <div class="exercise">
    <b-card :header="`Workout: ` + ONE_WORKOUT">
      {{ ONE_WORKOUT.name }}
      <b-carousel
        v-for="(item, index) in ONE_WORKOUT.exercises"
        :key="index"
        id="carousel-1"
        :interval="0"
        controls
        indicators
        >{{ item.name }}
        <b-carousel-slide>{{ ONE_WORKOUT }}</b-carousel-slide>
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