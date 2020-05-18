<template>
  <div class="userLogin">
    <b-card class="card">
      <h1>Anmelden</h1>
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
.userLogin {
  padding: 1em;
  margin: auto;
  margin-top: 4em;
}
.card {
  background-color: gainsboro;
}
</style>
