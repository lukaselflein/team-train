import axios from "axios";

export default {
  strict: true,
  state: {
    user_score: JSON.parse(localStorage.getItem("score")),
    user_history: JSON.parse(localStorage.getItem("history"))
  },
  getters: {
    SCORE_STATUS: state => {
      return state.status;
    },
    USER_SCORE: state => {
      return state.user_score;
    },
    USER_HISTORY: state => {
      return state.user_history;
    }
  },
  mutations: {
    SCORE_REQUEST(state) {
      state.status = "loading";
    },
    USER_SCORE_SUCCESS: (state, data) => {
      state.status = "success";
      state.user_score = data;
    },
    USER_HISTORY_SUCCESS(state, data) {
      state.status = "success";
      state.user_history = data;
    },
    SCORE_ERROR(state) {
      state.status = "error";
    }
  },
  actions: {
    GET_SCORE({ commit }) {
      let token = JSON.parse(localStorage.getItem("token")).token;
      /* eslint-disable-next-line*/
      console.log(token);
      return new Promise((resolve, reject) => {
        commit("SCORE_REQUEST");
        axios({
          url: "http://localhost:5000/my_score",
          method: "GET",
          headers: {
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            localStorage.setItem("score", JSON.stringify(resp.data));
            commit("USER_SCORE_SUCCESS", resp.data);
            resolve(resp);
          })
          .catch(err => {
            commit("SCORE_ERROR");
            reject(err);
          });
      });
    },
    CLAIM_SCORE({ commit }, workoutId) {
      let token = JSON.parse(localStorage.getItem("token")).token;
      /* eslint-disable-next-line*/
      console.log(token);
      return new Promise((resolve, reject) => {
        commit("SCORE_REQUEST");
        axios({
          url: `http://localhost:5000/claim/${workoutId}`,
          method: "POST",
          headers: {
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            localStorage.setItem("score", JSON.stringify(resp.data));
            commit("USER_SCORE_SUCCESS", resp.data);
            resolve(resp);
          })
          .catch(err => {
            commit("SCORE_ERROR");
            reject(err);
          });
      });
    },
    GET_HISTORY({ commit }) {
      let token = JSON.parse(localStorage.getItem("token")).token;
      /* eslint-disable-next-line*/
      console.log(token);
      return new Promise((resolve, reject) => {
        commit("SCORE_REQUEST");
        axios({
          url: "http://localhost:5000/my_score_hist",
          method: "GET",
          headers: {
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            localStorage.setItem("history", JSON.stringify(resp.data));
            commit("USER_HISTORY_SUCCESS", resp.data);
            resolve(resp);
          })
          .catch(err => {
            commit("SCORE_ERROR");
            reject(err);
          });
      });
    }
  }
};
