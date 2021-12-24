<template>
  <div id="Sec3-Chart0" class="rightC">
    <svg id="svg4"></svg><br>
    <chart-info>「新しい生活様式」に対応した<br>企業活動の定着見込み</chart-info>
  </div>
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import SunburstChart from "@/components/Visualization/SunburstChart.vue"

var f1aData = "default";

export default {
  name: "Sec3Chart0",
  data() {
    var data = null;
    return { data };
  },
  components: {},
  methods: {
    draw() {
      // for (let i=0; i<Object.assign({},Object.assign({}, this.data).children).length; i++)
      SunburstChart.methods.draw(this.data,"#svg4");
    },
    
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f3a-json";
      axios
        .get(path)
        .then((res) => {
          f1aData = res.data;
          if (f1aData != "default") {
            f1aData = JSON.parse(f1aData);
            let arr = f1aData.map(function (d) {
              return [d.name, d.value];
            });
            this.data = arr;
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
  margin-top: -100%;
  margin-top: 90%;
  margin-left: 1.5%;
  text-align:center;
}
.rightC {
  margin-right: 70%;
  margin-top: -15%;
}
</style>