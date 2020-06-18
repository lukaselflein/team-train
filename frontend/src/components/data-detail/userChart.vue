<template>
  <div>
    <apexchart
      type="bar"
      height="200"
      :options="options"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
// import VueApexCharts from "vue-apexcharts";

export default {
  name: "UserChart",
  data() {
    return {
      options: {
        chart: {
          id: "vuechart-example",
          toolbar: {
            show: false
          }
        },
        stroke: {
          curve: "smooth"
        },
        fill: {
          colors: ["#E91E63"]
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec"
          ]
        }
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 45, 50, 49, 60, 70, 50, 40, 20, 0, 10]
        }
      ]
    };
  }
};
</script>

<style></style>
