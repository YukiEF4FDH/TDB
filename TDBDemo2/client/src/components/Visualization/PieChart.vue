<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "PieChart",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(svg_) {
      // // set the dimensions and margins of the graph
      const margin = { top: 10, right: 20, bottom: 80, left: 50 },
        width = 500 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      const svg = d3
        .select(svg_)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      //    svg = d3.select(svg_),
      //     width = svg.attr("width"),
      //     height = svg.attr("height"),
      var radius = Math.min(width, height) / 2;

      var g = svg
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

      var color = d3.scaleOrdinal([
        "rgb(215, 25, 28)",
        "rgb(253, 174, 97)",
        "rgb(43, 131, 186)",
        "#BFBFBF",
        "#e41a1c",
      ]);

      var pie = d3.pie().value(function (d) {
        return d.percent;
      });

      var path = d3
        .arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

      var label = d3
        .arc()
        .outerRadius(radius)
        .innerRadius(radius - 80);

      d3.csv("browseruse.csv").then(function (data) {
        console.log(data);

        var arc = g
          .selectAll(".arc")
          .data(pie(data))
          .enter()
          .append("g")
          .attr("class", "arc");

        arc
          .append("path")
          .attr("d", path)
          .attr("fill", function (d) {
            return color(d.data.browser);
          });

        arc
          .append("text")
          .attr("transform", function (d) {
            return "translate(" + label.centroid(d) + ")";
          })
          .text(function (d) {
            return d.data.browser;
          });
      });
    },
  },
  mounted() {},
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
.rightC {
  margin-left: 2%;
  margin-top: -17%;
}

.arc text {
  font: 10px sans-serif;
  text-anchor: middle;
}

.arc path {
  stroke: #fff;
}

.title {
  fill: teal;
  font-weight: bold;
}
</style>