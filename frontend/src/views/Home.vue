<template>
  <div class="home">
    <div class="test">
      <table class="user-table">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Team</th>
        </tr>
        <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.id }}</td>
          <td>{{ user.name }}</td>
          <td>{{ user.team }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      users: ""
    };
  },
  methods: {
    getUsers() {
      const path = "http://localhost:5000/";
      axios
        .get(path)
        .then(res => {
          this.users = res.data.courses;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getUsers();
  }
};
</script>

<style scoped>
.home {
  min-height: 100vh;
  background-color: lavender;
  text-align: center;
}
.test {
  padding: 3em;
}

th,
td {
  padding: 0 2em;
  border: white solid 1px;
}
</style>
