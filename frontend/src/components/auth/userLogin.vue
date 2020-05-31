<template>
  <div class="userLogin">
    <!-- <b-card class="card"> -->
    <LoginForm />
    <!-- </b-card> -->
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

<style lang="scss" scoped>
.userLogin {
  text-align: center;
  padding: 2em;
  margin-top: 4em;
  display: block;
  .card {
    opacity: 0.9;
  }
}
@media only screen and (min-width: 700px) {
  .userLogin {
    display: flex;
    justify-content: center;
    margin-top: 12em;
  }
}
</style>
