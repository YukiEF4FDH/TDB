<script>
import axios from "axios";
import * as d3 from "d3";

var f1aData = "default";

export default {
  name: "MultipleLines",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw(data_, svg_, padding_, width_) {

        var dataset1 = [
            [1,1], [12,20], [24,36],
            [32, 50], [40, 70], [50, 100],
            [55, 106], [65, 123], [73, 130],
            [78, 134], [83, 136], [89, 138],
            [100, 140]
        ];

        var dataset2= [
            [1,43], [12, 138], [24,45],
            [32, 35], [40, 12], [50, 212],
            [55, 106], [65, 123], [73, 20],
            [78, 24], [83, 236], [89,32],
            [100, 20]
        ];


        // Step 3
        var svg = d3.select(svg_),
            margin = 20,
            width = svg.attr("width")  - margin, //300
            height = svg.attr("height") - margin; //200

        // Step 4 
        var xScale = d3.scaleLinear().domain([0, 100]).range([0, width]),
            yScale = d3.scaleLinear().domain([0, 250]).range([height, 0]);
            
        var g = svg.append("g")
            .attr("transform", "translate(" + 30 + "," + 10 + ")");

        // Step 5
        // Title
        svg.append('text')
        .attr('x', width/2 + 100)
        .attr('y', 100)
        .attr('text-anchor', 'middle')
        .style('font-family', 'Helvetica')
        .style('font-size', 20)
        .text('Line Chart');
        
        // X label
        svg.append('text')
        .attr('x', width/2 + 100)
        .attr('y', height - 15 + 150)
        .attr('text-anchor', 'middle')
        .style('font-family', 'Helvetica')
        .style('font-size', 12)
        .text('Independant');
        
        // Y label
        svg.append('text')
        .attr('text-anchor', 'middle')
        .attr('transform', 'translate(0,' + height + ')rotate(-90)')
        .style('font-family', 'Helvetica')
        .style('font-size', 12)
        .text('Dependant');

        // Step 6
        g.append("g")
         .attr("transform", "translate(0," + height + ")")
         .call(d3.axisBottom(xScale));
        
        g.append("g")
         .call(d3.axisLeft(yScale));
        
        // Step 7
        svg.append('g')
        .selectAll("dot")
        .data(dataset1)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return xScale(d[0]); } )
        .attr("cy", function (d) { return yScale(d[1]); } )
        .attr("r", 3)
        .attr("transform", "translate(" + 30 + "," + 10 + ")")
        .style("fill", "#CC0000");

          svg.append('g')
          .selectAll("dot")
          .data(dataset2)
          .enter()
          .append("circle")
          .attr("cx", function (d) { return xScale(d[0]); } )
          .attr("cy", function (d) { return yScale(d[1]); } )
          .attr("r", 3)
          .attr("transform", "translate(" + 30 + "," + 10 + ")")
          .style("fill", "#CC0000");

        // Step 8        
        var line = d3.line()
        .x(function(d) { return xScale(d[0]); }) 
        .y(function(d) { return yScale(d[1]); }) 
        .curve(d3.curveMonotoneX)
        
        svg.append("path")
        .datum(dataset1) 
        .attr("class", "line") 
        .attr("transform", "translate(" + 30 + "," + 10 + ")")
        .attr("d", line)
        .style("fill", "none")
        .style("stroke", "#CC0000")
        .style("stroke-width", "2");
  
      svg.append("path")
        .datum(dataset2) 
        .attr("class", "line") 
        .attr("transform", "translate(" + 30 + "," + 10 + ")")
        .attr("d", line)
        .style("fill", "none")
        .style("stroke", "#CC0000")
        .style("stroke-width", "2");
    },
  },
};
</script>

<style scoped>

</style>