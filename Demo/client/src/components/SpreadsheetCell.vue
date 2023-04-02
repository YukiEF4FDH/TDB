<template>
    <div class="spreadsheet-cell" :id="id">
        <spreadsheet v-bind="spreadsheetProps"></spreadsheet>
    </div>
</template>
  
<script>
import Spreadsheet from '@/components/SpreadsheetComponents/Spreadsheet.vue';
import { ElColumn, ElRow } from 'element-plus'
import { render } from 'vue'
import AddCells from '@/components/AddCells.vue';

var vm = null;

var SpreadsheetCell = {
    name: "SpreadsheetCell",
    components: {
        'spreadsheet': Spreadsheet,
        AddCells,
    },
    props: {
        index: null,
        sbIndex: null,
        layout: null,
        tableData: null,
        startNewLine: false,
    },
    data() {
        return {
            id: "spreadsheet-cell-" + this.sbIndex + "-" + this.index,
            sbId: "section-block-" + this.sbIndex,
            spreadsheetProps: {
                index: this.index,
                sbIndex: this.sbIndex,
                dataSourceURL: "http://127.0.0.1:5000/CSV/" + this.tableData,
                layout: this.layout,
            },
            layoutType: this.layout,
            startNewLineForDBL: this.startNewLine,
        }
    },
    methods: {

    },
    mounted() {
        vm = this;
        let thisCell = document.getElementById(vm.id)
        var nearestSecBlockOfThisCell = document.querySelector("#" + vm.id).closest(".section-block");
        let idStrs = vm.id.split('-');
        let idSuf = idStrs[idStrs.length - 2] + '-' + idStrs[idStrs.length - 1];


        var wrap = function (toWrap, wrapper) {
            toWrap.parentNode.appendChild(wrapper);
            return wrapper.appendChild(toWrap);
        };

        if (vm.layoutType == 'double-column') {

            if (vm.startNewLineForDBL) { // This cell: The 2nd one
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
                let addCellsNode = <AddCells />
                let newEl = document.createElement("div")
                render(addCellsNode, newEl)
                addCellsNode = newEl.firstChild
                let addCellsEle = newEl.firstElementChild
                addCellsEle.setAttribute("id", addCellsNodeId)
                // elRowOfThisCell = thisCell.parentNode.parentNode
                elRowOfThisCell.parentNode.parentNode.appendChild(addCellsNode)
                // let newWrapper = <el-row style="width: 100%; display: flex; flex-direction:"></el-row>
                // let newEl = document.createElement("div")
                // render(newWrapper, newEl)
                // newWrapper = newEl.childNodes[0]
                // wrap(elRowOfCellBeforeThisCell, newWrapper)
                // newWrapper.appendChild(thisCell)
            }
            else { // This Cell: the 1st one.
                let wrapper = <el-column style="width: 50%;"></el-column>
                let el = document.createElement("div")
                render(wrapper, el)
                wrapper = el.childNodes[0]
                // console.log(wrapper)
                thisCell = wrap(thisCell, wrapper)
                // console.log(thisCell.parentNode)

                // This is POINTLESS but the rendering below won't work if I remove it.
                wrapper = <el-row ></el-row >
                el = document.createElement("div")
                render(wrapper, el)
                wrapper = el.childNodes[0]
                // console.log(wrapper)

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
            wrap(thisCell, wrapper)

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
            elRowOfThisCell.parentNode.appendChild(addCellsNode)
        }
    },
};

export default SpreadsheetCell;

</script>
  
<style scoped>
.spreadsheet-cell {
    width: 100%;
    overflow: visible;
    /* min-height: 250px; */
    height: auto;
}
</style>