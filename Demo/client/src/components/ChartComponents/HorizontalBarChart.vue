<template>
    <div :id="id" style="height: 100%; weight: 100%;" @mouseover="InsertVisModify($event)">
        <div :id="id">
            <el-row>

            </el-row>
        </div>
        <div :id="svgId" class="vis-svg">
        </div>
        <center>
            <p style="margin-top: -1%;" @dblclick="dbClickCap($event)">Double click to input the caption</p>
        </center>
    </div>
</template>

<script>
import * as d3 from "d3";
import axios from "axios";
import { ElRow, ElCol, ElButton, ElIcon, ElPopover, ElCheckbox } from 'element-plus'
import {
    Filter,
    Delete,
    Back,
} from '@element-plus/icons-vue'
let isInputCap1 = false
import mybutton from '@/components/mybutton.vue';
import { render, ref } from 'vue'
// import ChartCellToolbarVue from "@/components/ChartComponents/ChartCellToolbar.vue";


let vm = null;

export default {
    name: "HorizontalBarChart",
    props: {
        index: null,
        sbIndex: null,
        dataSourceURL: null,
    },
    data() {
        return {
            id: "horizontal-bar-chart-" + this.sbIndex + "-" + this.index,
            svgId: "svg-" + this.sbIndex + "-" + this.index,
            dataURL: this.dataSourceURL,
            data: null,
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
        // ChartCellToolbarVue
    },
    methods: {
        dbClickCap(e) {
            let target = e.currentTarget
            let newInput = document.createElement("input")
            newInput.setAttribute("type", "text")
            newInput.setAttribute("id", "newInputId4")
            target.innerText = ""
            target.appendChild(newInput)
            isInputCap1 = true

            document.addEventListener('click', function (event) {
                if (isInputCap1 && (event.target.id != "newInputId4")) {
                    let newOutline = document.getElementById("newInputId4").value
                    newInput.remove()
                    target.innerText = newOutline
                    isInputCap1 = false
                }
            });
        },
        clickRect(event) {
            let rect = event.currentTarget
            let idSub = rect.id.split('-')[6]

            let clickedDataFactId = mybutton.methods.getClickedDataFactId()
            let dataFactType = clickedDataFactId.split('-')[3]

            let fillColor = null
            let fontColor = null
            if (dataFactType == "ref") {
                fillColor = "#cae6b6"
                fontColor = "#aabe9b"
            }
            else {
                fillColor = "#fbb"
                fontColor = "#d39d9c"
            }

            d3.select(rect).attr("fill", fillColor)
                .attr("stroke", fontColor)
                .attr("stroke-width", "5")
                ;
            d3.select(document.getElementById(vm.id + "-text-" + idSub))
                .attr("fill", fontColor)
                .attr("font-weight", 700)
                .attr("font-size", 16)

            mybutton.methods.setClickedFragmentId(rect.id)
        },
        Hover(event) {
            console.log("click")
        },
        draw(data_, mySvgId) {
            let nameOfXY = Object.keys(data_[0])
            let nameOfX = nameOfXY[0]
            let nameOfY = nameOfXY[1]

            let mySvg = document.getElementById(mySvgId)
            let myWidth = mySvg.offsetWidth;
            let myHeight = mySvg.offsetHeight;

            var chart = HorizontalBarChart(data_, {
                x: d => d[nameOfY],
                y: d => d[nameOfX],
                // yDomain: d3.groupSort(data_, ([d]) => d[nameOfY], d => d[nameOfX]), // sort by descending frequency
                xLabel: nameOfY,
                width: myWidth,
                color: "steelblue"
            })

            mySvg.appendChild(chart);

            // Copyright 2021 Observable, Inc.
            // Released under the ISC license.
            // https://observablehq.com/@d3/bar-chart
            function HorizontalBarChart(data, {
                x = d => d, // given d in data, returns the (quantitative) x-value
                y = (d, i) => i, // given d in data, returns the (ordinal) y-value
                title, // given d in data, returns the title text
                marginTop = 30, // the top margin, in pixels
                marginRight = 0, // the right margin, in pixels
                marginBottom = 10, // the bottom margin, in pixels
                marginLeft = 105, // the left margin, in pixels
                width = 640, // the outer width of the chart, in pixels
                height, // outer height, in pixels
                xType = d3.scaleLinear, // type of x-scale
                xDomain, // [xmin, xmax]
                xRange = [marginLeft, width - marginRight], // [left, right]
                xFormat, // a format specifier string for the x-axis
                xLabel, // a label for the x-axis
                yPadding = 0.1, // amount of y-range to reserve to separate bars
                yDomain, // an array of (ordinal) y-values
                yRange, // [top, bottom]
                color = "currentColor", // bar fill color
                titleColor = "white", // title fill color when atop bar
                titleAltColor = "currentColor", // title fill color when atop background
            } = {}) {
                const X = d3.map(data, x);
                const Y = d3.map(data, y);

                // Compute default domains, and unique the y-domain.
                if (xDomain === undefined) xDomain = [0, d3.max(X)];
                if (yDomain === undefined) yDomain = Y;
                yDomain = new d3.InternSet(yDomain);

                // Omit any data not present in the y-domain.
                const I = d3.range(X.length).filter(i => yDomain.has(Y[i]));

                // Compute the default height.
                if (height === undefined) height = Math.ceil((yDomain.size + yPadding) * 25) + marginTop + marginBottom;
                if (yRange === undefined) yRange = [marginTop, height - marginBottom];

                // Construct scales and axes.
                const xScale = xType(xDomain, xRange);
                const yScale = d3.scaleBand(yDomain, yRange).padding(yPadding);
                const xAxis = d3.axisTop(xScale).ticks(width / 80, xFormat);
                const yAxis = d3.axisLeft(yScale).tickSizeOuter(0);

                // Compute titles.
                if (title === undefined) {
                    const formatValue = xScale.tickFormat(100, xFormat);
                    title = i => `${formatValue(X[i])}`;
                } else {
                    const O = d3.map(data, d => d);
                    const T = title;
                    title = i => T(O[i], i, data);
                }

                const svg = d3.create("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .attr("viewBox", [0, 0, width, height])
                    .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

                svg.append("g")
                    .attr("transform", `translate(0,${marginTop})`)
                    .call(xAxis)
                    .call(g => g.select(".domain").remove())
                    .call(g => g.selectAll(".tick line").clone()
                        .attr("y2", height - marginTop - marginBottom)
                        .attr("stroke-opacity", 0.1))
                    .call(g => g.append("text")
                        .attr("x", width - marginRight)
                        .attr("y", -22)
                        .attr("fill", "currentColor")
                        .attr("text-anchor", "end")
                        .text(xLabel));

                svg.append("g")
                    .attr("fill", color)
                    .selectAll("rect")
                    .data(I)
                    .join("rect")
                    .attr("x", xScale(0))
                    .attr("y", i => yScale(Y[i]))
                    .attr("width", i => xScale(X[i]) - xScale(0))
                    .attr("height", yScale.bandwidth())
                    .on("click", vm.clickRect)
                    .attr("id", function (d, i) {
                        let index = i
                        return vm.id + "-rect-" + index
                    });

                svg.append("g")
                    .attr("fill", titleColor)
                    .attr("text-anchor", "end")
                    .attr("font-family", "sans-serif")
                    .attr("font-size", 10)
                    .selectAll("text")
                    .data(I)
                    .join("text")
                    .attr("id", function (d, i) {
                        let index = i
                        return vm.id + "-text-" + index
                    })
                    .attr("x", i => xScale(X[i]))
                    .attr("y", i => yScale(Y[i]) + yScale.bandwidth() / 2)
                    .attr("dy", "0.35em")
                    .attr("dx", -4)
                    .text(title)
                    .call(text => text.filter(i => xScale(X[i]) - xScale(0) < 20) // short bars
                        .attr("dx", +4)
                        .attr("fill", titleAltColor)
                        .attr("text-anchor", "start"));

                svg.append("g")
                    .attr("transform", `translate(${marginLeft},0)`)
                    .call(yAxis);

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