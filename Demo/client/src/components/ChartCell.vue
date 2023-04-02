<template>
  <div class="chart-cell" :id="id">
    <component :is="visType" v-bind="visProps"></component>
  </div>
</template>

<script>
import axios from "axios";
import { ElColumn, ElRow } from 'element-plus'
import { render } from 'vue'
import AddCells from '@/components/AddCells.vue';
import BarChart from "@/components/ChartComponents/BarChart.vue"
import StackedBarChart_Normalized from "@/components/ChartComponents/StackedBarChart_Normalized.vue"
import HorizontalBarChart from "@/components/ChartComponents/HorizontalBarChart.vue"
import PieChart from "@/components/ChartComponents/PieChart.vue"
let vm = null;
var chartCell = null;
var f1aData = "default";


export default {
  name: "ChartCell",
  props: {
    index: null,
    sbIndex: null,
    layout: null,
    chartData: null,
    chartType: null,
    startNewLine: null,
  },
  data() {
    return {
      id: "chart-cell-" + this.sbIndex + "-" + this.index,
      layoutType: this.layout,
      data: this.chartData,
      visProps: {
        index: this.index,
        sbIndex: this.sbIndex,
        dataSourceURL: "http://127.0.0.1:5000/CSV/" + this.chartData,
      },
      visType: this.chartType,
      startNewLineForDBL: this.startNewLine,
      // clickedFragmentId: null,
    };
  },
  components: {
    'bar-chart': BarChart,
    'stacked-bar-chart-normalized': StackedBarChart_Normalized,
    'horizontal-bar-chart': HorizontalBarChart,
    'pie-chart': PieChart,
    AddCells,
  },
  methods: {

    getClickedFragmentId(id) {
      // console.log(getId + ": " + id)
      // return id;
    },
    setClickedFragmentId(id) {
      // vm.clickedFragmentId = id
    },
    ensureClickedFragmentIdIsSet() {
      // let start = Date.now();
      // return new Promise(waitForFoo);

      // function waitForFoo(resolve, reject) {
      //   if (vm.clickedFragmentId)
      //     resolve(vm.clickedFragmentId);
      //   else if (timeout && (Date.now() - start) >= timeout)
      //     reject(new Error("timeout"));
      //   else
      //     setTimeout(waitForFoo.bind(this, resolve, reject), 30);
      // }
    }
  },
  mounted() {
    vm = this;
    var chartCellContainer = document.querySelector("#" + vm.id).closest(".el-row");
    var nearestBlock = document.querySelector("#" + vm.id).closest(".section-block");

    // console.log(vm.data)
    // console.log(vm.visProps)
    // console.log(vm.visType)

    //=================================================================================
    // Arrange the Layout.
    let thisCell = document.getElementById(vm.id)

    var wrap = function (toWrap, wrapper) {
      toWrap.parentNode.appendChild(wrapper);
      return wrapper.appendChild(toWrap);
    };

    if (vm.layoutType == 'double-column') {

      // This cell: is the 2nd one of the 2 columns
      if (vm.startNewLineForDBL) {
        let wrapper = <el-column style="width: 50%;"></el-column>
        let el = document.createElement("div")
        render(wrapper, el)
        wrapper = el.childNodes[0]
        wrap(thisCell, wrapper)

        let elRowOfThisCell = thisCell.parentNode
        let elRowOfCellBeforeThisCell = elRowOfThisCell.previousSibling
        elRowOfThisCell = wrap(elRowOfThisCell, elRowOfCellBeforeThisCell)
        let strs = vm.id.split('-');
        let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];
        let addCellsNodeId = "add-cells-" + suf
        // let props = { index: strs[strs.length - 2], sbIndex: strs[strs.length - 1], }
        let addCellsNode = <AddCells />
        let newEl = document.createElement("div")
        render(addCellsNode, newEl)
        addCellsNode = newEl.firstChild
        let addCellsEle = newEl.firstElementChild
        addCellsEle.setAttribute("id", addCellsNodeId)
        // elRowOfThisCell = thisCell.parentNode.parentNode
        elRowOfThisCell.parentNode.parentNode.appendChild(addCellsNode)
      }

      // This cell: is the 1st one of the 2 columns
      else {
        let wrapper = <el-column style="width: 50%;"></el-column>
        let el = document.createElement("div")
        render(wrapper, el)
        wrapper = el.childNodes[0]
        thisCell = wrap(thisCell, wrapper)

        // This is POINTLESS but the rendering below won't work if I remove it.
        wrapper = <el-row ></el-row >
        el = document.createElement("div")
        render(wrapper, el)
        wrapper = el.childNodes[0]

        let elColumnOfThisCell = thisCell.parentNode
        let newWrapper = <el-row style="width: 100%; display: flex; flex-direction: row;"></el-row>
        let newEl = document.createElement("div")
        render(newWrapper, newEl)
        newWrapper = newEl.childNodes[0]
        elColumnOfThisCell = wrap(elColumnOfThisCell, newWrapper)
      }
    }
    else {
      let wrapper = <el-row></el-row>
      let el = document.createElement("div")
      render(wrapper, el)
      wrapper = el.childNodes[0]
      thisCell = wrap(thisCell, wrapper)

      let elRowOfThisCell = thisCell.parentNode
      let strs = vm.id.split('-');
      let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];
      let addCellsNodeId = "add-cells-" + suf
      let addCellsNode = <AddCells />
      let newEl = document.createElement("div")
      render(addCellsNode, newEl)
      addCellsNode = newEl.firstChild
      let addCellsEle = newEl.firstElementChild
      addCellsEle.setAttribute("id", addCellsNodeId)
      elRowOfThisCell.parentNode.appendChild(addCellsNode) // ??? Dont know why

    }
  },
};
</script>

<style scoped>
.chart-cell-container {
  width: 100%;
  margin-left: 2%;
  margin-right: 0%;
  margin-top: 1%;
  margin-bottom: 1%;
}

.chart-cell {
  min-height: 219px;
  width: 100%;
  height: 100%;
  /* background: green; */
}
</style>
