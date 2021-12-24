<script>
import * as d3 from "d3";

export default {
  name: "Curve",
  data() {},
  methods: {
    drawCurve(id) {
      console.log(id);
      if (id == "#svg1Curve0") {
        console.log(id);
        let pointStr = "[[5,130],[200,60],[450,25],[550,84]]";
        let data = JSON.parse(pointStr);
        var points = [];
        const target_copy = data;
        for (var thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select(id)
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      } else if (id == "#svg2Curve2") {
        console.log(id);
        let pointStr = "[[5,130],[200,95],[420,92],[510,139]]";
        let data = JSON.parse(pointStr);
        let points = [];
        const target_copy = data;
        for (let thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select(id)
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      } else if (id == "#svg4Curve1") {
        console.log(id);
        let pointStr = "[[60,60],[150,35],[220,30],[250,50]]";
        let data = JSON.parse(pointStr);
        let points = [];
        const target_copy = data;
        for (let thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select(id)
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      }
    },
    drawCurve2(id) {
      if (id == "svgCurve3") {
        let pointStr = "[[0,110],[150,40],[500,50],[700,55]]";
        let data = JSON.parse(pointStr);
        let points = [];
        const target_copy = data;
        for (let thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select("#svgCurve3")
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      } else if (id == "svg1Curve4") {
        let pointStr = "[[150,120],[250,170],[400,160],[650,130]]";
        let data = JSON.parse(pointStr);
        let points = [];
        const target_copy = data;
        for (let thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select("#svg1Curve4")
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", 2)
          .attr("fill", "none");
      } else if (id == "svg2Curve1") {
        let pointStr = "[[0,180],[150,80],[400,120],[500,133]]";
        let data = JSON.parse(pointStr);
        let points = [];
        const target_copy = data;
        for (let thing in target_copy) {
          points.push(new Array(target_copy[thing][0], target_copy[thing][1]));
        }

        const curve = d3.line().curve(d3.curveNatural);

        d3.select("#svg2Curve1")
          .append("path")
          .attr("d", curve(points))
          .transition()
          .duration(500)
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", 2)
          .attr("fill", "none");

        d3.select("#svg2Curve1")
          .append("line")
          .attr("x1", 130)
          .attr("y1", 133)
          .attr("x2", 880)
          .attr("y2", 133)
          .attr("stroke", "black")
          .attr("stroke-width", 2)
          .attr("fill", "none")
          .attr("stroke-dasharray", 5);
      }
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style>
#svg1Curve0 {
  position: absolute;
  /* border: 2px dashed purple; */
  width: 750px;
  height: 120px;
  left: 35%;
  top: 50.5%;
}
#svgCurve3 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 850px;
  height: 320px;
  margin-top: -18%;
  margin-left: 10%;
}
#svg1Curve4 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 850px;
  height: 320px;
  margin-top: -18%;
  margin-left: 20%;
}
#svg2Curve1 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 900px;
  height: 320px;
  margin-top: -18%;
  margin-left: 30%;
}
#svg2Curve2 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 510px;
  height: 320px;
  margin-top: -8.5%;
  margin-left: 14%;
}
#svg4Curve1 {
  position: absolute;
  /* border: 5px dashed purple; */
  width: 270px;
  height: 120px;
  margin-top: -15%;
  margin-left: 5%;
}
</style>