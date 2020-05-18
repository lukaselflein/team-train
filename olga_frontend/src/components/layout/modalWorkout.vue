<template>
  <div>
    <b-button class="btnNew" v-b-modal.modal-1 variant="warning"
      >New Workout</b-button
    >
    <b-modal id="modal-1" title="Create Workout">
      <div>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-1"
            label="Workout Name:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.name"
              required
              placeholder="Think of a creative name ;)"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Points:" label-for="input-3">
            <b-form-input
              id="input-2"
              type="number"
              min="0.00"
              max="20.01"
              v-model="form.points"
              required
              placeholder="Difficulty level from 0-20"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-3"
            label="Exercise: "
            label-for="input-3"
          >
            <b-row v-for="(row, index) in rows" :key="index">
              <b-col>
                <b-form-input
                  id="input-3"
                  v-model="form.exercise.name"
                  required
                  label="name"
                  placeholder="Name"
                ></b-form-input>
              </b-col>
              <b-col class="exRow">
                <b-form-input
                  id="input-4"
                  v-model="form.exercise.quantity"
                  type="number"
                  min="0.00"
                  required
                  placeholder="repeat"
                ></b-form-input>
              </b-col>
              <b-col><b-button @click="removeLine"></b-button></b-col>
            </b-row>
          </b-form-group>
          <div>
            <b-button @click="addLine" variant="outline-primary">+</b-button>
            <b-row class="lstRow">
              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-row>
          </div>
        </b-form>
        <b-card class="mt-3" header="Form Data Result">
          <pre class="m-0">{{ form }}</pre>
        </b-card>
      </div>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "ModalWorkout",
  data() {
    return {
      value: [],
      form: {
        name: "",
        points: "",
        exercise: { name: "", quantity: "" },
        exerciseList: []
      },

      rows: ["1"],
      show: true
    };
  },
  mounted() {},
  methods: {
    addLine() {
      /* eslint-disable-next-line*/
      console.log("lalala");
      let ex = this.form.exercise;
      this.form.exerciseList.push(ex);
      this.rows.push("1");
    },
    removeLine(index) {
      /* eslint-disable-next-line*/
      console.log(index);
      this.rows.splice(index, 1);
    },
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.points = "";
      this.form.exercise = { name: "", quantity: "" };
      this.form.rows = 1;
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>

<style scoped>
.btnNew {
  min-width: 100%;
}

.lstRow {
  justify-content: right;
}
.lstRow > button {
  margin-right: 1em;
}
.exRow {
  max-width: 130px;
}
</style>
