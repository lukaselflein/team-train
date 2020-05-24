<template>
  <div class="create-workout">
    <b-card class="card" title="Create new workout">
      <b-form
        class="create-form"
        @submit="onSubmit"
        @reset="onReset"
        v-if="show"
      >
        <b-form-group
          id="input-group-1"
          label="Workout Name:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.name"
            required
            placeholder="Think of a creative name ;)"
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
            placeholder="Difficulty level from 0-20"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Exercise: " label-for="input-3">
          <b-row v-for="(exercise, index) in form.exercises" :key="index">
            <div class="exRow">
              <b-form-input
                id="input-3"
                required
                label="name"
                v-model="exercise.name"
                :name="`form.exercises[${index}][name]`"
                placeholder="Name"
              ></b-form-input>

              <b-form-input
                id="input-4"
                v-model="exercise.quantity"
                :name="`form.exercises[${index}][quantity]`"
                type="number"
                min="0.00"
                required
                placeholder="quantity"
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
            <b-button type="submit" variant="outline-primary">Submit</b-button>
            <b-button type="reset" variant="outline-danger">Reset</b-button>
          </b-row>
        </div>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "NewWorkout",
  data() {
    return {
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
      alert("Your Workout " + this.form.name + " has been created!");
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

<style scoped>
.card {
  opacity: 0.9;
  margin: 4em 1em 4em 1em;
  text-align: center;
  overflow-y: scroll;
}
.create-workout {
  min-height: 100vh;
}
.create-form {
  padding: 1em;
  text-align: left;
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
}

#trash {
  color: palevioletred;
  margin: 0.1em;
  padding: 0.1em;
  border: palevioletred solid 1px;
  border-radius: 20px;
}
#plus {
  color: blue;
  border: blue 1px solid;
  border-radius: 20px;
  padding: 0.1em;
}
</style>
