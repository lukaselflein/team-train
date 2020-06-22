<template>
  <div>
    <h6>{{ convertTime(time) }}</h6>
  </div>
</template>

<script>
export default {
  name: "Time",
  props: {
    time: {
      type: String,
      required: true
    }
  },
  methods: {
    // unix time convert
    convertTime(unix) {
      let timestamp = Date.parse(unix);
      let date = new Date(timestamp);
      const options = {
        // weekday: "short",
        year: "numeric",
        month: "2-digit",
        day: "numeric"
        // hour: "2-digit",
        // minute: "2-digit"
      };
      return date.toLocaleString("en-US", options);
    }
  }
};
</script>

<style></style>
