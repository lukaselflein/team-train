import axios from "axios";

export default {
  strict: true,
  state: {
    status: "",
    workoutList: JSON.parse(localStorage.getItem("allWorkouts")),
    workout: JSON.parse(localStorage.getItem("oneWorkout"))
  },
  getters: {
    ALL_WORKOUTS: state => state.workoutList,
    ONE_WORKOUT: state => state.workout
  },
  mutations: {
    WORKOUT_REQUEST(state) {
      state.status = "loading";
    },
    WORKOUT_GETALL(state, payload) {
      state.status = "success";
      state.workoutList = payload.reverse();
    },
    WORKOUT_GET_SUCCESS(state, payload) {
      state.status = "success";
      state.workout = payload;
    },
    WORKOUT_CREATE_SUCCESS(state, payload) {
      state = "success";
      state.workoutList.push(payload);
    },
    WORKOUT_CHANGE_SUCCESS(state, payload) {
      state = "success";
      state.workoutList.push(payload);
    },
    WORKOUT_REMOVE(state, workoutId) {
      state = "success";
      /* eslint-disable-next-line*/
      console.log(state.workoutList);
      /* eslint-disable-next-line*/
      console.log(state.workoutList.workout + " aaaaand id " + workoutId);
      state.workoutList.filter(workout => workout.id !== workoutId);
    },
    WORKOUT_ERROR(state) {
      state.status = "error";
    }
  },
  //------------------------------------------ GET PUT DELETE functions
  actions: {
    GET_ALL_WORKOUTS({ commit }) {
      //   let token = localStorage.getItem("token");

      return new Promise((resolve, reject) => {
        commit("WORKOUT_REQUEST");
        axios({
          url: "http://localhost:5000/workouts",
          method: "GET"
        })
          .then(resp => {
            let workouts = resp.data;
            localStorage.setItem("allWorkouts", JSON.stringify(workouts));
            commit("WORKOUT_GETALL", workouts);
            resolve(resp);
          })
          .catch(err => {
            commit("WORKOUT_ERROR");
            reject(err);
          });
      });
    },
    GET_WORKOUT({ commit }, id) {
      return new Promise((resolve, reject) => {
        let token = localStorage.getItem("token").token;
        commit("WORKOUT_REQUEST");
        axios({
          url: `http://localhost:5000/workouts/${id}`,
          method: "GET",
          headers: { Authorization: "Bearer" + token }
        })
          .then(resp => {
            let workoutItem = resp.data;
            commit("WORKOUT_GET_SUCCESS", workoutItem);
            localStorage.setItem("oneWorkout", JSON.stringify(workoutItem));
            resolve(resp);
          })
          .catch(err => {
            commit("WORKOUT_ERROR");
            reject(err);
          });
      });
    },
    CREATE_WORKOUT({ commit }, workout) {
      return new Promise((resolve, reject) => {
        /* eslint-disable-next-line*/
        console.log(workout);

        let token = JSON.parse(localStorage.getItem("token")).token;
        commit("WORKOUT_REQUEST");
        axios({
          url: "http://localhost:5000/workouts",
          method: "POST",
          data: {
            name: workout.name,
            points: workout.points,
            rounds: workout.rounds,
            exercises: workout.exercises,
            description: workout.description,
            has_timer: workout.has_timer
          },
          headers: {
            Accept: "*/*",
            "Content-Type": "application/json",
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            commit("WORKOUT_CREATE_SUCCESS", resp.data);
            localStorage.setItem("allWorkouts", JSON.stringify(resp.data));
            resolve(workout);
          })
          .catch(err => {
            commit("WORKOUT_ERROR");
            reject(err);
          });
      });
    },
    CHANGE_WORKOUT({ commit }, workout) {
      return new Promise((resolve, reject) => {
        let token = localStorage.getItem("token").token;

        if (workout)
          /* eslint-disable-next-line*/
          console.log(workout);

        commit("WORKOUT_REQUEST");
        axios({
          url: `http://localhost:5000/workouts/${workout.id}`,
          method: "PUT",
          data: {
            name: workout.name,
            points: workout.points,
            exercises: workout.exercises,
            description: workout.description,
            has_timer: workout.has_timer
          },
          headers: { Authorization: "Bearer" + token }
        })
          .then(resp => {
            let workoutItem = resp.data;
            commit("workout_patch_success", workoutItem);
            resolve(resp);
          })
          .catch(err => {
            /* eslint-disable-next-line*/
            console.log(err);
            commit("WORKOUT_ERROR");
            reject(err);
          });
      });
    },

    DELETE_WORKOUT({ commit }, workoutId) {
      return new Promise((resolve, reject) => {
        let token = JSON.parse(localStorage.getItem("token")).token;
        commit("WORKOUT_REQUEST");
        axios({
          url: `http://localhost:5000/workouts/${workoutId}`,
          method: "delete",
          headers: { Authorization: "Bearer " + token }
        })
          .then(resp => {
            commit("WORKOUT_REMOVE", workoutId);
            resolve(resp);
          })
          .catch(err => {
            /* eslint-disable-next-line*/
            console.log(err);
            commit("WORKOUT_ERROR");
            reject(err);
          });
      });
    }
  }
};
