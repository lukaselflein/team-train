<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Workouts</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.workout-modal>
            Add Workout
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Workout</th>
              <th scope="col">Points</th>
              <th scope="col">Coach</th>
              <th scope="col">Tap it</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(workout, index) in workouts" :key="index">
              <td>{{ workout.title }}</td>
              <td>{{ workout.points }}</td>
              <td>{{ workout.coach }}</td>
              <td>
                  <button
                          type="button"
                          class="btn btn-primary btn-sm"
                          v-b-modal.workout-update-modal
                          @click="claimWorkout(workout)">
                    <span v-if="workout.done">Yes</span>
                    <span v-else>No</span>
                  </button>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.workout-update-modal
                          @click="editWorkout(workout)">
                      Edit
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteWorkout(workout)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addWorkoutModal"
            id="workout-modal"
            title="Add a new workout"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addWorkoutForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-points-group"
                      label="Points:"
                      label-for="form-points-input">
            <b-form-input id="form-points-input"
                          type="text"
                          v-model="addWorkoutForm.points"
                          required
                          placeholder="Enter points">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-points-group"
                      label="Coach:"
                      label-for="form-coach-input">
            <b-form-input id="form-coach-input"
                          type="text"
                          v-model="addWorkoutForm.coach"
                          required
                          placeholder="Enter Coach">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-done-group">
          <b-form-checkbox-group v-model="addWorkoutForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editWorkoutModal"
            id="workout-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-points-edit-group"
                      label="Points:"
                      label-for="form-points-edit-input">
            <b-form-input id="form-points-edit-input"
                          type="text"
                          v-model="editForm.points"
                          required
                          placeholder="Enter points">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-coach-edit-group"
                      label="Coach:"
                      label-for="form-coach-edit-input">
            <b-form-input id="form-coach-edit-input"
                          type="text"
                          v-model="editForm.coach"
                          required
                          placeholder="Enter Coach">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-done-edit-group">
          <b-form-checkbox-group v-model="editForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      workouts: [],
      addWorkoutForm: {
        title: '',
        points: '',
        coach: '',
        done: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        points: '',
        coach: '',
        done: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getWorkouts() {
      const path = 'http://localhost:5000/api/workouts';
      axios.get(path)
        .then((res) => {
          this.workouts = res.data.workouts;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addWorkout(payload) {
      const path = 'http://localhost:5000/api/workouts';
      axios.post(path, payload)
        .then(() => {
          this.getWorkouts();
          this.message = 'Workout added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getWorkouts();
        });
    },
    initForm() {
      this.addWorkoutForm.title = '';
      this.addWorkoutForm.points = '';
      this.addWorkoutForm.done = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.points = '';
      this.editForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addWorkoutModal.hide();
      let done = false;
      if (this.addWorkoutForm.done[0]) done = true;
      const payload = {
        title: this.addWorkoutForm.title,
        points: this.addWorkoutForm.points,
        coach: this.addWorkoutForm.coach,
        done, // property shorthand
      };
      this.addWorkout(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addWorkoutModal.hide();
      this.initForm();
    },
    editWorkout(workout) {
      this.editForm = workout;
    },
    claimWorkout(workout) {
      this.editForm = workout;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editWorkoutModal.hide();
      let done = false;
      if (this.editForm.done[0]) done = true;
      const payload = {
        title: this.editForm.title,
        points: this.editForm.points,
        coach: this.editForm.coach,
        done,
      };
      this.updateWorkout(payload, this.editForm.id);
    },
    updateWorkout(payload, workoutID) {
      const path = `http://localhost:5000/workouts/${workoutID}`;
      axios.put(path, payload)
        .then(() => {
          this.getWorkouts();
          this.message = 'Workout updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getWorkouts();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editWorkoutModal.hide();
      this.initForm();
      this.getWorkouts(); // why?
    },
    removeWorkout(workoutID) {
      const path = `http://localhost:5000/workouts/${workoutID}`;
      axios.delete(path)
        .then(() => {
          this.getWorkouts();
          this.message = 'Workout removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getWorkouts();
        });
    },
    onDeleteWorkout(workout) {
      this.removeWorkout(workout.id);
    },
  },
  created() {
    this.getWorkouts();
  },
};
</script>
