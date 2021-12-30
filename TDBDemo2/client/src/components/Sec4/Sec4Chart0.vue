<template>
  <div id="Sec4-Chart0" class="rightCC">
    <chart-info>バイデン氏がアメリカ大統領に</chart-info>
    <chart-info>就任した場合に日本経済に与える影響</chart-info>
    <svg id="svg44"></svg>
    <!-- <chart-info>F2B XXXXXXXXXXXXXXXXXXXXXXX</chart-info> -->
  </div>
  <!-- 	<Sec2Text>what</Sec2Text>
	<Sec1Text></Sec1Text> -->
</template>
<script>
import axios from "axios";
import * as d3 from "d3";
// import BarChart from "@/components/Visualization/BarChart.vue"
import PieChart from "@/components/Visualization/PieChart.vue"

var f1aData = "default";

export default {
  name: "Sec4Chart0",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw() {
      PieChart.methods.draw('#svg44');
    },
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f2a-json";
      axios
        .get(path)
        .then((res) => {
          f1aData = res.data;
          if (f1aData != "default") {
            f1aData = JSON.parse(f1aData);
            var columns = Object.keys(f1aData[0]);
            columns = columns.slice(0, columns.length - 1);
            // // console.log(columns);
            f1aData.columns = columns;
            // console.log("f1aData");
            // console.log(f1aData);

            // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
            f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
            this.data = f1aData;
            this.draw();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.getF1AJson();
  },
};
</script>

<style scoped>
chart-info {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  text-align: center;
  margin-left: 30%;
}
.rightCC {
  /* margin-left:59%; */
  margin-left: 65%;
  margin-top: -20.7%;

}
</style>