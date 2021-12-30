<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "Map",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(svg_) {
      // set the dimensions and margins of the graph
      const margin = { top: 10, right: 20, bottom: 80, left: 50 },
        width = 1440 - margin.left - margin.right,
        height = 300 - margin.top - margin.bottom;

      // append the svg object to the body of the page
      const svg = d3
        .select(svg_)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // Map and projection
      const projection = d3
        .geoNaturalEarth1()
        .scale(width / 1.3 / Math.PI+1200)
        .translate([-2800, height-100/2])
        ;

        var i=0;

      // Load external data and boot
      d3.json(
        // "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
        "japan.json"
      ).then(function (data) {
        // Draw the map
        svg
          .append("g")
          .selectAll("path")
          .data(data.features)
          .join("path")
          .attr("id",function(){i+=1; return "path"+i;})
          .attr("fill", "#69b3a2")
          .attr("transform","rotate(90)")
          .attr("d", d3.geoPath().projection(projection))
          .style("stroke", "#fff")
          ;
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
#svgCurve2 {
  position: absolute;
  border: 2px dashed purple;
  width: 300px;
  height: 120px;
  left: 11%;
}
</style>