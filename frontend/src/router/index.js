import Vue from "vue";
import Router from "vue-router";
import store from "@/store/index.js";
import Home from "@/views/Home.vue";
import Workout from "@/views/Workout.vue";
import notFound from "@/views/notFound.vue";
import Login from "@/components/auth/userLogin.vue";
import Signup from "@/components/auth/userSignup.vue";
import Exercise from "@/views/Exercise.vue";
import NewWorkout from "@/views/NewWorkout.vue";
import Statistic from "@/components/data-overview/statistic.vue";

Vue.use(Router);

let router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/login",
      name: "Login",
      component: Login
    },
    {
      path: "/signup",
      name: "Signup",
      component: Signup
    },
    {
      path: "/about",
      name: "About",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/About.vue")
    },
    {
      path: "/new-workout",
      name: "newWorkout",
      component: NewWorkout,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/workouts",
      name: "Workouts",
      component: Workout,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/workouts/:id",
      name: "Workout",
      component: Exercise,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/stats",
      name: "Statistic",
      component: Statistic,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/*",
      component: notFound
    }
  ]
});

router.beforeEach((to, from, next) => {
  // check if auth required
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.IS_LOGGED_IN) {
      next();
      return;
    }
    // no token -> redirect to login
    next("/login");
  } else {
    next();
  }
});

export default router;
