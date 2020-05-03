import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/index";
import Axios from "axios";

import Buefy from "buefy";
import "./../node_modules/buefy/dist/buefy.css";

Vue.config.productionTip = false;

Vue.prototype.$http = Axios;
Vue.use(Buefy);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
