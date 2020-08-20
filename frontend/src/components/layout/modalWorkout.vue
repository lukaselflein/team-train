<template>
  <!-- execution of excercises -->
  <div>
    <b-modal
      id="modal-workout"
      no-close-on-backdrop
      no-close-on-esc
      hide-header
      hide-header-close
    >
      <!-- body of modal -->
      <b-carousel id="carousel" :interval="0" controls no-wrap>
        <b-carousel-slide
          :background="carouselbg()"
          class="slides"
          img="./../../assets/all_background.jpg"
          ><div>
            <h1>Starting Workout {{ ONE_WORKOUT.name }}</h1>
          </div>
        </b-carousel-slide>
        <div v-for="(turn, rounds) in ONE_WORKOUT.rounds" :key="turn">
          <b-carousel-slide
            class="innerSlides"
            :background="carouselbg()"
            v-for="(item, index) in ONE_WORKOUT.exercises"
            :key="index"
          >
            <div id="progress-bar">
              <h2>ROUND {{ rounds + 1 }}</h2>
              <b-progress
                variant="danger"
                :value="rounds + 1"
                :max="ONE_WORKOUT.rounds"
              ></b-progress>
            </div>
            <div id="slide-content">
              <h1>{{ item.name }}</h1>
              <h3>{{ item.quantity }} rep</h3>
              <h5>description</h5>
              <h6>{{ item.description }}</h6>
            </div>
          </b-carousel-slide>
        </div>
        <b-carousel-slide class="slides" :background="carouselbg()">
          <div>
            <h2>Congrats! You successfully completed {{ ONE_WORKOUT.name }}</h2>
            <h4>Finish workout and get the points</h4>
            <ClaimWorkout v-bind:workout="ONE_WORKOUT.id" />
          </div>
        </b-carousel-slide>
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
import ClaimWorkout from "@/components/controls/claimBtn";

export default {
  name: "WorkoutModal",
  components: {
    ClaimWorkout
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      backg: "linear-gradient(145deg,carouselbg(), carouselbg())"
    };
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"])
  },
  mounted() {
    this.$store.dispatch("GET_WORKOUT", this.id);
  },
  methods: {
    carouselbg() {
      // random backgroundcolor
      let bg = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
      // let c2 = "#" + (((1 << 24) * Math.random()) | 0).toString(16);
      return bg;
    }
  }
};
</script>

<style scoped lang="scss">
@import "./../../mixins.scss";

#modal-workout {
  max-width: 100%;
  min-height: 100%;
  @include background;
  opacity: 40%;
  text-align: center;
  align-content: center;
  margin: 0;
  #carousel {
    background-color: black;
    min-width: 100%;
    min-height: 100%;

    .slides {
      min-height: 600px;
      position: relative;
      text-align: center;
      div {
        position: absolute;
        bottom: 10em;
      }
    }
    .innerSlides {
      min-height: 600px;
      position: relative;
      #progress-bar {
        top: -500px;
        width: 100%;
        position: absolute;
      }
      #slide-content {
        width: 100%;
        top: -300px;
        position: absolute;
        h5 {
          margin-top: 2em;
        }
        h6 {
          text-align: left;
          padding: 1em 1em;
          border: white 1px solid;
          border-radius: 10px;
        }
      }
    }
  }
}
@media only screen and (min-width: 700px) {
  .slides {
  }
}
@media only screen and (min-width: 1200px) {
  .card {
    min-width: 150%;
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
