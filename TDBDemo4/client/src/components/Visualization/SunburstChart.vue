<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "SubburstChart",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(data_, svg_) {
      this.hierarchy(data_);

      let arr = Object.assign({}, Object.assign({}, this.data).children);
      let dom = new Array();
      for (let i = 0; i < Object.keys(arr).length; i++) dom[i] = arr[i].name;
      console.log(dom);

      let color = d3
        .scaleOrdinal()
        .domain(dom)
        .range([
          "rgb(215, 25, 28)",
          "rgb(255, 255, 191)",
          "rgb(253, 174, 97)",
          "rgb(171, 221, 164)",
          "rgb(43, 131, 186)",
          "rgb(215, 25, 28)",
          "rgb(253, 174, 97)",
          "rgb(255, 255, 191)",
          "rgb(171, 221, 164)",
          "rgb(43, 131, 186)",
        ]);

      let width = 250;

      let radius = width / 2;

      let arc = d3
        .arc()
        .startAngle((d) => d.x0)
        .endAngle((d) => d.x1)
        .padAngle(1 / radius)
        .padRadius(radius)
        .innerRadius((d) => Math.sqrt(d.y0))
        .outerRadius((d) => Math.sqrt(d.y1));

      let mousearc = d3
        .arc()
        .startAngle((d) => d.x0)
        .endAngle((d) => d.x1)
        .innerRadius((d) => Math.sqrt(d.y0))
        .outerRadius(radius);

      function partition(data) {
        return d3.partition().size([2 * Math.PI, radius * radius])(
          d3
            .hierarchy(data)
            .sum((d) => d.value)
            .sort((a, b) => b.value - a.value)
        );
      }

      const root = partition(this.data);
      // console.log(root);

      const svg = d3.select(svg_);

      const element = svg.node();
      element.value = { sequence: [], percentage: 0.0 };

      const label = svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("fill", "#888")
        .style("visibility", "hidden");

      label
        .append("tspan")
        .attr("class", "percentage")
        .attr("x", 0)
        .attr("y", 0)
        .attr("dy", "-0.1em")
        .attr("font-size", "3em")
        .text("");

      label
        .append("tspan")
        .attr("x", 0)
        .attr("y", 0)
        .attr("dy", "1.5em")
        .text("of visits begin with this sequence");

      svg
        .attr("viewBox", `${-radius} ${-radius} ${width} ${width}`)
        .style("max-width", `${width / 1.5}px`)
        .style("font", "12px sans-serif");
      var index = 0;

      const path = svg
        .append("g")
        .selectAll("path")
        .data(
          root.descendants().filter((d) => {
            return d.depth && d.x1 - d.x0 > 0.001;
          })
        )
        .join("path")
        .attr("fill", (d) => color(d.data.name))
        .attr("d", arc)
        .attr("id", function () {
          index += 1;
          return "path" + index;
        });

      // svg
      //   .append("g")
      //   .attr("fill", "none")
      //   .attr("pointer-events", "all")
      //   .on("mouseleave", () => {
      //     path.attr("fill-opacity", 1);
      //     label.style("visibility", "hidden");
      //     // Update the value of this view
      //     element.value = { sequence: [], percentage: 0.0 };
      //     element.dispatchEvent(new CustomEvent("input"));
      //   })
      //   .selectAll("path")
      //   .data(
      //     root.descendants().filter((d) => {
      //       // Don't draw the root node, and for efficiency, filter out nodes that would be too small to see
      //       return d.depth && d.x1 - d.x0 > 0.001;
      //     })
      //   )
      //   .join("path")
      //   .attr("d", mousearc);

      let fadeColor = "";

      svg
        .selectAll("path")
        .on("mouseover", function () {
          fadeColor = document.getElementById(this.id).getAttribute("fill");
          d3.select(this)
            .attr("fill", "yellow")
            .append("title")
            .text((d) => `${d.value}%`);
        })
        .on("mouseout", function () {
          d3.select(this).transition().duration(500).attr("fill", fadeColor);
        });
    },
    hierarchy(arr) {
      function buildHierarchy(csv) {
        // Helper function that transforms the given CSV into a hierarchical format.
        const root = { name: "root", children: [] };
        for (let i = 0; i < csv.length; i++) {
          const sequence = csv[i][0];
          const size = +csv[i][1];
          if (isNaN(size)) {
            // e.g. if this is a header row
            continue;
          }
          const parts = sequence.split("-");
          let currentNode = root;
          for (let j = 0; j < parts.length; j++) {
            const children = currentNode["children"];
            const nodeName = parts[j];
            let childNode = null;
            if (j + 1 < parts.length) {
              // Not yet at the end of the sequence; move down the tree.
              let foundChild = false;
              for (let k = 0; k < children.length; k++) {
                if (children[k]["name"] == nodeName) {
                  childNode = children[k];
                  foundChild = true;
                  break;
                }
              }
              // If we don't already have a child node for this branch, create it.
              if (!foundChild) {
                childNode = { name: nodeName, children: [] };
                children.push(childNode);
              }
              currentNode = childNode;
            } else {
              // Reached the end of the sequence; create a leaf node.
              childNode = { name: nodeName, value: size };
              children.push(childNode);
            }
          }
        }
        return root;
      }
      let testroot = buildHierarchy(arr);
      console.log("testroot");
      console.log(testroot);

      this.data = testroot;
      console.log(this.data);

      // this.draw();
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