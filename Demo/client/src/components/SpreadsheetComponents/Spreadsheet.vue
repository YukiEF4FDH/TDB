<template>
  <div class="spreadsheet" :id="id">
    <ejs-spreadsheet :ref="id" :select="select" :openUrl="openUrl"
    :allowOpen="true">
      <e-sheets>
        <e-sheet>
          <e-ranges>
            <e-range :dataSource="dataSource"></e-range>
          </e-ranges>
        </e-sheet>
      </e-sheets>
    </ejs-spreadsheet>
  </div>
</template>
  
<script>
import axios from "axios";
import {
  SpreadsheetComponent,
  RangesDirective,
  RangeDirective,
  SheetsDirective,
  SheetDirective,
  // getRangeAddress,
} from "@syncfusion/ej2-vue-spreadsheet";
import mybutton from "@/components/mybutton.vue"

var vm = null;
// let scount = 0;
// let sid = "spreadsheet1" + scount;

var Spreadsheet = {
  name: "Spreadsheet",
  // Declaring component and its directives
  components: {
    "ejs-spreadsheet": SpreadsheetComponent,
    "e-sheets": SheetsDirective,
    "e-sheet": SheetDirective,
    "e-ranges": RangesDirective,
    "e-range": RangeDirective,
  },
  // Bound properties declarations
  props: {
    index: null,
    sbIndex: null,
    dataSourceURL: null,
    layout: null
  },
  data() {
    return {
      id: "spreadsheet-" + this.sbIndex + "-" + this.index,
      sbId: "section-block-" + this.sbIndex,
      dataURL: this.dataSourceURL,
      layoutType: this.layout,
      dataSource: null,
      sid: "spreadsheet1",
      openUrl: "https://ej2services.syncfusion.com/production/web-services/api/spreadsheet/open"
    };
  },
  mounted() {
    vm = this;
    // scount += 1;
    // sid = "spreadsheet" + scount;
    // vm.LoadData()

    const path = vm.dataURL;
    let loadedData = null;

    let thisId = vm.id;
    let thisSheet = vm.$refs[thisId].ej2Instances.sheets[0]

    axios
      .get(path)
      .then((res) => {
        loadedData = res.data;
        if (loadedData != "default") {
          loadedData = JSON.parse(loadedData);

          let columns = Object.keys(loadedData[0]);
          columns = columns.slice(0, columns.length - 1);
          loadedData.columns = columns;
          loadedData = loadedData.sort((a, b) => b[1] / b.total - a[1] / a.total);

          vm.dataSource = loadedData;

          thisSheet.ranges[0].dataSource = loadedData;
        }
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    select: async function (args) {
      var range = args.range;
      let id = this.id
      console.log(id)
      let sheet = vm.$refs[id]
      console.log(this);
      console.log(range);

      function sleep(ms) {
        return new Promise(resolveFunc => setTimeout(resolveFunc, ms));
      }

      let clickedDataFactId = mybutton.methods.getClickedDataFactId()
      if (clickedDataFactId) {
        let clickedDataFact = document.getElementById(clickedDataFactId)
        let clickedDataDactIdStr = clickedDataFactId.split("-")
        let dataFactType = clickedDataDactIdStr[clickedDataDactIdStr.length - 2]
        if (dataFactType == "ref") {
          sheet.cellFormat({ backgroundColor: '#cae6b6' }, range);
          await sleep(1000);
          sheet.cellFormat({ backgroundColor: '#ffffff' }, range);
          clickedDataFact.setAttribute("bind-table", range)
          clickedDataFact.setAttribute("table-id", id)
        }
        else {
          sheet.cellFormat({ backgroundColor: '#fbb' }, range);
          await sleep(1000);
          sheet.cellFormat({ backgroundColor: '#ffffff' }, range);
          clickedDataFact.setAttribute("bind-table", range)
          clickedDataFact.setAttribute("table-id", id)
        }

        document.getElementById("btn-"+clickedDataFactId).remove()
      }
    },
    handleHover(dataFactType, tableId, range) {
      let sheet = vm.$refs[tableId]
      if (dataFactType == "ref") {
        sheet.cellFormat({ backgroundColor: '#cae6b6' }, range);
      }
      else {
        sheet.cellFormat({ backgroundColor: '#fbb' }, range);
      }
    }
    ,
    handleLeave(dataFactType, tableId, range) {
      let sheet = vm.$refs[tableId]
      sheet.cellFormat({ backgroundColor: '#ffffff' }, range);
    }
  },
};
export default Spreadsheet;

</script>
  
<style>
@import "../../../node_modules/@syncfusion/ej2-base/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-buttons/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-dropdowns/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-inputs/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-navigations/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-popups/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-splitbuttons/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-grids/styles/material.css";
@import "../../../node_modules/@syncfusion/ej2-vue-spreadsheet/styles/material.css";

.spreadsheet {
  width: 100%;
  height: 100%;
}

.e-spreadsheet {
  min-height: 270px;
  max-height: 270px;
}
</style>