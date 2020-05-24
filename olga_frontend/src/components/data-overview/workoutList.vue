<template>
  <div id="content">
    <b-card class="card">
      <div class="filter-Btn">
        <b-button variant="outline-warning" @click="nothing"
          >last week</b-button
        >
        <b-button variant="outline-warning" @click="nothing"
          >last month</b-button
        >
        <b-button variant="outline-warning" @click="nothing"
          >all workouts</b-button
        >
      </div>
      <b-container>
        <b-table
          show-empty
          small
          stacked="md"
          :items="ALL_WORKOUTS"
          :fields="fields"
          class="wkList"
        >
          <template v-slot:cell(name)="row">
            <b class="text-info">{{ row.value }}</b>
          </template>

          <template v-slot:cell(actions)="row">
            <b-row class="btnRow">
              <b-button
                size="sm"
                @click="startWorkout(row.item._id.$oid)"
                class="mr-1"
                variant="success"
              >
                Start
              </b-button>
              <b-button
                class="mr-1"
                variant="info"
                size="sm"
                @click="row.toggleDetails"
              >
                {{ row.detailsShowing ? "Hide" : "Show" }}
              </b-button>
              <b-button
                size="sm"
                @click="removeWorkout(row.item._id.$oid)"
                class="mr-1"
                variant="danger"
              >
                Delete
              </b-button>
            </b-row>
          </template>

          <template v-slot:row-details="row">
            <b-card>
              <ul>
                <li v-for="(value, key) in row.item.exercises" :key="key">
                  {{ key + 1 }}: {{ value.name }} ( {{ value.quantity }} )
                </li>
              </ul>
            </b-card>
          </template>
        </b-table>

        <!-- Info modal -->
        <b-modal
          :id="infoModal.id"
          :title="infoModal.title"
          ok-only
          @hide="resetInfoModal"
        >
          <pre>{{ infoModal.content }}</pre>
        </b-modal>
      </b-container>
    </b-card>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "WorkoutList",
  data() {
    return {
      sortDesc: true,
      fields: [
        { key: "name", label: "" },
        { key: "exercises.length", label: "exercises" },
        { key: "added_by.$oid", label: "Trainer" },
        { key: "points", label: "Points" },
        { key: "actions", label: "" }
      ],
      totalRows: 1,
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      }
    };
  },
  computed: {
    ...mapGetters(["ALL_WORKOUTS"])
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.ALL_WORKOUTS.length;
  },
  methods: {
    ...mapActions(["getAllWorkouts", "getWorkout", "deleteWorkout"]),

    startWorkout(id) {
      this.$router.push("/workouts/" + id);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    nothing() {
      alert("Hey, I'm not doing anything yet :)");
    },
    removeWorkout(id) {
      /* eslint-disable-next-line*/
      console.log(id);
      this.deleteWorkout(id);
      // patch for state.workoutList undefined after creating new workout
      window.location.reload();
    }
  },
  created() {
    this.getAllWorkouts();
  }
};
</script>

<style scoped>
#content {
  padding-bottom: 3em;
}
.card {
  margin: 1em;
  opacity: 0.9;
}
.filter-Btn {
  display: flex;
  justify-content: space-around;
  padding: 1em 0;
}
.btnRow {
  text-align: center;
  display: block;
  min-width: 100%;
}
.mr-1 {
  margin-bottom: 0.5em;
  margin: 0;
}
li {
  list-style: none;
}
.wkList {
  margin-bottom: 3em;
  text-align: left;
}
</style>
