<template>
  <div>
    <b-button class="btnNew" v-b-modal.modal-1 variant="warning"
      >New Workout
    </b-button>
    <b-modal hide-footer id="modal-1" ref="my-modal" title="Create Workout">
      <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
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

          <b-form-group
            id="input-group-3"
            label="Exercise: "
            label-for="input-3"
            class="exRow"
          >
            <b-row v-for="(exercise, index) in form.exercises" :key="index">
              <b-col>
                <b-form-input
                  id="input-3"
                  required
                  label="name"
                  v-model="exercise.name"
                  :name="`form.exercises[${index}][name]`"
                  placeholder="Name"
                ></b-form-input>
              </b-col>
              <b-col>
                <b-form-input
                  id="input-4"
                  v-model="exercise.quantity"
                  :name="`form.exercises[${index}][quantity]`"
                  type="number"
                  min="0.00"
                  required
                  placeholder="quantity"
                ></b-form-input>
              </b-col>
              <b-col
                ><b-icon
                  class="ico"
                  icon="trash"
                  @click="removeExercise"
                  font-scale="2"
                ></b-icon
              ></b-col>
            </b-row>
          </b-form-group>
          <div>
            <b-icon
              icon="plus"
              class="ico"
              font-scale="2"
              @click="addExercise"
              variant="outline-primary"
            ></b-icon>
            <b-row class="lstRow">
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-row>
          </div>
        </b-form>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "ModalWorkout",
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
      this.$refs["my-modal"].hide();
      // window.location.reload();
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
.ico {
  border: grey solid 1px;
  margin: 0.1em;
  padding: 0.1em;
  color: grey;
  border-radius: 5px;
  cursor: pointer;
}

.btnNew {
  min-width: 100%;
  border-radius: 0%;
}
.exRow {
  min-width: 100%;
  display: inline;
}
.exRow:nth-child(1) {
  background-color: blue;
}

.lstRow {
  justify-content: right;
}
.lstRow > button {
  margin-right: 1em;
}
.exRow {
  max-width: 100px;
}
</style>
