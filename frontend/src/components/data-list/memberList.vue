<template>
  <b-list-group>
    <b-list-group-item class="memberList"
      ><b-row class="row"
        ><b-col class="item1">Cras justo odio</b-col
        ><b-col class="item2"
          ><b-button variant="danger">kick out</b-button></b-col
        ></b-row
      ></b-list-group-item
    >
  </b-list-group>
</template>

<script>
export default {
  name: "MemberList"
};
</script>

<style scoped lang="scss">
@import "../../mixins.scss";

.memberList {
  text-align: left;
  border: none;
  padding: 0;
  .row {
    padding: 0 0 0.5em 0;
    margin: 0;
    display: grid;
    grid-template-columns: 3fr 2fr;
    align-items: center;
    border-bottom: 1px rgb(200, 200, 200) solid;
  }
}
</style>
