import axios from "axios";

export default {
  strict: true,
  state: {
    status: "",
    token: JSON.parse(localStorage.getItem("token")) || "",
    user: JSON.parse(localStorage.getItem("user"))
  },
  getters: {
    AUTH_STATUS: state => {
      return state.status;
    },
    IS_LOGGED_IN: state => {
      return !!state.token;
    },
    LOGGED_USER: state => {
      return state.user;
    }
  },
  mutations: {
    AUTH_REQUEST(state) {
      state.status = "loading";
    },
    SIGNUP_SUCCESS: state => {
      state.status = "success";
    },
    LOGIN_SUCCESS: (state, token) => {
      state.status = "success";
      state.token = token;
    },
    WHOAMI_SUCCESS(state, user) {
      state.status = "success";
      state.user = user;
    },
    LOGOUT_SUCCESS(state) {
      state.status = "";
      state.token = "";
    },
    AUTH_ERROR(state) {
      state.status = "error";
    }
  },
  actions: {
    REGISTER({ commit }, userdata) {
      return new Promise((resolve, reject) => {
        commit("AUTH_REQUEST");
        axios({
          url: "http://localhost:5000/signup",
          data: {
            email: userdata.email,
            username: userdata.username,
            password: userdata.password
          },
          method: "POST",
          headers: {
            Accept: "*/*",
            "Content-Type": "application/json"
          }
        })
          .then(resp => {
            // const userData = resp.data;
            commit("SIGNUP_SUCCESS");
            resolve(resp);
          })
          .catch(err => {
            commit("AUTH_ERROR");
            reject(err);
          });
      });
    },
    LOGIN({ commit }, userdata) {
      return new Promise((resolve, reject) => {
        commit("AUTH_REQUEST");
        axios({
          url: "http://localhost:5000/login",
          data: { email: userdata.email, password: userdata.password },
          method: "POST"
        })
          .then(resp => {
            localStorage.setItem("token", JSON.stringify(resp.data));
            commit("LOGIN_SUCCESS", resp.data);
            commit("SIGNUP_SUCCESS");
            resolve(resp);
          })
          .catch(err => {
            commit("AUTH_ERROR");
            reject(err);
          });
      });
    },
    WHOAMI({ commit }) {
      let token = JSON.parse(localStorage.getItem("token")).token;
      return new Promise((resolve, reject) => {
        commit("AUTH_REQUEST");
        axios({
          url: "http://localhost:5000/whoami",
          method: "GET",
          headers: {
            Authorization: "Bearer " + token
          }
        })
          .then(resp => {
            localStorage.setItem("user", JSON.stringify(resp.data));
            commit("WHOAMI_SUCCESS", resp.data);
            resolve(resp);
          })
          .catch(err => {
            commit("AUTH_ERROR");
            reject(err);
          });
      });
    },
    LOGOUT({ commit }) {
      return new Promise(resolve => {
        commit("LOGOUT_SUCCESS");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    }
  }
};
