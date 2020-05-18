<template>
  <div class="register">
    <b-card class="card">
      <b-col class="left">
        <h1>Registrieren</h1>
        <AuthForm />
      </b-col>
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
.register {
  padding: 1em;
  margin: auto;
  margin-top: 4em;
}
.card {
  background-color: gainsboro;
}
</style>
