<template>
  <div id="content">
    <h1>Workouts</h1>
    <div class="filter-row">
      <b-button class="filter-btn" @click="nothing">last week</b-button>
      <b-button class="filter-btn" @click="nothing">last month</b-button>
      <b-button class="filter-btn" @click="nothing">all workouts</b-button>
    </div>
    <b-container class="table-cell">
      <b-table
        show-empty
        small
        responsive
        stacked="lg"
        :items="ALL_WORKOUTS"
        :fields="fields"
        class="workout-table"
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

<style lang="scss" scoped>
@import "../../mixins.scss";

#content {
  padding: 1em 1em 3em 1em;
  // margin: 0.5em 3em;
  min-width: 100%;
  min-height: 100%;
  position: absolute;
  top: 5em;
  bottom: 0;

  background-color: white;
  .filter-row {
    display: flex;
    justify-content: space-around;
    padding: 1em 0;
    .filter-btn {
      background-color: $dark-title;
      font-size: 0.7rem;
    }
  }
  .workout-table {
    text-align: left;
  }
}
@media only screen and (min-width: 700px) {
  #content {
    background-color: white;
    // max-width: 90%;
    min-width: 50%;

    .filter-row {
      .filter-btn {
        font-size: 0.8em;
      }
    }
  }
  @media only screen and (min-width: 800px) {
    #content {
      min-width: 50%;
    }
  }
}
</style>
