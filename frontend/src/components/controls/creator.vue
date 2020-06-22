<template>
  <div v-if="creatorTools[0] == LOGGED_USER.username">
    <b-row id="creatorBtn">
      <b-col>
        <b-button v-b-modal.alterWorkout variant="info"
          >change Workout</b-button
        >
      </b-col>
      <b-col>
        <b-btn variant="danger" @click="deleteWorkout(creatorTools[1])"
          >delete Workout</b-btn
        >
      </b-col>
    </b-row>

    <!-- modal change workout -->
    <ModalChangeWorkout />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import ModalChangeWorkout from "@/components/layout/modalChangeWorkout";

export default {
  name: "CreatorTools",
  components: {
    ModalChangeWorkout
  },
  props: {
    creatorTools: {
      type: Array,
      required: true
    }
  },
  computed: {
    ...mapGetters(["LOGGED_USER", "ALL_WORKOUTS"]),
    ...mapActions(["DELETE_WORKOUT"])
  },
  methods: {
    deleteWorkout(id) {
      this.$store
        // call action from store "login"
        .dispatch("DELETE_WORKOUT", id)
        .then(() => {
          this.$router.push("/workouts");
        })
        .catch(err => {
          this.$router.push("/workouts");
          // eslint-disable-next-line no-console
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
#creatorBtn {
}
</style>
