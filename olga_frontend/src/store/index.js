import Vue from "vue";
import Vuex from "vuex";

import user from "./modules/user";
import workout from "./modules/workout";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    workout
  }
});
