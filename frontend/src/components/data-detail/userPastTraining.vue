<template>
  <div>
    <p>TRAININGS</p>
    <div id="sq_past">
      <div v-if="USER_HISTORY">
        <h3>{{ USER_HISTORY }}</h3>
      </div>
      <div v-else>
        <h3>0</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserPastTraining",
  computed: {
    ...mapGetters(["USER_HISTORY"])
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

#sq_past {
  @include square($dark-title);
}
</style>
