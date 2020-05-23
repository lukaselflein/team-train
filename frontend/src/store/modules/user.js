import axios from "axios";

export default {
  strict: true,
  state: {
    status: "",
    token: JSON.parse(localStorage.getItem("token")) || "",
    user: localStorage.getItem("userId") || ""
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
    signup_success(state, userId) {
      state.status = "success";
      state.user = userId;
    },
    auth_success(state, token /*, userId*/) {
      state.status = "success";
      state.token = token;
      // state.user = userId;
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
      let nm = userdata.name;
      let pw = userdata.password;
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: "http://localhost:5000/signup",
          data: { email: nm, password: pw },
          method: "POST"
        })
          .then(resp => {
            const userId = resp.data;
            /* eslint-disable-next-line */
            console.log(userId);
            localStorage.setItem("user", JSON.stringify(userId));
            commit("signup_success", userId);
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            reject(err);
          });
      });
    },
    login({ commit }, userdata) {
      let nm = userdata.name;
      let pw = userdata.password;
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: "http://localhost:5000/login",
          data: { email: nm, password: pw },
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
