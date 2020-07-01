<template>
  <div>
    <p>SCORE</p>

    <div id="sq_score">
      <div v-if="USER_SCORE">
        <h3>{{ USER_SCORE }}</h3>
      </div>
      <div v-else><h3>0</h3></div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserScore",
  computed: {
    ...mapGetters(["USER_SCORE"])
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_score {
  @include square($alarm-title);
}
</style>
