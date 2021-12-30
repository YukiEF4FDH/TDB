<template>
  <div id="container">
    <!-- <canvas id="myCanvas2" width="800" height="300"></canvas> -->
    <!-- <svg id="svgCurve0" width="800" height="300"></svg> -->
    <div id="overlay">
      There're some text for test. <br />
      For example, this is a <ref>ref</ref>.<br />
      And, this is a <claim>claim</claim>.<br />
    </div>
    <svg id="svgCurve1"></svg>
    <!-- <svg id="svgCurve2"></svg> -->
  </div>
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";

export default {
  name: "Test2",
  data() {
    // let pointStr = "[[100,40],[50,106],[200,80],[200,20]]";
    // let data = JSON.parse(pointStr);

    // return { data };
  },
  components: { ref, claim },
  methods: {
    draw() {
      var data = [{ x1: 0, x2: 60, y1: 0, y2: 20 }];

      var data2 = [{ x1: 0, x2: 60, y1: 30, y2: 50 }];

      var svg = d3.select("#svgCurve1");

      var rect1 = svg
        .selectAll("foo")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", (d) => d.x1)
        .attr("y", (d) => d.y1)
        .attr("width", (d) => d.x2 - d.x1)
        .attr("height", (d) => d.y2 - d.y1)
        .attr("fill", "red")
        .attr("id", "rec1");

      var rect2 = svg
        .selectAll("foo")
        .data(data2)
        .enter()
        .append("rect")
        .attr("x", (d) => d.x1)
        .attr("y", (d) => d.y1)
        .attr("width", (d) => d.x2 - d.x1)
        .attr("height", (d) => d.y2 - d.y1)
        .attr("fill", "pink")
        .attr("id", "rec2");

      /////////////////

      // var c = document.getElementById("myCanvas2");
      // var ctx = c.getContext("2d");

      // ctx.beginPath();
      // ctx.moveTo(180, 20);
      // ctx.bezierCurveTo(180, 100, 200, 100, 300, 20);
      // ctx.strokeStyle = "#FF0000";
      // ctx.stroke();

      //////////////

      //////////////////////////////
    },
    drawCurve() {
          let pointStr = "[[100,40],[50,106],[200,80],[200,20]]";
    let data = JSON.parse(pointStr);

      var points = [];
      const target_copy = data;//Object.assign({}, this.data);
      for (var thing in target_copy) {
        console.log(target_copy[thing][0] + "," + target_copy[thing][1]);
        points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
      }
      console.log(points);

      const curve = d3.line().curve(d3.curveNatural);
      

      d3.select("#svgCurve2")
        .append("path")
        .attr("d", curve(points))
        .attr("stroke", "red")
        .attr("fill", "none");

        console.log("?");
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style>
#container {
  position: relative;
  border: 2px solid red;
}
#overlay {
  position: absolute;
  border: 2px solid green;
  fill: green;
}
#myCanvas2 {
  position: absolute;
  border: 2px solid orange;
}
#svgCurve0 {
  position: absolute;
  border: 2px solid orange;
  fill: orange;
}
/* #overlayB {
  position: relative;
  top: 10px;
  left: 50px;
  border: 2px solid blue;
} */
#svgCurve1 {
  position: relative;
  border: 2px dashed blue;
  width: 300px;
  height: 120px;
  left: 15%;
}
#svgCurve2 {
  position: absolute;
  border: 2px dashed purple;
  width: 300px;
  height: 120px;
  left: 11%;
}
</style>