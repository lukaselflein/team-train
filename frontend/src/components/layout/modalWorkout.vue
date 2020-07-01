<template>
  <div>
    <b-modal
      id="modal-workout"
      :title="ONE_WORKOUT.name"
      no-close-on-backdrop
      no-close-on-esc
      title-tag="h3"
      hide-header-close
    >
      <!-- body of modal -->
      <b-carousel
        id="carousel-no-animation"
        style="text-shadow: 0px 0px 2px #000"
        :interval="0"
        controls
        no-wrap
        img-height="480"
        img-width="1024"
      >
        <b-carousel-slide
          id="slides"
          v-for="(item, index) in ONE_WORKOUT.exercises"
          :key="index"
          ><b-progress
            :value="index + 1"
            :variant="variant"
            :max="ONE_WORKOUT.exercises.length"
            class="mb-3"
          ></b-progress>
          <h1>{{ item.name }}</h1>
          <h2>{{ item.quantity }}</h2></b-carousel-slide
        >
      </b-carousel>

      <!-- footer of modal -->
      <template v-slot:modal-footer>
        <b-button size="sm" variant="outline-danger" v-b-modal.modal-end>
          end training
        </b-button>
        <b-modal id="modal-end" size="sm" no-close-on-backdrop no-close-on-esc
          ><p>Are you sure you want to end the training here?</p>
          <template v-slot:modal-footer>
            <b-button variant="success" @click="$bvModal.hide('modal-end')"
              >resume really cool training</b-button
            >
            <b-button
              size="sm"
              variant="outline-danger"
              @click="$bvModal.hide('modal-workout')"
            >
              end training for real!
            </b-button>
          </template>
        </b-modal>
      </template>
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "WorkoutModal",
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      variant: "danger"
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
#modal-workout {
  text-align: center;
  min-width: 100vw;
  min-height: 100%;
  #slides {
    min-height: 500px;
  }
}
</style>
