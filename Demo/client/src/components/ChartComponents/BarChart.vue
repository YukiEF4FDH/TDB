<template>
  <div :id="id" style="height: 100%; weight: 100%;">
    <!-- <el-row justify="end" style="margin-left: 64.8%; margin-bottom: 3%;">
      <el-button info @click="onClickResetDataAndChart()">
        <el-icon class="el-icon--left">
          <Back />
        </el-icon>Reset Data or Chart Type
      </el-button>
      <el-popover placement="bottom" :width="200" trigger="click"
        content="this is content, this is content, this is content">
        <template #reference>
          <el-button plain>
            Data Filter<el-icon class="el-icon--right">
              <Filter />
            </el-icon>
          </el-button>
        </template>
        <div>Column</div>
        <el-checkbox v-model="checked1" label="Option 1" size="large" />
        <el-checkbox v-model="checked2" label="Option 2" size="large" />
        <div>Row</div>
        <el-checkbox v-model="checked1" label="Option 1" size="large" />
        <el-checkbox v-model="checked2" label="Option 2" size="large" />
      </el-popover>
      <el-button plain>
        Delete<el-icon class="el-icon--right">
          <Delete />
        </el-icon>
      </el-button>
    </el-row> -->
    <div :id="svgId" class="vis-svg" @click="Hover($event)">
    </div>
    <p>
      <center>{{ title }}</center>
    </p>
  </div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
import { ElRow, ElCol, ElButton, ElIcon, ElPopover, ElCheckbox } from 'element-plus'
import {
  // Upload,
  Filter,
  Delete,
  Back,
} from '@element-plus/icons-vue'
// import {
//   Plus,
// } from '@element-plus/icons-vue'

// import VisCellCreator from "../VisCellCreator.vue";
import { render, ref } from 'vue'

let vm = null;

