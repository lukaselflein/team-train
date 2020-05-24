<template>
  <div class="register">
    <b-card class="card">
      <h4>Registrieren</h4>
      <AuthForm />
    </b-card>
  </div>
</template>

<script>
import AuthForm from "@/components/auth/userSignupForm";

export default {
  name: "Signup",
  components: {
    AuthForm
  }
};
</script>

<style scoped>
@media only screen and (max-width: 700px) {
  .register {
    text-align: center;
    padding: 1em;
    margin-top: 4em;
    display: block;
  }
  .card {
    opacity: 0.9;
  }
}
@media only screen and (min-width: 701px) {
  .register {
    display: flex;
    justify-content: center;
    margin-top: 12em;
    /* margin: 5em;
  min-width: 100%;
  display: flex;
  justify-content: center; */
  }
  .card {
    min-width: 600px;
    opacity: 0.9;
  }
}
</style>
