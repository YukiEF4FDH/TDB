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
      let pointStr = "[[20,115],[120,140],[370,165],[750,39]]";
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
  border: 5px dashed purple;
  width: 450px;
  height: 120px;
  left: 35%;
  top: 0%;
}
#svgCurve3 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 300px;
  height: 120px;
  margin-top: 0%;
}
</style>