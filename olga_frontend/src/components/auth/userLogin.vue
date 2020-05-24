<template>
  <div class="userLogin">
    <b-card class="card">
      <h4>Anmelden</h4>
      <LoginForm />
    </b-card>
  </div>
</template>

<script>
import LoginForm from "@/components/auth/userLoginForm";
export default {
  name: "Login",
  components: {
    LoginForm
  }
};
</script>

<style scoped>
@media only screen and (max-width: 700px) {
  .userLogin {
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
  .userLogin {
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
