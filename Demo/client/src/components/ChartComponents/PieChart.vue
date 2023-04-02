<template>
    <div :id="id" style="height: 100%; weight: 100%;">
        <div :id="svgId" class="vis-svg" @click="Hover($event)">
            <center>
                <p style="margin-top: 0%;" @dblclick="dbClickCap($event)">Double click to input the caption</p>
            </center>
        </div>
    </div>
</template>
  
<script>
import * as d3 from "d3";
import axios from "axios";
import mybutton from '@/components/mybutton.vue';
let isInputCap2 = false
let vm = null;

export default {
    name: "PieChart",
    props: {
        index: null,
        sbIndex: null,
        dataSourceURL: null,
    },
    data() {
        return {
            id: "pie-chart-" + this.sbIndex + "-" + this.index,
            svgId: "svg-" + this.sbIndex + "-" + this.index,
            dataURL: this.dataSourceURL,
            data: null
        };
    },
    components: {
        // ElButton,
        // ElIcon, Plus
    },
    methods: {
        Hover(event) { },
        dbClickCap(e) {
            let target = e.currentTarget
            let newInput = document.createElement("input")
            newInput.setAttribute("type", "text")
            newInput.setAttribute("id", "newInputId4")
            target.innerText = ""
            target.appendChild(newInput)
            isInputCap2 = true

            document.addEventListener('click', function (event) {
                if (isInputCap2 && (event.target.id != "newInputId4")) {
                    let newOutline = document.getElementById("newInputId4").value
                    newInput.remove()
                    target.innerText = newOutline
                    isInputCap2 = false
                }
            });
        },

        clickArc(event) {
            let arc = event.currentTarget
            let idSub = arc.id.split('-')[6]

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

            if (dataFactType == "ref") {
            d3.select(arc)
                .attr("fill", "#cae6b6")
                .attr("stroke", fontColor)
                .attr("stroke-width", "5")
                ;
                }
                else{
                    d3.select(arc)
                .attr("fill", "#fbb")
                .attr("stroke", fontColor)
                .attr("stroke-width", "5")
                ;
                }
            d3.select(document.getElementById(vm.id + "-text-" + idSub))
                .attr("fill", fontColor)
                .attr("font-weight", 700)
                .attr("font-size", 16)

            mybutton.methods.setClickedFragmentId(arc.id)
        },
        draw(data_, mySvgId) {
            // var population = data_

            let nameOfXY = Object.keys(data_[0])
            let nameOfX = nameOfXY[0]
            let nameOfY = nameOfXY[1]

            let mySvg = document.getElementById(mySvgId)
            let myWidth = mySvg.offsetWidth;
            let myHeight = mySvg.offsetHeight;

            var chart = PieChart(data_, {
                name: d => d[nameOfX],
                value: d => d[nameOfY],
                width: myWidth,
                height: myHeight,
            })

            mySvg.insertBefore(chart, mySvg.firstElementChild);

            // Copyright 2021 Observable, Inc.
            // Released under the ISC license.
            // https://observablehq.com/@d3/pie-chart
            function PieChart(data, {
                name = ([x]) => x,  // given d in data, returns the (ordinal) label
                value = ([, y]) => y, // given d in data, returns the (quantitative) value
                title, // given d in data, returns the title text
                width = 640, // outer width, in pixels
                height = 400, // outer height, in pixels
                innerRadius = 0, // inner radius of pie, in pixels (non-zero for donut)
                outerRadius = Math.min(width, height) / 2, // outer radius of pie, in pixels
                labelRadius = (innerRadius * 0.2 + outerRadius * 0.8), // center radius of labels
                format = ",", // a format specifier for values (in the label)
                names, // array of names (the domain of the color scale)
                colors, // array of colors for names
                stroke = innerRadius > 0 ? "none" : "white", // stroke separating widths
                strokeWidth = 1, // width of stroke separating wedges
                strokeLinejoin = "round", // line join of stroke separating wedges
                padAngle = stroke === "none" ? 1 / outerRadius : 0, // angular separation between wedges
            } = {}) {
                // Compute values.
                const N = d3.map(data, name);
                const V = d3.map(data, value);
                const I = d3.range(N.length).filter(i => !isNaN(V[i]));

                // Unique the names.
                if (names === undefined) names = N;
                names = new d3.InternSet(names);

                // Chose a default color scheme based on cardinality.
                if (colors === undefined) colors = d3.schemeSpectral[names.size];
                if (colors === undefined) colors = d3.quantize(t => d3.interpolateSpectral(t * 0.8 + 0.1), names.size);

                // Construct scales.
                const color = d3.scaleOrdinal(names, colors);

                // Compute titles.
                if (title === undefined) {
                    const formatValue = d3.format(format);
                    title = i => `${N[i]}\n${formatValue(V[i])}`;
                } else {
                    const O = d3.map(data, d => d);
                    const T = title;
                    title = i => T(O[i], i, data);
                }

                // Construct arcs.
                const arcs = d3.pie().padAngle(padAngle).sort(null).value(i => V[i])(I);
                const arc = d3.arc().innerRadius(innerRadius).outerRadius(outerRadius);
                const arcLabel = d3.arc().innerRadius(labelRadius).outerRadius(labelRadius);

                const svg = d3.create("svg")
                    .attr("width", width)
                    .attr("height", height)
                    .attr("viewBox", [-width / 2, -height / 2, width, height])
                    .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

                svg.append("g")
                    .attr("stroke", stroke)
                    .attr("stroke-width", strokeWidth)
                    .attr("stroke-linejoin", strokeLinejoin)
                    .selectAll("path")
                    .data(arcs)
                    .join("path")
                    .attr("fill", "steelblue")
                    .attr("id", function (d, i) {
                        let index = i
                        return vm.id + "-arc-" + index
                    })
                    .on("click", vm.clickArc)
                    .attr("d", arc)
                    .append("title")
                    .text(d => title(d.data))
                    ;

                svg.append("g")
                    .attr("font-family", "sans-serif")
                    .attr("font-size", 10)
                    .attr("text-anchor", "middle")
                    .selectAll("text")
                    .data(arcs)
                    .join("text")
                    .attr("id", function (d, i) {
                        let index = i
                        return vm.id + "-text-" + index
                    })
                    .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
                    .selectAll("tspan")
                    .data(d => {
                        const lines = `${title(d.data)}`.split(/\n/);
                        return (d.endAngle - d.startAngle) > 0.25 ? lines : lines.slice(0, 1);
                    })
                    .join("tspan")
                    .attr("x", 0)
                    .attr("y", (_, i) => `${i * 1.1}em`)
                    .attr("font-weight", (_, i) => i ? null : "bold")
                    .text(d => d);

                return Object.assign(svg.node(), { scales: { color } });
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