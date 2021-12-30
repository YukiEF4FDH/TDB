<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "StackedBarWithLine",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(data_,svg_,padding_,width_) {
      this.data = data_;
      // console.log("data");
      // console.log(data_);
      let series = d3
        .stack()
        .keys(this.data.columns.slice(1))
        .offset(d3.stackOffsetExpand)(this.data)
        .map((d) => (d.forEach((v) => (v.key = d.key)), d));

      // console.log("series");
      //         console.log(series);

      let color = d3
        .scaleOrdinal()
        .domain(series.map((d) => d.key))
        .range(d3.schemeSpectral[series.length])
        .unknown("#ccc");


      let margin = {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0,
      };

      let width = 1330;
      let height = this.data.length * 33+250;
      // console.log(height);

      let svg = d3
        .select(svg_)
        .attr("viewBox", [0, 0, width+width_, height])
        .style("overflow", "visible");

      let y = d3
        .scaleBand()
        .domain(this.data.map((d) => d.year))
        .range([margin.top, height])
        .padding(padding_);

      let x = d3.scaleLinear().range([margin.left, width - margin.right]);

      let formatValue = (x) => (isNaN(x) ? "N/A" : x.toLocaleString("en"));

      let formatPercent = d3.format(".1%");

      let arr_j = new Array();
      let j = 0;
      let postfix = "";
      let length_y = series[0].length;

      svg
        .append("g")
        .selectAll("g")
        .data(series)
        .enter()
        .append("g")
        .attr("fill", function (d, i) {
          if (i + 1 == 1) arr_j[j++] = i + 1 + "a";
          // ???
          else if (i + 1 == 2) arr_j[j++] = i + "b";
          else arr_j[j++] = i;
          // if (d.key=="踊り場局面") return "rgb(254, 224, 139)";
          if (d.key=="悪化局面") return "rgb(43, 131, 186)";
          if (d.key=="分からない") return "#BFBFBF";
          // console.log(i);
          return color(d.key);
        })
        .selectAll("rect")
        .data(function (d) {
          j = 0;
          return d;
        })
        .join("rect")
        .attr("id", function (d, i) {
          let id = "";
          if (j % length_y == 0) {
            postfix = arr_j[j / length_y];
            id = "F1A_" + (i + 1) + "_" + postfix;
          } else {
            id = "F1A_" + (i + 1) + "_" + postfix;
          }
          // console.log("F1A_" + (i + 1) + "_" + arr_j[(j) / length_y]);
          j++;
          return id;
        })
        .attr("class", (d) => `${d.data.year}${d.key}`)
        .attr("x", function (d) {
          return x(d[0]);
        })
        .attr("y", function (d, i) {
          return y(d.data.year) ;//+ i * 7;
        })
        .attr("width", (d) => x(d[1]) - x(d[0]) + 15)
        .attr("height", y.bandwidth());

      let newSeries = new Array(14 * 3);
      for (let i = 0; i < 14 * 3; i++) {
        newSeries[i] = new Array(2);
        for (let j = 0; j < 2; j++) {
          newSeries[i][j] = new Array(1);
          newSeries[i][j][0] = 0;
          newSeries[i][j].year = "test";
          // console.log(newSeries[i][j]);
          // console.log(newSeries[i][j].year);
        }
      }
      // console.log(series);
      // for (let i=0; i<series.length;i++)
      //   for (let j=0; j<series[i].length; j++)
      //     console.log(series[i][j].data.year);

      for (let i = 0,ii=1,jj=0; i < newSeries.length; i++) 
      {
        if (jj>=14) {ii+=1;jj=0;}
        newSeries[i][0][0] = series[ii][jj][0];
        newSeries[i][0].year = series[ii][jj].data.year;
        newSeries[i][1][0] = series[ii][++jj][0];
        newSeries[i][1].year = series[ii][jj].data.year;
      }
      console.log(newSeries);

      let count=0;
      var line = d3
        .line()
        .x(function (d) {
          console.log(d[0]);
          return x(d[0]);
        })
        .y(function (d, i) {
          console.log(i + " " + d.year);
          if (count>13) count=0;
          if (i==0)
          {
            let val = y(d.year) +(y.bandwidth() );//+ count * 7 );
            return val;
          }
          else
          {
            let val = y(d.year) ;//+ (++count) * 7  ;//+(y.bandwidth()/2);
            return val;
          }
          // if (i%2==0)
          // {
          //   last = y(d.data.year)+i*4+y.bandwidth();
          //   return y(d.data.year)+i*4+y.bandwidth();
          //   }
          //   else {
          //     return last+i*4;
          //   }
        });

      svg
        .selectAll("myLines")
        .data(newSeries)
        .enter()
        .append("path")
        .attr("d", function (d, i) {
            return line(d);
        })
        .attr("stroke", function (d) {
          return "grey";
        })
        .style("stroke-width", 2)
        .style("fill", "none")
        .style("stroke-dasharray", "5,5");

      var font;

      svg
        .selectAll("rect")
        .on("mouseover", function () {
          // console.log(this);
          // console.log(d3.select(this)._groups[0]);
          d3.select(this)
            .attr("fill", "yellow")
            .append("title")
            .text(
              (d) => `${d.data.year} ${d.key}
											${formatPercent(d[1] - d[0])} (${formatValue(d.data[d.key])})`
            );

          font = document.getElementById("test0").style.font;
          document.getElementById("test0").style.font =
            "italic 20px arial,serif";
        })
        .on("mouseout", function () {
          d3.select(this)
            .transition()
            .duration(500)
            .attr("fill", (d) => color(d.key));

          document.getElementById("test0").style.font = font;
        });

      let yAxis = (g) =>
        g
          .attr("transform", `translate(${margin.left},`+0+`)`)
          .call(d3.axisLeft(y).tickSizeOuter(0))
          .call((g) => g.selectAll(".domain").remove());

      let xAxis = (g) =>
        g
          .attr("transform", `translate(0,${margin.top})`)
          .call(d3.axisTop(x).ticks(width / 100, "%"))
          .call((g) => g.selectAll(".domain").remove());

      svg.append("g").call(xAxis);

      svg.append("g").call(yAxis);
    },
  },
};
</script>

<style scoped>

.rightC {
  margin-left: 42%;
}

</style>