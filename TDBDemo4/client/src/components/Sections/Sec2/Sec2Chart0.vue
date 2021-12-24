<template>
  <div id="Sec2-Chart0" class="rightC">
    <svg id="svg2"></svg>
    <chart-info>業績に『プラスの影響がある』割合 (%)</chart-info>
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
      BarChart.methods.draw(this.data,"#svg2");

    // var dataset = this.data;
    //   var width = 800; // グラフの幅
    //   var height = 160; // グラフの高さ
    //   var padding = 30; // スケール表示用マージン

    //   // 2. SVG領域の設定
    //   var svg = d3.select("#svg2").attr("width", width).attr("height", height);

    //   // 3. 軸スケールの設定
    //   var xScale = d3
    //     .scaleBand()
    //     .rangeRound([padding, width - padding])
    //     .padding(0.1)
    //     .domain(
    //       dataset.map(function (d) {
    //         return d.name;
    //       })
    //     );

    //   var yScale = d3
    //     .scaleLinear()
    //     .domain([
    //       0,
    //       d3.max(dataset, function (d) {
    //         return d.value;
    //       }),
    //     ])
    //     .range([height - padding, padding]);

    //   // 4. 軸の表示
    //   svg
    //     .append("g")
    //     .attr("transform", "translate(" + 0 + "," + (height - padding) + ")")
    //     .call(d3.axisBottom(xScale));

    //   svg
    //     .append("g")
    //     .attr("transform", "translate(" + padding + "," + 0 + ")")
    //     .call(d3.axisLeft(yScale));

    //   // 5. バーの表示
    //   svg
    //     .append("g")
    //     .selectAll("rect")
    //     .data(dataset)
    //     .enter()
    //     .append("rect")
    //     .attr("x", function (d) {
    //       return xScale(d.name);
    //     })
    //     .attr("y", function (d) {
    //       return yScale(d.value);
    //     })
    //     .attr("width", xScale.bandwidth())
    //     .attr("height", function (d) {
    //       return height - padding - yScale(d.value);
    //     })
    //     .attr("fill", "steelblue");
    },
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f2a-json";
      axios
        .get(path)
        .then((res) => {
          f1aData = res.data;
          if (f1aData != "default") {
            f1aData = JSON.parse(f1aData);
            // var columns = Object.keys(f1aData[0]);
            // f1aData.columns = columns;

            // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
            // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
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
  margin-top: -13%;
}
</style>