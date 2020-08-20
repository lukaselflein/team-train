<template>
  <b-button variant="success" @click="claimPoints(workout)"
    >get points</b-button
  >
</template>

<script>
export default {
  name: "ClaimWorkout",
  methods: {
    // unauthorized 401 error
    claimPoints(id) {
      this.$store
        .dispatch("CLAIM_SCORE", id)
        .then(() => {
          this.$router.push("/");
        })
        .catch(err => {
          // eslint-disable-next-line no-console
          console.log(err);
        });
    }
  },
  props: {
    workout: {
      type: String,
      required: true
    }
  }
};
</script>

<style>
</style>