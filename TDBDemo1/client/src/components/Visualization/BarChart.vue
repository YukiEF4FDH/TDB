<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "BarChart",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(data_, svg_) {
      var dataset = data_;
      var width = 800; // グラフの幅
      var height = 160; // グラフの高さ
      var padding = 30; // スケール表示用マージン

      // 2. SVG領域の設定
      var svg = d3.select(svg_).attr("width", width).attr("height", height);

      // 3. 軸スケールの設定
      var xScale = d3
        .scaleBand()
        .rangeRound([padding, width - padding])
        .padding(0.1)
        .domain(
          dataset.map(function (d) {
            return d.name;
          })
        );

      var yScale = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(dataset, function (d) {
            return d.value;
          }),
        ])
        .range([height - padding, padding]);

      // 4. 軸の表示
      svg
        .append("g")
        .attr("transform", "translate(" + 0 + "," + (height - padding) + ")")
        .call(d3.axisBottom(xScale));

      svg
        .append("g")
        .attr("transform", "translate(" + padding + "," + 0 + ")")
        .call(d3.axisLeft(yScale));

      var ii=0;

      // 5. バーの表示
      svg
        .append("g")
        .selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function (d) {
          return xScale(d.name);
        })
        .attr("y", function (d) {
          return yScale(d.value);
        })
        .attr("width", xScale.bandwidth())
        .attr("height", function (d) {
          return height - padding - yScale(d.value);
        })
        .attr("id",function(){ii+=1; return svg_+"bar"+ii;})
        ;

        d3.select(document.getElementById("#svg2bar1"))
        .attr("fill", "rgb(215, 25, 28)");
        d3.select(document.getElementById("#svg2bar2"))
        .attr("fill", "rgb(253, 174, 97)");
        d3.select(document.getElementById("#svg2bar3"))
        .attr("fill", "rgb(255, 255, 191)");
      d3.select(document.getElementById("#svg2bar4"))
        .attr("fill", "rgb(171, 221, 164)");
        d3.select(document.getElementById("#svg2bar5"))
        .attr("fill", "rgb(43, 131, 186)");
        d3.select(document.getElementById("#svg2bar6"))
        .attr("fill", "rgb(215, 25, 28)");
        d3.select(document.getElementById("#svg2bar7"))
        .attr("fill", "rgb(253, 174, 97)");
        d3.select(document.getElementById("#svg2bar8"))
        .attr("fill", "rgb(255, 255, 191)");
        d3.select(document.getElementById("#svg2bar9"))
        .attr("fill", "rgb(171, 221, 164)");


        d3.select(document.getElementById("#svg3bar1"))
        .attr("fill", "rgb(215, 25, 28)");
        d3.select(document.getElementById("#svg3bar2"))
        .attr("fill", "rgb(253, 174, 97)");
        d3.select(document.getElementById("#svg3bar3"))
        .attr("fill", "rgb(255, 255, 191)");
      d3.select(document.getElementById("#svg3bar4"))
        .attr("fill", "rgb(171, 221, 164)");
        d3.select(document.getElementById("#svg3bar5"))
        .attr("fill", "rgb(43, 131, 186)");
        d3.select(document.getElementById("#svg3bar6"))
        .attr("fill", "rgb(215, 25, 28)");
        d3.select(document.getElementById("#svg3bar7"))
        .attr("fill", "rgb(253, 174, 97)");
        d3.select(document.getElementById("#svg3bar8"))
        .attr("fill", "rgb(255, 255, 191)");
        d3.select(document.getElementById("#svg3bar9"))
        .attr("fill", "rgb(171, 221, 164)");
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
  margin-left: 42%;
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