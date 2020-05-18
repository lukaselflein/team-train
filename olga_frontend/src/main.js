import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store/index";
import Axios from "axios";

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

Vue.prototype.$http = Axios;
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

const token = localStorage.getItem("token");
if (token) {
  Vue.prototype.$http.defaults.headers.common["Authorization"] = token;
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
