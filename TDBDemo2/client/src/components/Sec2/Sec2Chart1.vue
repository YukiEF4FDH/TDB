<template>
  <div id="Sec2-Chart1" class="rightC">
    <chart-info>2021 年の景気を「回復」「悪化」と見込む割合 ～ 業界別 ～</chart-info>
    <svg id="svg3" width="200%" class="ss"></svg>
  </div>
  <!-- 	<Sec2Text>what</Sec2Text>
	<Sec1Text></Sec1Text> -->
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import BarChart from "@/components/Visualization/GroupedBarChart.vue"

var f1aData = "default";

export default {
  name: "Sec2Chart1",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw() {
      BarChart.methods.draw("#svg3");
    },
    getF1AJson() {
      // const path = "http://127.0.0.1:5000/f2a_1-json";
      // axios
      //   .get(path)
      //   .then((res) => {
      //     f1aData = res.data;
      //     if (f1aData != "default") {
      //       f1aData = JSON.parse(f1aData);
      //       // var columns = Object.keys(f1aData[0]);
      //       // f1aData.columns = columns;

      //       // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
      //       // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
      //       this.data = f1aData;
      //       this.draw();
      //     }
      //   })
      //   .catch((error) => {
      //     console.error(error);
      //   });
    },
  },
  mounted() {
    this.draw();
    // this.getF1AJson();
  },
};
</script>

<style scoped>
chart-info {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  text-align: center;
  margin-left: 41%;
}
.rightC {
  margin-left: -2%;
  margin-top: 1%;
}
.ss {
  margin-top: 2%;
}
</style>