export default {
  name: "BarChart",
  props: {
    index: null,
    sbIndex: null,
    dataSourceURL: null,
  },
  data() {
    return {
      id: "bar-chart-" + this.sbIndex + "-" + this.index,
      svgId: "svg-" + this.sbIndex + "-" + this.index,
      dataURL: this.dataSourceURL,
      data: null,
      title: "プラスの影響がある"
    };
  },
  components: {
    // ElButton,
    // ElIcon,
    // Filter,
    // Delete,
    // Back,
    // ElPopover,
    // ElCheckbox,
  },
  methods: {
    // onClickResetDataAndChart() {
    //   let visCellCreatorNode = document.getElementById("newBarChart")
    //   while (visCellCreatorNode.firstChild) {
    //     visCellCreatorNode.removeChild(visCellCreatorNode.firstChild);
    //   }

    //   let vnode = <VisCellCreator />
    //   let el = document.createElement("div")
    //   render(vnode, el)

    //   visCellCreatorNode.appendChild(el)
    // },
    Hover(event) {
      console.log("click")
      // let parentNode = event.target.parentNode
      // let parentParentNode = parentNode.parentNode

      // let htmlString = `<el-icon style="background-color: black;"><Plus /></el-icon>`

      // var div = document.createElement('div');
      // div.innerHTML = htmlString.trim();

      // let el = document.createElement("div")
      // el = render(div, el)

      // // let el = document.createElement("div")
      // // let vnode = 
      // //       render(vnode, el)
      // //       let newNode = el

      // let referenceNode = parentNode//parentParentNode
      // referenceNode.parentNode.insertBefore(vnode, referenceNode.nextSibling);
    },
    draw(data_, mySvgId) {
      if (mySvgId == "svg-2-2") {
        vm.title = "マイナスの影響がある"
      }
      let nameOfXY = Object.keys(data_[0])
      let nameOfX = nameOfXY[0]
      let nameOfY = nameOfXY[1]

      let mySvg = document.getElementById(mySvgId)
      let myWidth = mySvg.offsetWidth;
      let myHeight = mySvg.offsetHeight;

      // console.log(mySvgId)
      // console.log(vm.id)

      var chart = BarChart(data_, {
        x: d => d[nameOfX],
        y: d => d[nameOfY],
        xDomain: d3.groupSort(data_, ([d]) => -d[nameOfY], d => d[nameOfX]), // sort by descending frequency
        // yFormat: "%",
        yLabel: nameOfY,
        width: myWidth,
        height: myHeight,
        color: "steelblue"
      })

      mySvg.appendChild(chart);

      // Copyright 2021 Observable, Inc.
      // Released under the ISC license.
      // https://observablehq.com/@d3/bar-chart
      function BarChart(data, {
        x = (d, i) => i, // given d in data, returns the (ordinal) x-value
        y = d => d, // given d in data, returns the (quantitative) y-value
        title, // given d in data, returns the title text
        marginTop = 20, // the top margin, in pixels
        marginRight = 20, // the right margin, in pixels
        marginBottom = 30, // the bottom margin, in pixels
        marginLeft = 40, // the left margin, in pixels
        width = 640, // the outer width of the chart, in pixels
        height = 400, // the outer height of the chart, in pixels
        xDomain, // an array of (ordinal) x-values
        xRange = [marginLeft, width - marginRight], // [left, right]
        yType = d3.scaleLinear, // y-scale type
        yDomain, // [ymin, ymax]
        yRange = [height - marginBottom, marginTop], // [bottom, top]
        xPadding = 0.1, // amount of x-range to reserve to separate bars
        yFormat, // a format specifier string for the y-axis
        yLabel, // a label for the y-axiss
        color = "currentColor" // bar fill color
      } = {}) {
        // Compute values.
        const X = d3.map(data, x);
        const Y = d3.map(data, y);

        // Compute default domains, and unique the x-domain.
        if (xDomain === undefined) xDomain = X;
        if (yDomain === undefined) yDomain = [0, d3.max(Y)];
        xDomain = new d3.InternSet(xDomain);

        // Omit any data not present in the x-domain.
        const I = d3.range(X.length).filter(i => xDomain.has(X[i]));

        // Construct scales, axes, and formats.
        const xScale = d3.scaleBand(xDomain, xRange).padding(xPadding);
        const yScale = yType(yDomain, yRange);
        const xAxis = d3.axisBottom(xScale).tickSizeOuter(0);
        const yAxis = d3.axisLeft(yScale).ticks(height / 40, yFormat);

        // Compute titles.
        if (title === undefined) {
          const formatValue = yScale.tickFormat(100, yFormat);
          title = i => `${X[i]}\n${formatValue(Y[i])}`;
          // console.log(i => `${X[i]}\n${formatValue(Y[i])}`)
        } else {
          const O = d3.map(data, d => d);
          const T = title;
          title = i => T(O[i], i, data);
        }

        const svg = d3.create("svg")
          .attr("width", width)
          .attr("height", height)
          .attr("viewBox", [-10, -5, width, height])
          .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

        svg.append("g")
          .attr("transform", `translate(${marginLeft},0)`)
          .call(yAxis)
          .call(g => g.select(".domain").remove())
          .call(g => g.selectAll(".tick line").clone()
            .attr("x2", width - marginLeft - marginRight)
            .attr("stroke-opacity", 0.1))
          .call(g => g.append("text")
            .attr("x", -marginLeft)
            .attr("y", 10)
            .attr("fill", "currentColor")
            .attr("text-anchor", "start")
            .text(yLabel));

        const bar = svg.append("g")
          .attr("fill", color)
          .selectAll("rect")
          .data(I)
          .join("rect")
          .attr("x", i => xScale(X[i]))
          .attr("y", i => yScale(Y[i]))
          .attr("height", i => yScale(0) - yScale(Y[i]))
          .attr("width", xScale.bandwidth())
          .on("click", function () {
            let fontColor = "#aabe9b"
            d3.select(this).style("fill", "#cae6b6")
              .attr("stroke", fontColor)
              .attr("stroke-width", "5")
          });

        if (title) bar.append("title")
          .text(title);

        svg.append("g")
          .attr("transform", `translate(0,${height - marginBottom})`)
          .call(xAxis);

        return svg.node();
      }
    },
  },
  mounted() {
    vm = this;

    const path = vm.dataURL;
    let loadedData = null;
    let mySvgId = vm.svgId

    axios
      .get(path)
      .then((res) => {
        loadedData = res.data;
        if (loadedData != "default") {
          loadedData = JSON.parse(loadedData);

          vm.data = loadedData;

          // console.log(mySvgId)
          // console.log(vm.dataURL)

          vm.draw(loadedData, mySvgId)
        }
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<style scoped>
.vis-svg {
  width: 100%;
  min-height: 250px;
  height: 100%;
  /* margin-left: 50%; */

}
</style>