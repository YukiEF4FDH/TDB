<template>
  <el-row>
    <div class="section-block" :id="id">
      <component :is="cell.cellType" v-for="cell in cells" :key="cell.props.index" v-bind="cell.props"></component>
    </div>
  </el-row>
</template>

<script>
import TextCell from "@/components/TextCell.vue";
import ChartCell from "@/components/ChartCell.vue"
import SpreadsheetCell from "@/components/SpreadsheetCell.vue"
import { ElRow } from 'element-plus'


let vm = null;

var SectionBlock = {
  name: "SectionBlock",
  props: {
    index: 0,
    cellOrder: [],
    cellLayout: [],
    cellData: [],
    chartType: [],
  },
  data() {
    return {
      id: "section-block-" + this.index,
      cells: [
        // cellType = 'text-cell','chart-cell','spreadsheet-cell'
        // props = {index:..., sbIndex:..., layout:..., data:..., startNewLine:..., }
      ],
      countOfCells: 0,
    };
  },
  setup(props) {
  },
  methods: {
    printCellsOfThisSection() {

    }
  },
  components: {
    'text-cell': TextCell,
    'chart-cell': ChartCell,
    'spreadsheet-cell': SpreadsheetCell,
    'el-row': ElRow,
  },
  mounted() {
    vm = this;
    // For layout arrangement (double-column): whether start a new line
    vm.countOfCells = 0;

    // For each cell of this section block
    let numOfCells = vm.cellOrder.length;
    for (let i = 0; i < numOfCells; i++) {
      let type = vm.cellOrder[i]; // text-cell, vis-cell, spreadsheet-cell
      let cl = vm.cellLayout[i]; // double column, single column
      let startNewLineForDoubleCol = false; // For layout arrangement (double-column): Will start a new line for next cell
      if (cl == 'double-column')
        vm.countOfCells += 1; 
      else
        vm.countOfCells = 0;
      if (vm.countOfCells >= 2 || (cl == 'double-column' && vm.countOfCells == 0)) {
        // For layout arrangement (double-column): Will start a new line for next cell
        // -> this cell i is the 2nd cell on the right side in the double-column layout
        startNewLineForDoubleCol = true;
        vm.countOfCells = 0;
      }

      if (type === 'text-cell') {
        let textCell = {
          cellType: 'text-cell',
          props: {
            index: (i + 1),
            sbIndex: vm.index,
            layout: vm.cellLayout[i],
            textData: vm.cellData[i],
            startNewLine: startNewLineForDoubleCol,
            // data...
          }
        }
        vm.cells.push(textCell);
      }
      else if (type === 'chart-cell') {
        let chartCell = {
          cellType: 'chart-cell',
          props: {
            index: (i + 1),
            sbIndex: vm.index,
            layout: vm.cellLayout[i],
            chartData: vm.cellData[i],
            chartType: vm.chartType[i],
            startNewLine: startNewLineForDoubleCol,
            // data...
          }
        }
        vm.cells.push(chartCell);
      }
      else // 'spreadsheet-cell'
      {
        let spreadsheetCell = {
          cellType: 'spreadsheet-cell',
          props: {
            index: (i + 1),
            sbIndex: vm.index,
            layout: vm.cellLayout[i],
            tableData: vm.cellData[i],
            // chartType: vm.chartType[i],
            startNewLine: startNewLineForDoubleCol,
            // data...
          }
        }
        vm.cells.push(spreadsheetCell);
      }
    }

    var wrapper = document.createElement("div");

    // var wrap = function (toWrap, wrapper) {
    //   toWrap.parentNode.appendChild(wrapper);
    //   return wrapper.appendChild(toWrap);
    // };

    // wrap(document.getElementById('#'+vm.id).firstChild,wrapper);

    // console.log(document.getElementById(vm.id).childNodes);
    var nodeList = document.getElementById(vm.id).childNodes;
    // for (let i=0; i<nodeList.length; i++)
    // {
    //   console.log(nodeList[i]);
    // }
    // console.log(nodeList);

    document.addEventListener('DOMContentLoaded', function () {
      // console.log(document.getElementById(vm.id).childNodes);
      var nodeList = document.getElementById(vm.id).childNodes;
      for (let i = 0; i < nodeList.length; i++) {
        var node = nodeList[i];
        // if (node.nodeType===1)
        // console.log(node);

      }
      // console.log(nodeList);
    });

  },
  created() {
  },
};
export default SectionBlock;
</script>

<style scoped>
.section-block {
  /* background: orange; */
  display: flex;
  /* flex-direction: row; */
  flex-direction: column;
  margin-bottom: 0.5%;
  width: 100%;
}
</style>