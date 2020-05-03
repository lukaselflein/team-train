import axios from "axios";

export default {
  strict: true,
  state: {
    loadingStatus: "",
    userList: JSON.parse(localStorage.getItem("USERS"))
  },
  mutations: {
    SET_LOADING_STATUS(state, status) {
      state.loadingStatus = status;
    },
    GET_ALL_USERS(state, users) {
      //   state.loadingstatustatus = "success";
      state.userList = users;
    },
    ERROR_STATUS(state, status) {
      state.loadingStatus = status;
    }
  },
  getters: {
    userList(state) {
      return state.userList;
    }
  },
  actions: {
    getAllUsers({ commit }) {
      /* eslint-disable-next-line*/
      console.log("trying to get");
      return new Promise((resolve, reject) => {
        commit("SET_LOADING_STATUS", "loading");
        axios
          .get("http://localhost:5000/")
          .then(res => {
            let users = res.data;
            /* eslint-disable-next-line*/
            console.log(JSON.stringify(users));
            commit("GET_ALL_USERS", JSON.stringify(res.data));
            localStorage.setItem("USERS", JSON.stringify(res.data));
            /* eslint-disable-next-line*/
            console.log(localStorage.getItem("USERS"));
            resolve(res.data);
          })
          .catch(err => {
            commit("ERROR_STATUS", err.data.status);
            reject(err);
          });
      });
    }
  }
};
