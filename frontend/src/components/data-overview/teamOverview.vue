<template>
  <b-tab title="Team Data" class="teamTab">
    <b-col>
      <p>MEMBERS</p>
      <div id="sq_member">
        <h3>12</h3>
      </div>
    </b-col>
    <b-card class="teamCard" header-tag="header">
      <template v-slot:header>
        <b-row id="invitebar">
          <b-col class="item1">
            <b-form-input
              id="input-none"
              :state="null"
              placeholder="e-mail"
            ></b-form-input>
          </b-col>

          <b-col class="item2">
            <b-button variant="success">invite</b-button>
          </b-col>
        </b-row>
      </template>
      <!-- member List -> delete member -->
      <MemberList />
    </b-card>
  </b-tab>
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

.teamTab {
  margin: 1em 0 0 0;
  #sq_member {
    @include square($dark-title);
  }
  #invitebar {
    display: flex;
    .item1 {
      flex-grow: 4;
    }
  }
  .teamCard {
    margin-top: 2em;
    @include cardstyle;
  }
}
</style>
