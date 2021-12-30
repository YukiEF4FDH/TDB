<template>
  <div id="Sec2-Chart0" class="rightC">
    <svg id="svg2" width=750 height=410></svg>
    <!-- <chart-info>新型コロナウイルス感染症による業績への影響</chart-info> -->
  </div>
  <!-- 	<Sec2Text>what</Sec2Text>
	<Sec1Text></Sec1Text> -->
  <!-- <svg id="svgCurve2"></svg> -->
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import MultipleLines from "@/components/Visualization/MultipleLines.vue"

var f1aData = "default";

export default {
  name: "Sec2Chart0",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw() {
      MultipleLines.methods.draw(this.data,'#svg2',0.5,0);
    },
    drawCurvedLine() {
      // const points = [[0, 0], [10, 10], [20, 50], [300, 150]];
      // const curve = d3.line().curve(d3.curveNatural);
      // d3.select().select("#svg1").append('path')
      // .attr('d', curve(points))
      // .attr('stroke', 'black')
      // // with multiple points defined, if you leave out fill:none,
      // // the overlapping space defined by the points is filled with
      // // the default value of 'black'
      // .attr('fill', 'none');
    },
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f1a-json";
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
    // this.drawCurvedLine();
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
  margin-top: 10%;
}
.rightC {
  margin-left: 50%;
  margin-top: -35%;
  margin-right: 2%;
}
#svgCurve2 {
  position: absolute;
  border: 2px dashed purple;
  width: 200px;
  height: 120px;
  left: 11%;
}
#svgCurve2 {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  text-align: center;
  margin-left: 30%;
}
</style>