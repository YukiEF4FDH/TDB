<template>
  <div class="section-block-list" :id="id">
    <section-block v-for="sb in sectionBlocks" :key="sb.index" v-bind="sb">
    </section-block>
  </div>
</template>

<script>
import SectionBlock from "@/components/SectionBlock.vue";
import MarkdownCell from "./TextComponents/MarkdownCell.vue";
import axios from "axios";

let vm = null;
var chartData = [];
var chartFileNames = []; // JSON loaded from app.py
var specifications = null;
var cellTypesOfSB = [];
var cellLayoutsOfSB = [];
var cellDataOfSB = [];
var chartTypesOfSB = [];
var numOfSections = 0;

function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}

var SectionBlockList = {
  data() {
    return {
      id: "section-block-list",
      sectionBlocks: [
        // Will be filled in mounted() with the data loaded.

        // For a sectionBlock: Id, Order, Position and Data of TextCell and ChartCell and SpreadsheetCell.
        // e.g., index,
        //       [text-cell, chart-cell, text-cell, chart-cell, text-cell],
        //       [double-column,double-column,double-column,double-column, single-column],
        //       [...(data)],
      ]
    };
  },
  components: {
    'section-block': SectionBlock,
  },
  methods: {
    printSectionBlocks() {
      console.log(vm.sectionBlocks)
    },
    printIndexedSectionBlocks(secId) {
      console.log(vm.sectionBlocks[secId])
    },
    getCountOfCellsOfIndexedSecBlock(secId) {
      let indexedCell = vm.sectionBlocks[secId]
      console.log(indexedCell.cellOrder.length)
    }
  },
  mounted() {
    vm = this;

    // Load and Parse the Specifications.json
    function loadSpecifications() {
      let spEndpoint = "http://127.0.0.1:5000/" + "specifications-json";
      // This returns a Promise, i.e., req
      const req = axios.get(spEndpoint);
      return req;
    }

    loadSpecifications()
      .then(response => {
        let res = response.data;
        specifications = JSON.parse(res);
      })
      .then(() => {
        numOfSections = specifications.length;

        for (let i = 0; i < numOfSections; i++) {
          let cellTypes = [];
          let cellLayouts = [];
          let cellData = [];
          let chartTypes = [];

          for (let j = 0; j < Object.keys(specifications[i]).length; j++) {
            var val = specifications[i][j];
            if (val !== null) {
              cellTypes.push(val['cellType']);
              cellLayouts.push(val['cellLayout']);
              cellData.push(val['cellData']);
              if (val['cellType'] !== 'text-cell')
                chartFileNames.push(val['cellData']);

              chartTypes.push(val['chartType']);
            }
          }
          cellTypesOfSB.push(cellTypes);
          cellLayoutsOfSB.push(cellLayouts);
          cellDataOfSB.push(cellData);
          chartTypesOfSB.push(chartTypes);
        }
      })
      .then(() => {
        for (let i = 0; i < numOfSections; i++) {
          let sectionBlock = {
            index: (i + 1),
            cellOrder: cellTypesOfSB[i],
            cellLayout: cellLayoutsOfSB[i],
            cellData: cellDataOfSB[i],
            chartType: chartTypesOfSB[i],
            // Data...
          }
          vm.sectionBlocks.push(sectionBlock);
        }

      })
      .catch(error => {
        console.log(error)
      });

    //===============================================================================

    // For Text-Cell:
    // End the editing of the Markdown Editor by clicking outside of it.
    // document.addEventListener("click", function (event) {
    //   let ancestorT = event.target.closest(".text-cell");
    //   if (ancestorT === null) {
    //     MarkdownCell.methods.endEdit();
    //   }
    // });

  },
};

export default SectionBlockList;

</script>

<style scoped>
/* .section-block-list {
  display: flex;
  flex-direction: column;
} */
</style>