<template>
  <div class="create-workout">
    <h2>Create Workout</h2>
    <b-form class="create-form" @submit="onSubmit" @reset="onReset" v-if="show"
      ><div class="form-align">
        <b-form-group
          id="input-group-1"
          label="Workout Name:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.name"
            required
            v-b-tooltip.click
            title="Think of a creative name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-2" label="Points:" label-for="input-3">
          <b-form-input
            id="input-2"
            type="number"
            min="0.00"
            max="20.01"
            v-model="form.points"
            required
            v-b-tooltip.click
            title="Difficulty level from 0-20"
          ></b-form-input>
        </b-form-group>
      </div>
      <b-form-group
        id="input-group-5"
        label="Workout Description:"
        label-for="input-5"
      >
        <b-form-textarea
          id="input-5"
          type="text"
          rows="3"
          max-rows="6"
          v-b-tooltip.click
          title="Enter a description of yout Workout"
        ></b-form-textarea>
      </b-form-group>

      <b-form-group id="input-group-6" label="add Timer:" label-for="input-6">
        <b-form-checkbox
          id="input-6"
          v-model="checked"
          name="check-button"
          switch
        >
          Timer: {{ checked }}
        </b-form-checkbox>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Exercises & Quantity: "
        label-for="input-3"
      >
        <b-row v-for="(exercise, index) in form.exercises" :key="index">
          <div class="exRow">
            <b-form-input
              id="input-3"
              required
              label="name"
              v-model="exercise.name"
              :name="`form.exercises[${index}][name]`"
            ></b-form-input>

            <b-form-input
              id="input-4"
              label="Quantity"
              v-model="exercise.quantity"
              :name="`form.exercises[${index}][quantity]`"
              type="number"
              min="0.00"
              required
            ></b-form-input>

            <b-icon
              id="trash"
              icon="trash"
              @click="removeExercise(index)"
              font-scale="2"
            ></b-icon>
          </div>
        </b-row>
      </b-form-group>
      <div>
        <b-icon
          icon="plus"
          id="plus"
          font-scale="2"
          @click="addExercise"
          variant="outline-primary"
        ></b-icon>
        <b-row class="lstRow">
          <b-button type="submit" class="btn-lg" variant="outline-primary"
            >Submit</b-button
          >
          <b-button type="reset" class="btn-lg" variant="outline-danger"
            >Reset</b-button
          >
        </b-row>
      </div>
    </b-form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "NewWorkout",
  data() {
    return {
      checked: false,
      form: {
        name: "",
        points: "",
        exercises: [
          {
            name: "",
            quantity: ""
          }
        ]
      },
      index: "",
      show: true
    };
  },
  computed: {
    ...mapGetters(["NEW_WORKOUT"])
  },
  methods: {
    ...mapActions(["createWorkout"]),
    // adding a new input row
    addExercise() {
      let index = this.form.exercises.length - 1;
      if (
        this.form.exercises[index].name != "" &&
        this.form.exercises[index].quantity != ""
      ) {
        this.form.exercises.push({
          name: "",
          quantity: ""
        });
      } else {
        alert("Please finish the previous exercise.");
      }
    },
    // removing input row
    removeExercise(index) {
      if (this.form.exercises.length >= 2) {
        this.form.exercises.splice(index, 1);
      } else {
        alert("Please enter at least one exercise.");
      }
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.createWorkout(this.form);
      // this.show = false;
      // this.$refs["my-modal"].hide();
      // alert("Your Workout " + this.form.name + " has been created!");
      this.$router.push("/");
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset form values
      this.form.name = "";
      this.form.points = "";
      this.form.exercises = [{ name: "", quantity: "" }];
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../mixins.scss";

.create-workout {
  @include background;
  margin-top: 1em;
  text-align: center;
  .create-form {
    padding: 1em;
    text-align: left;
    .form-align {
      display: inline-flex;
      :first-child {
        min-width: 75%;
        margin-right: 1em;
      }
    }
    .lstRow {
      display: flex;
      justify-content: flex-end;
    }
    .lstRow > button {
      margin-right: 1em;
    }
    .exRow {
      padding: 0 1em 0 1em;
      display: grid;
      grid-template-columns: 4fr 3fr 1fr;
      justify-items: end;
      justify-content: end;
      grid-column-gap: 10px;
      margin-bottom: 0.5em;
      #trash {
        color: palevioletred;
        margin: 0.1em;
        padding: 0.1em;
        border: palevioletred solid 1px;
        border-radius: 20px;
      }
    }
    #plus {
      color: blue;
      border: blue 1px solid;
      border-radius: 20px;
      padding: 0.1em;
      margin-bottom: 1em;
    }
  }
}
@media only screen and (min-width: 700px) {
  .create-workout {
    max-width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
