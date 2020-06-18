<template>
  <div class="tab">
    <b-tab title="Team Data">
      <b-col>
        <p>MEMBERS</p>
        <div id="sq_member">
          <h4>12</h4>
        </div>
      </b-col>
      <b-card>
        <b-row>
          <b-col>
            <b-form-input
              id="input-none"
              :state="null"
              placeholder="e-mail"
            ></b-form-input>
          </b-col>
          <b-col>
            <b-button variant="success">invite</b-button>
          </b-col>
        </b-row>
        <!-- member List -> delete member -->
        <MemberList />
      </b-card>
    </b-tab>
  </div>
</template>

<script>
import MemberList from "@/components/data-list/memberList";

export default {
  name: "TeamOverview",
  components: {
    MemberList
  }
};
</script>

<style lang="scss" scoped>
@import "../../mixins.scss";

.tab {
  margin-top: 1em;
  #sq_member {
    @include square;
    background-color: $dark-title;
    box-shadow: shade($dark-title);
  }
  .memberList {
    text-align: left;
  }
}
</style>
