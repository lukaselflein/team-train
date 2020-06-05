import axios from "axios";

export default {
  strict: true,
  state: {
    status: "",
    token: JSON.parse(localStorage.getItem("token")) || "",
    user: JSON.parse(localStorage.getItem("userData")) || ""
  },
  getters: {
    AUTH_STATUS: state => state.status,
    IS_LOGGED_IN: state => !!state.token,
    LOGGED_USER: state => state.user
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    signup_success(state, userData) {
      state.status = "success";
      state.user = userData;
    },
    auth_success(state, token) {
      state.status = "success";
      state.token = token;
    },
    logout(state) {
      state.status = "";
      state.token = "";
    },
    auth_error(state) {
      state.status = "error";
    }
  },
  actions: {
    register({ commit }, userdata) {
      let nm = userdata.username;
      let em = userdata.email;
      let pw = userdata.password;
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: "http://localhost:5000/signup",
          data: { email: em, username: nm, password: pw },
          method: "POST"
        })
          .then(resp => {
            const userData = resp.data;
            localStorage.setItem("user", JSON.stringify(userData));
            commit("signup_success", userData);
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            reject(err);
          });
      });
    },
    login({ commit }, userdata) {
      let em = userdata.email;

      let pw = userdata.password;

      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: "http://localhost:5000/login",
          data: { email: em, password: pw },
          method: "POST"
        })
          .then(resp => {
            const token = resp.data;
            localStorage.setItem("token", JSON.stringify(token));
            commit("auth_success", token);
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            reject(err);
          });
      });
    },
    LOGOUT({ commit }) {
      return new Promise(resolve => {
        commit("logout");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    }
  }
};
