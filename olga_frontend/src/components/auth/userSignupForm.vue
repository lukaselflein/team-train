<template>
  <div class="authentification">
    <h1>Sign Up</h1>
    <b-form id="registerForm" @submit.prevent="register">
      <b-input
        required
        placeholder="Email"
        type="email"
        v-model="username"
        :state="validateNewName"
        id="new-user"
      ></b-input>
      <b-form-invalid-feedback :state="validateNewMail"
        >Your user Name must be 4-12 characters long.</b-form-invalid-feedback
      >
      <b-form-valid-feedback :state="validateNewMail"></b-form-valid-feedback>
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
      <b-input
        required
        placeholder="repeat Password"
        v-model="passwordR"
        type="password"
        :state="validatePasswordR"
        id="repeat-password"
      ></b-input>
      <b-form-invalid-feedback :state="validatePasswordR"
        >Repeated password does not match password.</b-form-invalid-feedback
      >
      <b-form-valid-feedback :state="validatePasswordR"></b-form-valid-feedback>
    </b-form>
    <b-button
      id="btn-signin"
      :disabled="!validateNewMail || !validatePassword || !validatePasswordR"
      @click="register()"
      >register</b-button
    >
  </div>
</template>

<script>
// import { mapActions } from "vuex";

export default {
  name: "AuthForm",
  data() {
    // bound data from form input
    return {
      username: "",
      password: "",
      passwordR: ""
    };
  },
  computed: {
    // ...mapActions["register"],
    // form fields length validation
    validateNewMail() {
      return this.username.length > 3 && this.username.length < 32;
    },
    validatePassword() {
      return this.password.length > 5 && this.password.length < 32;
    },
    // password repeat validation
    validatePasswordR() {
      return this.password == this.passwordR;
    }
  },
  methods: {
    register() {
      let name = this.username;
      let password = this.password;

      this.$store
        .dispatch("register", { name, password })
        .then(() => {
          this.$router.push("/login");
        })
        .catch(err => {
          alert("Ups! Etwas ist schiefgelaufen.\n" + err);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.authentification {
  @include background;

  #registerForm {
    padding: 1em 0;
    input {
      margin-top: 1em;
    }
  }
  #btn-signin {
    @include auth;
  }
}
</style>
