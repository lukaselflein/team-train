import axios from "axios";

export default {
  strict: true,
  state: {
    status: "",
    workoutList: JSON.parse(localStorage.getItem("allWorkouts")),
    workout: JSON.parse(localStorage.getItem("oneWorkout")),
    newWorkout: JSON.parse(localStorage.getItem("newWK"))
  },
  getters: {
    ALL_WORKOUTS: state => state.workoutList,
    ONE_WORKOUT: state => state.workout,
    NEW_WORKOUT: state => state.newWorkout
  },
  mutations: {
    workout_request(state) {
      state.status = "loading";
    },
    workout_getAll_success(state, workouts) {
      state.status = "success";
      state.workoutList = workouts;
    },
    workout_get_success(state, workout) {
      state.status = "success";
      state.workout = workout;
    },
    workout_create_success(state, workout) {
      state = "success";
      state.workoutList.shift(workout);
    },
    workout_remove_success(state, workoutId) {
      state = "success";
      state.workoutList = state.workoutList.filter(
        workout => workout._id !== workoutId
      );
    },
    workout_error(state) {
      state.status = "error";
    }
  },
  //------------------------------------------ GET PUT DELETE functions
  actions: {
    getAllWorkouts({ commit }) {
      //   let token = localStorage.getItem("token");

      return new Promise((resolve, reject) => {
        commit("workout_request");
        axios({
          url: "http://localhost:5000/workouts",
          method: "GET"
        })
          .then(resp => {
            let workouts = resp.data;
            commit("workout_getAll_success", resp.data);
            localStorage.setItem("allWorkouts", JSON.stringify(workouts));
            resolve(resp);
          })
          .catch(err => {
            commit("workout_error");
            //localStorage.removeItem("project");
            reject(err);
          });
      });
    },
    getWorkout({ commit }, id) {
      return new Promise((resolve, reject) => {
        let token = localStorage.getItem("token").token;
        /* eslint-disable-next-line*/
        console.log(token);
        commit("workout_request");

        axios({
          url: `http://localhost:5000/workouts/${id}`,
          method: "GET",
          headers: { Authorization: "Bearer" + token }
        })
          .then(resp => {
            let workoutItem = resp.data;
            /* eslint-disable-next-line*/
            console.log(workoutItem);
            commit("workout_get_success", workoutItem);

            localStorage.setItem("oneWorkout", JSON.stringify(workoutItem));
            resolve(resp);
          })
          .catch(err => {
            commit("workout_error");
            reject(err);
          });
      });
    },
    createWorkout({ commit }, workout) {
      return new Promise((resolve, reject) => {
        let token = JSON.parse(localStorage.getItem("token")).token;
        commit("workout_request");
        axios({
          url: "http://localhost:5000/workouts",
          method: "POST",
          data: {
            name: workout.name,
            points: workout.points,
            exercises: workout.exercises
          },
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            let newWorkout = resp.data;

            // localStorage.setItem(
            //   "workoutCreated",
            //   JSON.stringify(resp.data._id)
            // );
            localStorage.setItem("newWK", JSON.stringify(resp.data));
            commit("workout_create_success", newWorkout);
            resolve(resp);
          })
          .catch(err => {
            // if (err.resp.status == 400) {
            //   alert("Workout already exists.");
            // }
            commit("workout_error");
            reject(err);
          });
      });
    },
    patchWorkout() {},
    deleteWorkout({ commit }, workoutId) {
      /* eslint-disable-next-line*/
      console.log(workoutId);
      return new Promise((resolve, reject) => {
        let token = JSON.parse(localStorage.getItem("token")).token;
        commit("workout_request");
        axios({
          url: `http://localhost:5000/workouts/${workoutId}`,
          method: "delete",
          headers: { Authorization: "Bearer " + token }
        })
          .then(resp => {
            commit("workout_remove_success", workoutId);
            resolve(resp);
          })
          .catch(err => {
            /* eslint-disable-next-line*/
            console.log(err);
            // if (err.response.status == 403) {
            //   alert("You can only delete workouts you created!");
            // }
            commit("workout_error");

            reject(err);
          });
      });
    }
  }
};
