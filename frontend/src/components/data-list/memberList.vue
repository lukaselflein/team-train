<template>
  <b-list-group class="memberList">
    <b-list-group-item
      ><b-row class="row"
        ><b-col>Cras justo odio</b-col
        ><b-col
          ><b-button variant="danger">delete member</b-button></b-col
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
.row {
  display: flex;
}
</style>