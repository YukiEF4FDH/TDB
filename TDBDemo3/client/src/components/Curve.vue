<script>
import * as d3 from "d3";

export default {
  name: "Curve",
  data() {},
  methods: {
    drawCurve() {
      let pointStr = "[[20,120],[150,70],[370,35],[450,88]]";
      let data = JSON.parse(pointStr);
      var points = [];
      const target_copy = data; //Object.assign({}, this.data);
      for (var thing in target_copy) {
        // console.log(target_copy[thing][0] + "," + target_copy[thing][1]);
        points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
      }

      const curve = d3.line().curve(d3.curveNatural);

      d3.select("#svgCurve2")
        .append("path")
        .attr("d", curve(points))
        .attr("stroke", "#aabe9b")
        .attr("stroke-width", 2)
        .attr("fill", "none");

    },
    drawCurve2() {
      let pointStr = "[[20,15],[150,70],[370,35],[450,22]]";
      let data = JSON.parse(pointStr);
      var points = [];
      const target_copy = data; //Object.assign({}, this.data);
      for (var thing in target_copy) {
        // console.log(target_copy[thing][0] + "," + target_copy[thing][1]);
        points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
      }

      const curve = d3.line().curve(d3.curveNatural);

      d3.select("#svgCurve3")
        .append("path")
        .attr("d", curve(points))
        .attr("stroke", "#d39d9c")
        .attr("stroke-width", 2)
        .attr("fill", "none");

    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style>
#svgCurve2 {
  position: absolute;
  border: 2px dashed purple;
  width: 450px;
  height: 120px;
  left: 35%;
  top: 50.5%;
}
#svgCurve3 {
  position: absolute;
  border: 2px dashed purple;
  width: 450px;
  height: 120px;
  left: 35%;
  top: 70%;
}
</style>