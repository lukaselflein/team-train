<template>
  <div class="create-workout">
    <h1>Create Workout</h1>
    <b-form class="create-form" @submit="onSubmit" @reset="onReset" v-if="show">
      <!-- Workout Name -->
      <b-form-group
        id="input-group-1"
        label="workout name:"
        label-for="input-1"
      >
        <b-form-input id="input-1" v-model="form.name" required></b-form-input>
      </b-form-group>
      <!-- Workout description -->
      <b-form-group
        id="input-group-2"
        label="workout description:"
        label-for="input-2"
      >
        <b-form-textarea
          id="input-2"
          type="text"
          rows="1"
          max-rows="6"
          size="sm"
          v-model="form.description"
          title="Enter a description of yout Workout"
        ></b-form-textarea>
      </b-form-group>

      <b-row class="rowStyle">
        <b-col>
          <!-- Workout Points -->
          <b-form-group id="input-group-3" label="points:" label-for="input-3">
            <b-form-input
              id="input-3"
              type="number"
              min="0.00"
              max="100.01"
              v-model="form.points"
              required
              title="Difficulty level from 0-100"
            ></b-form-input>
          </b-form-group>
        </b-col>
        <b-col>
          <!-- Workout Rounds -->
          <b-form-group id="input-group-4" label="rounds:" label-for="input-4">
            <b-form-input
              id="input-4"
              type="number"
              min="1.00"
              max="100.01"
              v-model="form.rounds"
              required
              title="Repetition of excercise set"
            ></b-form-input>
          </b-form-group>
        </b-col>
        <!-- <b-col> -->
        <!-- Workout timer checkbox -->
        <!-- <b-form-group
            id="input-group-5"
            label="add Timer:"
            label-for="input-5"
          >
            <b-form-checkbox
              id="input-5"
              v-model="form.has_timer"
              name="check-button"
              switch
            >
            </b-form-checkbox>
          </b-form-group>
        </b-col> -->
      </b-row>

      <!-- ----------------------------------------------------------------------------------- -->
      <!-- ------------------------------------------------------------------ excercise fields -->
      <b-card>
        <h2>Exercises</h2>
        <!-- <h3 v-if="form.exercises">{{ form.exercises.name }}</h3> -->
        <ul v-for="(names, number) in form.exercises" :key="number">
          <b-row class="exList">
            <b-col
              ><li>{{ number + 1 }}. {{ names.name }}</li></b-col
            >
            <b-col>
              <b-icon
                class="icon"
                icon="chevron-up"
                @click="moveUp(number)"
              ></b-icon>
            </b-col>
            <b-col>
              <b-icon
                class="icon"
                icon="chevron-down"
                @click="moveDown(number)"
              ></b-icon>
            </b-col>
            <!---------------------------------------------------------- delete excercise field -->
            <b-col id="trashcol">
              <b-icon
                class="icon"
                id="trash"
                icon="trash"
                @click="removeExercise(number)"
                font-scale="2"
              ></b-icon>
            </b-col>
          </b-row>
          <!--   <h4>{{ index + 2 }}. {{ names.name }} x {{ names.quantity }}</h4>-->
        </ul>
      </b-card>

      <!-- --------------------------------------------------------------------- add exercise form -->
      <b-card>
        <div v-for="(exercise, indexEx) in exerciseBuffer" :key="indexEx">
          <b-row class="rowStyle">
            <!-- -------------------------------------------------------- excercise name field -->
            <b-col>
              <b-form-group
                id="input-group-6"
                label="name:"
                label-for="input-6"
              >
                <b-form-input
                  id="input-6"
                  label="name"
                  v-model="exercise.name"
                  :name="`exerciseBuffer[${indexEx}][name]`"
                ></b-form-input>
              </b-form-group>
            </b-col>
            <!-- ---------------------------------------------------- excercise quantity field -->
            <b-col>
              <b-form-group
                id="input-group-7"
                label="quantity:"
                label-for="input-7"
              >
                <b-form-input
                  id="input-7"
                  label="quantity"
                  v-model="exercise.quantity"
                  :name="`exerciseBuffer[${indexEx}][quantity]`"
                  type="number"
                  min="0.00"
                  required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <b-row class="rowStyle" v-if="seen">
                <b-col>
                  <b-button variant="warning" v-on:click="seen = !seen"
                    >add description</b-button
                  ></b-col
                >
                <!----------------------------------------------------------------- add new excercise -->
                <b-col>
                  <b-btn id="add" variant="info" @click="addExercise"
                    >add</b-btn
                  ></b-col
                >
              </b-row>
              <!------------------------------------------------------------ exercise description -->
              <div class="description" v-if="!seen">
                <!-- <b-row > -->
                <b-col>
                  <b-form-group
                    id="input-group-8"
                    label="description:"
                    label-for="input-8"
                  >
                    <b-form-textarea
                      id="input-8"
                      type="text"
                      v-model="exercise.description"
                      rows="1"
                      max-rows="6"
                      :name="`exerciseBuffer[${indexEx}][description]`"
                      title="Enter a description of your excercise"
                    ></b-form-textarea>
                  </b-form-group>
                </b-col>
                <!-- </b-row> -->
                <b-row class="rowStyle">
                  <b-col>
                    <b-icon
                      @click="seen = !seen"
                      icon="dash"
                      class="icon"
                      font-scale="2"
                    >
                    </b-icon
                  ></b-col>
                  <b-col>
                    <!----------------------------------------------------------------- add new excercise -->
                    <b-btn id="add" variant="info" @click="addExercise"
                      >add</b-btn
                    ></b-col
                  >
                </b-row>
              </div>
            </b-col>
          </b-row>
        </div>
      </b-card>
      <div>
        <!---------------------------------------------------------------- submit & reset btn -->
        <b-row class="lstRow">
          <b-button type="reset" class="btn-lg" variant="secondary"
            >Reset</b-button
          >
          <b-button type="submit" class="btn-lg" variant="success"
            >Submit</b-button
          >
        </b-row>
      </div>
    </b-form>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "NewWorkout",
  data() {
    return {
      seen: true,
      exerciseBuffer: [
        {
          name: "",
          quantity: 1,
          description: ""
        }
      ],
      form: {
        name: "",
        points: 10,
        rounds: 1,

        description: "",
        has_timer: false,
        exercises: []
      },
      index: "",
      show: true
    };
  },
  computed: {
    ...mapActions(["CREATE_WORKOUT"])
  },
  methods: {
    // ...mapActions(["createWorkout"]),

    // move exercise one down
    moveDown(index) {
      if (index + 1) {
        let element = this.form.exercises[index];
        this.form.exercises.splice(index, 1);
        this.form.exercises.splice(index + 1, 0, element);
      }
    },
    // move exercise onw up
    moveUp(index) {
      if (index >= 1) {
        let element = this.form.exercises[index];
        this.form.exercises.splice(index, 1);
        this.form.exercises.splice(index - 1, 0, element);
      }
    },

    // adding a new input row
    addExercise() {
      let index = this.exerciseBuffer.length - 1;
      if (!this.exerciseBuffer[index].name) {
        alert("Please enter a name for the exercise.");
      } else {
        this.form.exercises.push(this.exerciseBuffer[index]);
        this.exerciseBuffer.splice(index, 1);
        this.exerciseBuffer.push({
          name: "",
          quantity: 1,
          description: ""
        });
      }
    },
    // removing input row
    removeExercise(index) {
      if (this.form.exercises.length >= 1) {
        this.form.exercises.splice(index, 1);
      } else {
        alert("Please enter at least one exercise.");
      }
    },
    onSubmit(evt) {
      evt.preventDefault();

      if (this.form.exercises.length < 1) {
        alert("Please enter at least one exercise.");
      }

      this.$store
        .dispatch("CREATE_WORKOUT", this.form)
        .then(() => {
          this.$router.push("/workouts");
        })
        .catch(() => {
          // alert("Workout was not created.");
          this.$router.push("/workouts");
        });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset form values
      this.form.name = "";
      this.form.points = 1;
      this.form.rounds = 1;
      this.exerciseBuffer = [{ name: "", quantity: "", description: "" }];
      this.form.exercises = [];
      this.form.description = "";
      this.form.has_timer = false;
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../mixins.scss";

.create-workout {
  @include background;
  margin-top: 4em;
  text-align: center;
  .create-form {
    .icon {
      cursor: pointer;
      margin: auto;
      padding: 0.1em;
      color: $dark-title;
      box-shadow: 0 0 10px $light-title;
      border-radius: 30px;
    }
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
      margin-top: 1em;
      display: flex;
      justify-content: flex-end;
    }
    .lstRow > button {
      margin-right: 1em;
    }
    .exList {
      display: grid;
      grid-template-columns: 10fr 1fr 1fr 2fr;
      padding: 0.1em;
      border: 1px $light-title solid;
      border-radius: 10px;
    }

    .exRowsnd {
      padding: 0 1em 0 1em;
      display: grid;
      grid-template-columns: 5fr 2fr;
      grid-column-gap: 10px;
      margin-bottom: 0.5em;
      min-width: 100%;
    }

    #trashcol {
      text-align: right;
    }

    .rowStyle {
      padding: 0 1em 0 1em;
      display: grid;
      grid-template-columns: 5fr 2fr;
      grid-column-gap: 10px;
      margin-bottom: 0.5em;
    }
  }
  #add {
    float: right;
    width: 80px;
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
