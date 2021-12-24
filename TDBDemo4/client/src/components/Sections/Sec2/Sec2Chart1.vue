<template>
  <div id="Sec2-Chart1" class="rightC">
    <svg id="svg3"></svg>
    <chart-info>業績に『マイナスの影響がある』割合 (%)</chart-info>
  </div>
  <!-- 	<Sec2Text>what</Sec2Text>
	<Sec1Text></Sec1Text> -->
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import BarChart from "@/components/Visualization/BarChart.vue"

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
      BarChart.methods.draw(this.data,"#svg3");
    },
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f2a2-json";
      axios
        .get(path)
        .then((res) => {
          f1aData = res.data;
          if (f1aData != "default") {
            f1aData = JSON.parse(f1aData);
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
  margin-left: 35%;
}
.rightC {
  margin-left: 42%;
  margin-top: -25%;
}
</style>