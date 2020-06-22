<template>
  <div class="register">
    <AuthForm />
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

<style lang="scss" scoped>
.register {
  text-align: center;
  padding: 2em;
  margin-top: 4em;
  display: block;
}
@media only screen and (min-width: 701px) {
  .register {
    display: flex;
    justify-content: center;
    margin-top: 12em;
  }
}
</style>
