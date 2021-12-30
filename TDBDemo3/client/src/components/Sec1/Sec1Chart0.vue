<template>
  <div id="Sec1-Chart0" class="rightC">
    <svg id="svg1" width=950></svg>
    <!-- <chart-info>新型コロナウイルス感染症による業績への影響</chart-info> -->
  </div>
  <!-- 	<Sec2Text>what</Sec2Text>
	<Sec1Text></Sec1Text> -->
  <!-- <svg id="svgCurve2"></svg> -->
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import StackedBarWithLine from "@/components/Visualization/StackedNormalizedHorizontalBarWithLine.vue"

var f1aData = "default";

export default {
  name: "Sec1Chart0",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw() {
      // let series = d3
      //   .stack()
      //   .keys(this.data.columns.slice(1))
      //   .offset(d3.stackOffsetExpand)(this.data)
      //   .map((d) => (d.forEach((v) => (v.key = d.key)), d));

      // let color = d3
      //   .scaleOrdinal()
      //   .domain(series.map((d) => d.key))
      //   .range(d3.schemeSpectral[series.length])
      //   .unknown("#ccc");

      // let margin = {
      //   top: 0,
      //   right: 0,
      //   bottom: 0,
      //   left: 0,
      // };

      // let width = 1330;
      // let height = this.data.length * 33 + margin.top + margin.bottom;
      // // console.log(height);

      // let svg = d3
      //   .select("#svg1")
      //   .attr("viewBox", [0, 0, width, height])
      //   .style("overflow", "visible");

      // let y = d3
      //   .scaleBand()
      //   .domain(this.data.map((d) => d.month))
      //   .range([margin.top, height - margin.bottom])
      //   .padding(0.08);

      // let x = d3.scaleLinear().range([margin.left, width - margin.right]);

      // let formatValue = (x) => (isNaN(x) ? "N/A" : x.toLocaleString("en"));

      // let formatPercent = d3.format(".1%");

      // let arr_j = new Array();
      // let j = 0;
      // let postfix = "";
      // let length_y = series[0].length;

      // svg
      //   .append("g")
      //   .selectAll("g")
      //   .data(series)
      //   .enter()
      //   .append("g")
      //   .attr("fill", function (d, i) {
      //     if (i + 1 == 1) arr_j[j++] = i + 1 + "a";
      //     // ???
      //     else if (i + 1 == 2) arr_j[j++] = i + "b";
      //     else arr_j[j++] = i;
      //     // console.log(i);
      //     return color(d.key);
      //   })
      //   .selectAll("rect")
      //   .data(function (d) {
      //     j = 0;
      //     return d;
      //   })
      //   .join("rect")
      //   .attr("id", function (d, i) {
      //     let id = "";
      //     if (j % length_y == 0) {
      //       postfix = arr_j[j / length_y];
      //       id = "F1A_" + (i + 1) + "_" + postfix;
      //     } else {
      //       id = "F1A_" + (i + 1) + "_" + postfix;
      //     }
      //     // console.log("F1A_" + (i + 1) + "_" + arr_j[(j) / length_y]);
      //     j++;
      //     return id;
      //   })
      //   .attr("class", (d) => `${d.data.month}${d.key}`)
      //   .attr("x", (d) => x(d[0]))
      //   .attr("y", (d) => y(d.data.month))
      //   .attr("width", (d) => x(d[1]) - x(d[0]))
      //   .attr("height", y.bandwidth());

      // var font;

      // svg
      //   .selectAll("rect")
      //   .on("mouseover", function () {
      //     // console.log(this);
      //     // console.log(d3.select(this)._groups[0]);
      //     d3.select(this)
      //       .attr("fill", "yellow")
      //       .append("title")
      //       .text(
      //         (d) => `${d.data.month} ${d.key}
			// 								${formatPercent(d[1] - d[0])} (${formatValue(d.data[d.key])})`
      //       );

      //     font = document.getElementById("test0").style.font;
      //     document.getElementById("test0").style.font =
      //       "italic 20px arial,serif";
      //   })
      //   .on("mouseout", function () {
      //     d3.select(this)
      //       .transition()
      //       .duration(500)
      //       .attr("fill", (d) => color(d.key));

      //     document.getElementById("test0").style.font = font;
      //   });

      // let yAxis = (g) =>
      //   g
      //     .attr("transform", `translate(${margin.left},0)`)
      //     .call(d3.axisLeft(y).tickSizeOuter(0))
      //     .call((g) => g.selectAll(".domain").remove());

      // let xAxis = (g) =>
      //   g
      //     .attr("transform", `translate(0,${margin.top})`)
      //     .call(d3.axisTop(x).ticks(width / 100, "%"))
      //     .call((g) => g.selectAll(".domain").remove());

      // svg.append("g").call(xAxis);

      // svg.append("g").call(yAxis);
      StackedBarWithLine.methods.draw(this.data,'#svg1',0.5,0);
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
  margin-left: 40%;
  margin-top: -52%;
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