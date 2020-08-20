<template>
  <div>
    <b-modal id="alterWorkout" title="Change Workout">
      <b-form class="change-form" @submit="onSubmit" @reset="onReset">
        <!-- change Workout Name -->
        <b-form-group
          id="change-name"
          label="Workout Name:"
          label-for="change-name-input"
        >
          <b-form-input
            id="change-name-input"
            v-model="form.name"
            :placeholder="ONE_WORKOUT.name"
          ></b-form-input>
        </b-form-group>
        <!-- Workout description -->
        <b-form-group
          id="change-description"
          label="Workout Description:"
          label-for="change-description-input"
        >
          <b-form-textarea
            id="change-description-input"
            type="text"
            max-rows="6"
            :placeholder="ONE_WORKOUT.description"
            v-model="form.description"
            title="Enter a description of yout Workout"
          ></b-form-textarea>
        </b-form-group>
        <b-row>
          <b-col>
            <!-- Workout Points -->
            <b-form-group
              id="change-points"
              label="Points:"
              label-for="change-points-input"
            >
              <b-form-input
                id="change-points-input"
                type="number"
                min="0.00"
                max="100.01"
                v-model="form.points"
                :placeholder="ONE_WORKOUT.points.toString()"
                title="Difficulty level from 0-100"
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col>
            <!-- Workout Rounds -->
            <b-form-group
              id="change-rounds"
              label="Rounds:"
              label-for="change-rounds-input"
            >
              <b-form-input
                id="change-rounds-input"
                type="number"
                min="1.00"
                max="100.01"
                v-model="form.rounds"
                :placeholder="ONE_WORKOUT.rounds.toString()"
                title="Repetition of excercise set"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-card title="Exercises">
          <b-list-group
            v-for="(exi, index) in ONE_WORKOUT.exercises"
            :key="index"
          >
            <b-list-group-item>
              <b-row class="ex-row">
                <b-col>{{ index + 1 }}.</b-col>
                <b-col> {{ exi.name }} </b-col>
                <b-col> x {{ exi.quantity }}</b-col>
                <b-col>
                  <!-- delete excercise field -->
                  <b-icon id="trashex" icon="trash" font-scale="2"></b-icon>
                </b-col>
              </b-row>
            </b-list-group-item>
          </b-list-group>
          <!-- <b-row class="ex-row">
            <b-col>
              excercise name field
              <b-form-group
                id="change-exname"
                label="Exercise name:"
                label-for="change-exname-input"
              >
                <b-form-input
                  id="change-exname-input"
                  label="name"
                  v-model="exi.name"
                  :name="`form.exercises[${index}][name]`"
                ></b-form-input>
              </b-form-group>
            </b-col>
            <b-col>
              excercise quantity field
              <b-form-group
                id="change-exquant"
                label="Exercise quantity:"
                label-for="change-exquant-input"
              >
                <b-form-input
                  id="change-exquant-input"
                  label="name"
                  v-model="exi.quantity"
                  :name="`form.exercises[${index}][quantity]`"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          excercise description field
          <b-form-group
            id="change-exdes"
            label="Exercise description:"
            label-for="change-exdes-input"
          >
            <b-form-input
              id="change-exdes-input"
              label="name"
              v-model="exi.description"
              :name="`form.exercises[${index}][description]`"
            ></b-form-input>
          </b-form-group> -->
        </b-card>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "ModalChangeWorkout",
  data() {
    return {
      id: this.$route.params.id,
      wName: "",
      form: {
        name: "",
        description: "",
        points: "",
        excercises: [
          {
            name: "",
            quantity: "",
            description: ""
          }
        ]
      }
    };
  },
  computed: {
    ...mapGetters(["ONE_WORKOUT"])
  },
  mounted() {
    this.$store.dispatch("GET_WORKOUT", this.id);
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();

      // eslint-disable-next-line no-console
      console.log(this.form);
      // this.$store
      //   .dispatch("CHANGE_WORKOUT", this.form)
      //   .then(() => {
      //     // this.$router.push("/workouts" + this.id);

      //   })
      //   .catch(err => {
      //     if (err.status == 500) {
      //       alert("Workout was not altered.");
      //     }
      //     // eslint-disable-next-line no-console
      //     console.log(err);
      //     // this.$router.push("/workouts/" + this.id);
      //   });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset form values
      // this.form.name = "";
      // this.form.points = "";
      // this.form.rounds = "";
      // this.form.exercises = [{ name: "", quantity: "" }];
      // this.form.description = "";
      // this.form.has_timer = false;
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.ex-row {
  display: grid;
  grid-template-columns: 0.5fr 3fr 2fr 1fr;

  #trashex {
    color: $alarm-title;
    border: solid $alarm-title 1px;
    padding: 0.2em;
    border-radius: 20px;
  }
}
</style>
