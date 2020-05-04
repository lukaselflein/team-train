import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Workouts from './components/Workouts.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Workouts',
      component: Workouts,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
