<template>
  <div class="authentification">
    <h1>Sign In</h1>
    <b-form id="loginForm" @submit.prevent="login">
      <b-input
        required
        placeholder="Name"
        v-model="username"
        :state="validateName"
        id="feedback-user"
      ></b-input>
      <b-form-invalid-feedback :state="validateName"
        >Your user ID must be 4-12 characters long.</b-form-invalid-feedback
      >
      <b-form-valid-feedback :state="validateName"></b-form-valid-feedback>
      <b-input
        required
        placeholder="Password"
        v-model="password"
        type="password"
        :state="validatePassword"
        id="feedback-password"
      ></b-input>
      <b-form-invalid-feedback :state="validatePassword"
        >Your password must be 6-12 characters long.</b-form-invalid-feedback
      >
      <b-form-valid-feedback :state="validatePassword"></b-form-valid-feedback>
    </b-form>

    <b-button
      id="btn-login"
      variant="outline-primary"
      :disabled="!validateName || !validatePassword"
      @click="login()"
    >
      login</b-button
    >
  </div>
</template>

<script>
// import axios from "axios";
import { mapActions } from "vuex";
export default {
  name: "LoginForm",
  data() {
    // bound data from form input
    return {
      username: "",
      password: ""
    };
  },
  // form fields length validation
  computed: {
    ...mapActions["LOGIN"],
    validateName() {
      return this.username.length > 3 && this.username.length < 32;
    },
    validatePassword() {
      return this.password.length > 5 && this.password.length < 32;
    }
  },
  // login user by taking data from input and sending it as post request to /user/signin
  methods: {
    login() {
      let name = this.username;
      let password = this.password;

      this.$store
        // call action from store "login"
        .dispatch("login", { name, password })
        .then(() => {
          this.$router.push("/");
        })
        .catch(err => {
          if (err.status == 404) {
            alert("This User doesn't exist.");
          }
          // eslint-disable-next-line no-console
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.authentification {
  @include background;

  #loginForm {
    padding: 1em 0;
    input {
      margin-top: 1em;
    }
  }
}
#btn-login {
  @include auth;
}
</style>
