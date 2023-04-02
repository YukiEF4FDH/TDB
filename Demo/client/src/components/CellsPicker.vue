<script>
import { PolymerElement, html } from '@polymer/polymer';
import '@polymer/paper-button/paper-button.js';
import { render, h } from 'vue'
import { eventPromise } from '@syncfusion/ej2-grids';
import { ElSteps, ElStep, ElRow, ElCol, ElButton, ElIcon } from 'element-plus'
// import MarkdownCell from './MarkdownCell.vue';
// import Sec1Table1 from './Sections/Sec1/Sec1Table1.vue'
// import VisCellCreator from './VisCellCreator.vue'
import { createApp } from 'vue'
import SectionBlockList from '@/components/SectionBlockList.vue'

import {
    Check,
    Delete,
} from '@element-plus/icons-vue'
import TextCell from '@/components/TextCell.vue';
import $ from 'jquery'
import SpreadsheetCell from '@/components/SpreadsheetCell.vue';
import VisCellCreator from '@/components/VisCellCreator.vue';
import TableCellCreator from '@/components/TableCellCreator.vue';
import { props } from '@syncfusion/ej2-vue-spreadsheet/src/spreadsheet/spreadsheet.component';
import ChartCell from '@/components/ChartCell.vue';
let vm = null;
let singleColIsSelected = true
let doubleColIsSelected = false
let scCellsIsSelected = [true, false, false]
let dcCellsIsSelected = [false, false, false, false, false, false]

let CellsPicker = {
    name: "CellsPicker",
    components: {
        layoutInlineIsActivated: true,
        layoutAsideIsActivated: false,
        ElSteps,
        ElStep,
        ElRow,
        ElCol,
        ElButton,
        ElIcon,
        Check,
        Delete,
        // VisCellCreator,
        TextCell,
        VisCellCreator,
        SpreadsheetCell,
        SectionBlockList,
    },
    data() {
        return {
            id: "cells-picker-0",
        };
    },
    methods: {
        selectSingleColumn(event) {
            let doubleColumnButton = document.getElementsByClassName("layout-button double-column")[0]
            doubleColumnButton.removeAttribute("active")

            let singleColumnButton = document.getElementsByClassName("layout-button single-column")[0]
            singleColumnButton.setAttribute("active", "")

            let singleColumnCellSelectionPanel = document.getElementsByClassName("selection-single-column-cell")[0]
            singleColumnCellSelectionPanel.style.display = "block"

            let doubleColCellSelectionPanel1 = document.getElementsByClassName("selection-double-column-cells-left")[0]
            let doubleColCellSelectionPanel2 = document.getElementsByClassName("selection-double-column-cells-right")[0]
            doubleColCellSelectionPanel1.style.display = "none"
            doubleColCellSelectionPanel2.style.display = "none"

            let textCell = document.getElementsByClassName("single-col-cell-text-1")[0]
            let visCell = document.getElementsByClassName("single-col-cell-text-2")[0]
            let tableCell = document.getElementsByClassName("single-col-cell-text-3")[0]

            textCell.setAttribute("active", "")
            visCell.removeAttribute("active")
            tableCell.removeAttribute("active")

            let textCellLogo = document.getElementsByClassName("single-col-text-cell-logo")[0]
            let visCellLogo = document.getElementsByClassName("single-col-vis-cell-logo")[0]
            let tableCellLogo = document.getElementsByClassName("single-col-table-cell-logo")[0]

            textCellLogo.style.display = "block"
            visCellLogo.style.display = "none"
            tableCellLogo.style.display = "none"

            singleColIsSelected = true
            doubleColIsSelected = false
            scCellsIsSelected = [true, false, false]
            dcCellsIsSelected = [false, false, false, false, false, false]

            document.getElementById("stepsBar-SC-TX").style.display="flex"
            document.getElementById("stepsBar-SC-V").style.display="none"
            document.getElementById("stepsBar-SC-TB").style.display="none"
            document.getElementById("stepsBar-DC").style.display="none"

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColumn(event) {
            let doubleColumnButton = document.getElementsByClassName("layout-button double-column")[0]
            doubleColumnButton.setAttribute("active", "")

            let singleColumnButton = document.getElementsByClassName("layout-button single-column")[0]
            singleColumnButton.removeAttribute("active")

            let singleColumnCellSelectionPanel = document.getElementsByClassName("selection-single-column-cell")[0]
            singleColumnCellSelectionPanel.style.display = "none"

            let doubleColCellSelectionPanel1 = document.getElementsByClassName("selection-double-column-cells-left")[0]
            let doubleColCellSelectionPanel2 = document.getElementsByClassName("selection-double-column-cells-right")[0]
            doubleColCellSelectionPanel1.style.display = "block"
            doubleColCellSelectionPanel2.style.display = "block"

            vm.selectDoubleColTextCellLeft(null)

            singleColIsSelected = false
            doubleColIsSelected = true
            scCellsIsSelected = [false, false, false]
            dcCellsIsSelected = [true, false, false, false, true, false]
            
            document.getElementById("stepsBar-SC-TX").style.display="none"
            document.getElementById("stepsBar-SC-V").style.display="none"
            document.getElementById("stepsBar-SC-TB").style.display="none"
            document.getElementById("stepsBar-DC").style.display="flex"

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectSingleColTextCell(event) {
            let textCell = document.getElementsByClassName("single-col-cell-text-1")[0]
            let visCell = document.getElementsByClassName("single-col-cell-text-2")[0]
            let tableCell = document.getElementsByClassName("single-col-cell-text-3")[0]
            textCell.setAttribute("active", "")
            visCell.removeAttribute("active")
            tableCell.removeAttribute("active")

            let textCellLogo = document.getElementsByClassName("single-col-text-cell-logo")[0]
            let visCellLogo = document.getElementsByClassName("single-col-vis-cell-logo")[0]
            let tableCellLogo = document.getElementsByClassName("single-col-table-cell-logo")[0]
            textCellLogo.style.display = "block"
            visCellLogo.style.display = "none"
            tableCellLogo.style.display = "none"

            scCellsIsSelected = [true, false, false]

            document.getElementById("stepsBar-SC-TX").style.display="flex"
            document.getElementById("stepsBar-SC-V").style.display="none"
            document.getElementById("stepsBar-SC-TB").style.display="none"

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectSingleColVisCell(event) {
            let textCell = document.getElementsByClassName("single-col-cell-text-1")[0]
            let visCell = document.getElementsByClassName("single-col-cell-text-2")[0]
            let tableCell = document.getElementsByClassName("single-col-cell-text-3")[0]
            textCell.removeAttribute("active")
            visCell.setAttribute("active", "")
            tableCell.removeAttribute("active")

            let textCellLogo = document.getElementsByClassName("single-col-text-cell-logo")[0]
            let visCellLogo = document.getElementsByClassName("single-col-vis-cell-logo")[0]
            let tableCellLogo = document.getElementsByClassName("single-col-table-cell-logo")[0]
            textCellLogo.style.display = "none"
            visCellLogo.style.display = "block"
            tableCellLogo.style.display = "none"

            document.getElementById("stepsBar-SC-TX").style.display="none"
            document.getElementById("stepsBar-SC-V").style.display="flex"
            document.getElementById("stepsBar-SC-TB").style.display="none"

            scCellsIsSelected = [false, true, false]

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)

        },
        selectSingleColTableCell(event) {
            let textCell = document.getElementsByClassName("single-col-cell-text-1")[0]
            let visCell = document.getElementsByClassName("single-col-cell-text-2")[0]
            let tableCell = document.getElementsByClassName("single-col-cell-text-3")[0]
            textCell.removeAttribute("active")
            visCell.removeAttribute("active")
            tableCell.setAttribute("active", "")

            let textCellLogo = document.getElementsByClassName("single-col-text-cell-logo")[0]
            let visCellLogo = document.getElementsByClassName("single-col-vis-cell-logo")[0]
            let tableCellLogo = document.getElementsByClassName("single-col-table-cell-logo")[0]
            textCellLogo.style.display = "none"
            visCellLogo.style.display = "none"
            tableCellLogo.style.display = "block"

            document.getElementById("stepsBar-SC-TX").style.display="none"
            document.getElementById("stepsBar-SC-V").style.display="none"
            document.getElementById("stepsBar-SC-TB").style.display="flex"

            scCellsIsSelected = [false, false, true]

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColTextCellLeft(event) {
            let textCell1 = document.getElementById("double-col-cell-text-left1")
            let visCell1 = document.getElementById("double-col-cell-text-left2")
            let tableCell1 = document.getElementById("double-col-cell-text-left3")
            textCell1.setAttribute("active", "")
            visCell1.removeAttribute("active")
            tableCell1.removeAttribute("active")

            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            textCell2.removeAttribute("active")
            textCell2.setAttribute("disabled", "")
            visCell2.setAttribute("active", "")
            visCell2.removeAttribute("disabled")
            tableCell2.removeAttribute("active")
            tableCell2.removeAttribute("disabled")

            let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
            let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
            let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
            textCellLogo1.style.display = "block"
            visCellLogo1.style.display = "none"
            tableCellLogo1.style.display = "none"

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            textCellLogo2.style.display = "none"
            visCellLogo2.style.display = "block"
            tableCellLogo2.style.display = "none"

            dcCellsIsSelected = [true, false, false, false, true, false]
            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColVisCellLeft(event) {
            let textCell1 = document.getElementById("double-col-cell-text-left1")
            let visCell1 = document.getElementById("double-col-cell-text-left2")
            let tableCell1 = document.getElementById("double-col-cell-text-left3")
            textCell1.removeAttribute("active")
            visCell1.setAttribute("active", "")
            tableCell1.removeAttribute("active")

            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            textCell2.setAttribute("active", "")
            textCell2.removeAttribute("disabled")
            visCell2.removeAttribute("active")
            visCell2.setAttribute("disabled", "")
            tableCell2.removeAttribute("active")
            tableCell2.removeAttribute("disabled")

            let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
            let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
            let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
            textCellLogo1.style.display = "none"
            visCellLogo1.style.display = "block"
            tableCellLogo1.style.display = "none"

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            visCellLogo2.style.display = "none"
            textCellLogo2.style.display = "block"
            tableCellLogo2.style.display = "none"

            dcCellsIsSelected = [false, true, false, true, false, false]
            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)

        },
        selectDoubleColTableCellLeft(event) {
            let textCell1 = document.getElementById("double-col-cell-text-left1")
            let visCell1 = document.getElementById("double-col-cell-text-left2")
            let tableCell1 = document.getElementById("double-col-cell-text-left3")
            textCell1.removeAttribute("active")
            visCell1.removeAttribute("active")
            tableCell1.setAttribute("active", "")

            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            textCell2.setAttribute("active", "")
            textCell2.removeAttribute("disabled")
            visCell2.removeAttribute("active")
            visCell2.removeAttribute("disabled")
            tableCell2.setAttribute("disabled", "")
            tableCell2.removeAttribute("active")

            let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
            let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
            let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
            textCellLogo1.style.display = "none"
            visCellLogo1.style.display = "none"
            tableCellLogo1.style.display = "block"

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            textCellLogo2.style.display = "block"
            visCellLogo2.style.display = "none"
            tableCellLogo2.style.display = "none"

            dcCellsIsSelected = [false, false, true, true, false, false]
            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColTextCellRight(event) {
            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            textCell2.setAttribute("active", "")
            visCell2.removeAttribute("active")
            tableCell2.removeAttribute("active")

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            textCellLogo2.style.display = "block"
            visCellLogo2.style.display = "none"
            tableCellLogo2.style.display = "none"

            dcCellsIsSelected[3] = true
            dcCellsIsSelected[4] = false
            dcCellsIsSelected[5] = false

            let textCell1 = document.getElementById("double-col-cell-text-left1")
            if (textCell1.hasAttribute("active")) {
                let visCell1 = document.getElementById("double-col-cell-text-left2")
                let tableCell1 = document.getElementById("double-col-cell-text-left3")
                textCell1.removeAttribute("active")
                visCell1.setAttribute("active", "")
                tableCell1.setAttribute("disabled", "")
                tableCell1.removeAttribute("active")

                let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
                let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
                let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
                textCellLogo1.style.display = "none"
                visCellLogo1.style.display = "block"
                tableCellLogo1.style.display = "none"

                dcCellsIsSelected[0] = false
                dcCellsIsSelected[1] = true
                dcCellsIsSelected[2] = false
            }

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColVisCellRight(event) {

            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            textCell2.removeAttribute("active")
            visCell2.setAttribute("active", "")
            tableCell2.removeAttribute("active")

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            textCellLogo2.style.display = "none"
            visCellLogo2.style.display = "block"
            tableCellLogo2.style.display = "none"

            dcCellsIsSelected[3] = false
            dcCellsIsSelected[4] = true
            dcCellsIsSelected[5] = false

            let visCell1 = document.getElementById("double-col-cell-text-left2")
            if (visCell1.hasAttribute("active")) {
                let textCell1 = document.getElementById("double-col-cell-text-left1")
                let tableCell1 = document.getElementById("double-col-cell-text-left3")
                visCell1.removeAttribute("active")
                visCell1.setAttribute("disabled", "")
                textCell1.setAttribute("active", "")
                tableCell1.removeAttribute("active")

                let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
                let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
                let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
                textCellLogo1.style.display = "block"
                visCellLogo1.style.display = "none"
                tableCellLogo1.style.display = "none"

                dcCellsIsSelected[0] = true
                dcCellsIsSelected[1] = false
                dcCellsIsSelected[2] = false
            }

            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        selectDoubleColTableCellRight(event) {

            let textCell2 = document.getElementById("double-col-cell-text-right1")
            let visCell2 = document.getElementById("double-col-cell-text-right2")
            let tableCell2 = document.getElementById("double-col-cell-text-right3")
            visCell2.removeAttribute("active")
            tableCell2.setAttribute("active", "")
            textCell2.removeAttribute("active")

            let textCellLogo2 = document.getElementById("double-col-text-cell-logo2")
            let visCellLogo2 = document.getElementById("double-col-vis-cell-logo2")
            let tableCellLogo2 = document.getElementById("double-col-table-cell-logo2")
            textCellLogo2.style.display = "none"
            visCellLogo2.style.display = "none"
            tableCellLogo2.style.display = "block"

            dcCellsIsSelected[3] = false
            dcCellsIsSelected[4] = false
            dcCellsIsSelected[5] = true

            let tableCell1 = document.getElementById("double-col-cell-text-left3")
            if (tableCell1.hasAttribute("active")) {
                let textCell1 = document.getElementById("double-col-cell-text-left1")
                let visCell1 = document.getElementById("double-col-cell-text-left2")
                tableCell1.removeAttribute("active")
                tableCell1.setAttribute("disabled", "")
                textCell1.setAttribute("active", "")
                visCell1.removeAttribute("active")

                let textCellLogo1 = document.getElementById("double-col-text-cell-logo1")
                let visCellLogo1 = document.getElementById("double-col-vis-cell-logo1")
                let tableCellLogo1 = document.getElementById("double-col-table-cell-logo1")
                textCellLogo1.style.display = "block"
                visCellLogo1.style.display = "none"
                tableCellLogo1.style.display = "none"

                dcCellsIsSelected[0] = true
                dcCellsIsSelected[1] = false
                dcCellsIsSelected[2] = false
            }
            // console.log("---------------------")
            // console.log(singleColIsSelected)
            // console.log(doubleColIsSelected)
            // console.log(scCellsIsSelected)
            // console.log(dcCellsIsSelected)
        },
        activateLeftTextCell() {

        },
        onClickCheck(event) {

            var wrap = function (toWrap, wrapper) {
                toWrap.parentNode.appendChild(wrapper);
                return wrapper.appendChild(toWrap);
            };

            let eventCurrentTarget = event.currentTarget
            let thisCellsPicker = eventCurrentTarget.parentNode.parentNode.parentNode
            let thisCPId = thisCellsPicker.id
            let thisCP = document.getElementById(thisCPId)
            while (thisCP.firstChild) {
                thisCP.removeChild(thisCP.firstChild);
            }
            thisCP.remove()

            let strs = thisCPId.split('-');
            let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];
            let thisAddCells = document.getElementById("add-cells-" + suf)
            thisAddCells.style.removeProperty('display');

            let thisSecBlock = document.getElementById("section-block-" + strs[strs.length - 2])
            let childrenOfThisSB = thisSecBlock.children
            let newIndex = 0
            for (const child of childrenOfThisSB) {
                if (child.className == "el-row" || child.tagName == "EL-ROW") {
                    if (child.children && child.children.length == 2) {
                        newIndex += 2
                    }
                    else if (child.children && child.children.length == 1) {
                        newIndex += 1
                    }
                }
            }

            if (singleColIsSelected) {
                if (scCellsIsSelected[0]) { // single-col Text Cell
                    let el = document.createElement("div")
                    el.setAttribute("id", "test-div")
                    const tcProps = {
                        index: newIndex,
                        sbIndex: strs[strs.length - 2],
                        layout: 'single-column',
                        textData: '**Double Click** to edit the content here. <ref>Ref</ref> refers to the data reference, <claim>Claim</claim> refers to the calculated value from the tabular data.',
                        startNewLine: false,
                    }
                    let referenceNode = thisAddCells
                    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);
                    let mdCellId = "markdown-cell-" + strs[strs.length - 2] + "-" + newIndex

                    const newTC = createApp(TextCell, tcProps)
                    newTC.mount('#test-div')
                    let cnt = $("#test-div").contents();
                    $("#test-div").replaceWith(cnt);
                }
                else if (scCellsIsSelected[1]) // single-col Vis Cell
                {
                    let el = document.createElement("div")
                    el.setAttribute("id", "test-div")

                    let referenceNode = thisAddCells
                    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);

                    let newTCProps = {
                        index: newIndex,
                        sbIndex: strs[strs.length - 2]
                    }
                    const newTC = createApp(VisCellCreator, newTCProps)
                    newTC.mount('#test-div')
                    let cnt = $("#test-div").contents();
                    $("#test-div").replaceWith(cnt);
                }
                else if (scCellsIsSelected[2]) // single-col Table Cell
                {
                    let el = document.createElement("div")
                    el.setAttribute("id", "test-div")

                    let referenceNode = thisAddCells
                    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);

                    let newTCProps = {
                        index: newIndex,
                        sbIndex: strs[strs.length - 2]
                    }
                    const newTC = createApp(TableCellCreator, newTCProps)
                    newTC.mount('#test-div')
                    let cnt = $("#test-div").contents();
                    $("#test-div").replaceWith(cnt);
                }
                // else if (scCellsIsSelected[2]) {

                // }
                // else {

                // }
            }
            else if (doubleColIsSelected) {
                if (dcCellsIsSelected[0]) {
                    let el = document.createElement("div")
                    el.setAttribute("id", "test-div1")
                    const tcProps = {
                        index: 0,
                        sbIndex: strs[strs.length - 2],
                        layout: 'double-column',
                        textData: '**Double Click** to edit the content here. <ref>Ref</ref> refers to the data reference, <claim>Claim</claim> refers to the calculated value from the tabular data.',
                        startNewLine: false,
                    }
                    let referenceNode = thisAddCells
                    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);

                    const newTC = createApp(TextCell, tcProps)
                    newTC.mount('#test-div1')
                    let cnt = $("#test-div1").contents();
                    // console.log(cnt)
                    $("#test-div1").replaceWith(cnt);

                    let createdTC = document.getElementById("text-content-container-1-0")
                    console.log(createdTC)
                    console.log(createdTC.parentElement.parentElement)
                    console.log(createdTC.parentElement.parentElement.parentElement)
                    let newRow = createdTC.parentElement.parentElement

                    let el2 = document.createElement("div")
                    el2.setAttribute("id", "test-div2")
                    newRow.appendChild(el2)

                    let col = <el-column style="width: 50%"></el-column>
                    render(col, el2)
                    col = el2.firstChild
                    let elrow = createdTC.parentElement.parentElement.parentElement
                    elrow.appendChild(col.cloneNode(true))
                    el2.remove()

                    let secondCol = elrow.children[1]
                    console.log(secondCol)

                    let el3 = document.createElement("div")
                    el3.setAttribute("id", "test-div3")
                    secondCol.appendChild(el3)
                    let newTCProps = {
                        index: 0,
                        sbIndex: strs[strs.length - 2]
                    }
                    const newTC2 = createApp(VisCellCreator, newTCProps)
                    newTC2.mount('#test-div3')
                    let cnt3 = $("#test-div3").contents();
                    $("#test-div3").replaceWith(cnt3);
                }
            }

        },
        onClickDelete(event) {
            let cs = document.getElementsByClassName("cells-picker-cell")[0]
            cs.style.display = "none"

        }
    },
    computed: {},
    created() {
    },
    mounted() {
        vm = this;

        const thisEleId = vm.$refs.cp.id
        vm.id = thisEleId
    },
};


export default CellsPicker;

</script>

<template>
    <div class="cells-picker-cell" ref="cp">
        <!-- <VisCellCreator /> -->
        <el-row class="cells-picker-step-bar-cell" style="margin-bottom: 5px;">
            <el-col class="el-col-layout" :span="22">
                <el-steps class="el-steps-sc" :space="325" :active="2" finish-status="success" id="stepsBar-SC-TX">
                    <el-step title="Select the Layout" description="Single or Double Column(s)" />
                    <el-step title="Select the Cell Type" description="Text Cell, Vis Cell or Table Cell" />
                    <el-step title="Click the Add Button" description="Add the Empty Text Cell" />
                    <el-step title="Try to Input Something!" description="Edit the Text Content In the Editor!" />
                </el-steps>
                <el-steps class="el-steps-sc" :space="325" :active="2" finish-status="success" id="stepsBar-SC-V" style="display: none">
                    <el-step title="Select the Layout" description="Single or Double Column(s)" />
                    <el-step title="Select the Cell Type" description="Text Cell, Vis Cell or Table Cell" />
                    <el-step title="Click the Add Button" description="Add The Empty Vis Cell" />
                    <el-step title="Select the CSV File" description="The Data to be Visualized" />
                    <el-step title="Select the Chart Type" description="The Basic Chart Types" />
                </el-steps>
                <el-steps class="el-steps-sc" :space="325" :active="2" finish-status="success" id="stepsBar-SC-TB"  style="display: none">
                    <el-step title="Select the Cell Layout" description="Single or Double Column(s)" />
                    <el-step title="Select the Component" description="Text, Vis or Table Component" />
                    <el-step title="Click the Add Button" description="Insert the Table Component" />
                    <el-step title="Select the CSV File" description="The Data to be Presented In the Table" />
                </el-steps>
                <el-steps :space="325" :active="3" finish-status="success" id="stepsBar-DC"  style="display: none" >
                    <el-step title="Select the Layout" description="Single or Double Column(s)" />
                    <el-step title="Select the Cell Type (Left)" description="Text Cell, Vis Cell or Table Cell" />
                    <el-step title="Select the Cell Type (Right)" description="Text Cell, Vis Cell or Table Cell" />
                    <el-step title="Click the Add Button" description="Add The Empty Cells" />
                    <el-step title="(Other operations)" description="..." />
                </el-steps>
            </el-col>
            <!-- 上面的都是 进度条的el-col :span="22"       check按钮的el-col style="margin-left: -3%;"  -->
            <!-- <el-col class="el-col-dc" :span="10" id="stepsBar-DC-L-TX">
                <el-steps :space="325" :active="1" finish-status="success">
                    <el-step title="(Click the Add Button)" description="The Empty Table Cells are Added" />
                    <el-step title="Try to Input Something! (Left)"
                        description="Edit the Text Content In the Editor!" />
                </el-steps>
            </el-col> -->
            <!-- <el-col class="el-col-dc" :span="14" id="stepsBar-DC-L-V">
                <el-steps :space="325" :active="1" finish-status="success">
                    <el-step title="(Click the Add Button)" description="The Empty Table Cells are Added" />
                    <el-step title="Select the CSV File (Right)" description="The Data to be Visualized" />
                    <el-step title="Select the Chart Type (Right)" description="The Basic Chart Types" />
                </el-steps>
            </el-col> -->
            <!-- <el-col class="el-col-dc" :span="10" style="display: initial" id="stepsBar-DC-L-TB">
                <el-steps :space="325" :active="1" finish-status="success">
                    <el-step title="(Click the Add Button)" description="The Empty Table Cells are Added" />
                    <el-step title="Select the CSV File(s) (Right)"
                        description="The Data to be Presented In the Table" />
                </el-steps>
            </el-col> -->
            <!-- <el-col class="el-col-dc" :span="6" style="margin-left: 3%; display: initial " id="stepsBar-DC-R-TX">
                <el-steps :space="325" :active="0" finish-status="success">
                    <el-step title="Try to Input Something! (Left)"
                        description="Edit the Text Content In the Editor!" />
                </el-steps>
            </el-col> -->
            <!-- <el-col class="el-col-dc" :span="10" style="margin-left: 3%;" id="stepsBar-DC-R-V">
                <el-steps :space="325" :active="0" finish-status="success">
                    <el-step title="Select the CSV File (Right)" description="The Data to be Visualized" />
                    <el-step title="Select the Chart Type (Right)" description="The Basic Chart Types" />
                </el-steps>
            </el-col> -->
            <!-- <el-col class="el-col-dc" :span="6" style="margin-left: 3%;" id="stepsBar-DC-R-TB">
                <el-steps :space="325" :active="0" finish-status="success">
                    <el-step title="Select the CSV File(s) (Right)" description="The Data to be Presented In the Table" />
                </el-steps>
            </el-col> -->
            <!-- 单栏的按钮 -->
            <el-col :span="1" style="margin-left: -3%;">
                <el-button size="large" type="success" @click="onClickCheck($event)">
                    <el-icon style="vertical-align: middle;">
                        <Check />
                    </el-icon>
                </el-button>
                <div class="center">
                    <p style="color:darkolivegreen">Add</p>
                </div>
            </el-col>
            <el-col :span="1" style="margin-left: 3%;">
                <el-button size="large" type="danger" @click="onClickDelete($event)">
                    <el-icon style="vertical-align: middle;">
                        <Delete />
                    </el-icon>
                </el-button>
                <div class="center">
                    <p style="color:darkred">Cancel</p>
                </div>
            </el-col>
            <!-- 双栏的按钮 -->
            <!-- <el-col :span="1" style="margin-left: 2%; ">
                    <el-button size="large" type="success" @click="onClickCheck($event)">
                        <el-icon style="vertical-align: middle;" @click="onClickCheck($event)">
                            <Check @click="onClickCheck($event)" />
                        </el-icon>
                    </el-button>
                    <div class="center">
                        <p style="color:darkolivegreen">Add</p>
                    </div>
                </el-col>
                <el-col :span="1" style="margin-left: 3%; ">
                    <el-button size="large" type="danger" @click="onClickDelete($event)">
                        <el-icon style="vertical-align: middle;" @click="onClickDelete($event)">
                            <Delete @click="onClickDelete($event)" />
                        </el-icon>
                    </el-button>
                    <div class="center">
                        <p style="color:darkred">Cancel</p>
                    </div>
                </el-col> -->
        </el-row>
        <div class="selection-layout">
            <paper-button toggles raised active class="layout-button single-column" @click="selectSingleColumn($event)">
                <div class="layout-button-text">New Cell:<br />
                    Single<br />Column</div>
                <div class="layout-button-logo">
                    <img class="selection-layout-logo" src="@/assets/new_inline_cell_logo.png" width="120"
                        height="95" />
                </div>
            </paper-button>
            <paper-button toggles raised class="layout-button double-column" @click="selectDoubleColumn($event)">
                <div class="layout-button-text">New Cells:<br />
                    double<br />
                    columns</div>
                <div class="layout-button-logo">
                    <img class="selection-layout-logo" src="@/assets/new_aside_cells_logo.png" width="120"
                        height="95" />
                </div>
            </paper-button>
        </div>
        <div class="selection-single-column-cell">
            <div class="single-column-cell-text">
                <paper-button toggles raised active class="single-col-cell-text-1"
                    @click="selectSingleColTextCell($event)">
                    TEXT COMPONENT
                </paper-button>
                <paper-button toggles raised class="single-col-cell-text-2" @click="selectSingleColVisCell($event)">
                    VISUALIZATION COMPONENT
                </paper-button>
                <paper-button toggles raised class="single-col-cell-text-3" @click="selectSingleColTableCell($event)">
                    TABLE COMPONENT
                </paper-button>
            </div>
            <div class="single-col-text-cell-logo">
                <img class="text-cell-logo" src="@/assets/text-cell-logo.png" width="470" height="200" />
            </div>
            <div class="single-col-vis-cell-logo">
                <img class="vis-cell-logo" src="@/assets/vis-cell-logo-2.png" width="470" height="220" />
            </div>
            <div class="single-col-table-cell-logo">
                <img class="table-cell-logo" src="@/assets/table-cell-logo-2.png" width="470" height="200" />
            </div>
            <!-- <paper-button toggles raised active class="single-column-uploaded-csv">
                Select Uploaded CSV
            </paper-button>
            <paper-button toggles raised class="single-column-new-csv">
                Upload New CSV
            </paper-button>
            <div class="single-col-vis-cell-logo">
                <img class="vis-cell-logo" src="@/assets/vis-cell-logo.png" width="240" height="220" />
            </div>
            <div class="single-col-table-cell-logo">
                <img class="table-cell-logo" src="@/assets/table-cell-logo.png" />
            </div> -->
        </div>
        <div class="selection-double-column-cells-left">
            <div>
                <div class="double-column-cell-text">
                    <paper-button toggles raised active class="double-col-cell-text" id="double-col-cell-text-left1"
                        @click="selectDoubleColTextCellLeft($event)">
                        TEXT<br />COMPONENT</paper-button>
                    <paper-button toggles raised class="double-col-cell-text" id="double-col-cell-text-left2"
                        @click="selectDoubleColVisCellLeft($event)">
                        VIS<br />COMPONENT </paper-button>
                    <paper-button toggles raised class="double-col-cell-text" id="double-col-cell-text-left3"
                        @click="selectDoubleColTableCellLeft($event)">
                        TABLE<br />COMPONENT</paper-button>
                </div>
                <div class="double-col-text-cell-logo" id="double-col-text-cell-logo1">
                    <img class="text-cell-logo-small" src="@/assets/text-cell-logo.png" />
                </div>
                <!-- <paper-button toggles raised active class="double-column-uploaded-csv" id="double-column-uploaded-csv1">
                    Select<br />Uploaded<br />CSV
                </paper-button>
                <paper-button toggles raised class="double-column-new-csv" id="double-column-new-csv1">
                    Upload<br />New <br />CSV
                </paper-button> -->
                <div class="double-col-vis-cell-logo" id="double-col-vis-cell-logo1">
                    <img class="vis-cell-logo-small" src="@/assets/vis-cell-logo-2.png" />
                </div>
                <div class="double-col-table-cell-logo" id="double-col-table-cell-logo1">
                    <img class="table-cell-logo-small" src="@/assets/table-cell-logo-2.png" />
                </div>
            </div>
        </div>
        <div class="selection-double-column-cells-right">
            <div class="double-column-cell-text">
                <paper-button toggles raised disabled class="double-col-cell-text" id="double-col-cell-text-right1"
                    @click="selectDoubleColTextCellRight($event)">
                    TEXT<br />COMPONENT</paper-button>
                <paper-button toggles raised active class="double-col-cell-text" id="double-col-cell-text-right2"
                    @click="selectDoubleColVisCellRight($event)">
                    VIS<br />COMPONENT</paper-button>
                <paper-button toggles raised class="double-col-cell-text" id="double-col-cell-text-right3"
                    @click="selectDoubleColTableCellRight($event)">
                    TABLE<br />COMPONENT</paper-button>
            </div>
            <div class="double-col-text-cell-logo" id="double-col-text-cell-logo2">
                <img class="text-cell-logo-small" src="@/assets/text-cell-logo.png" />
            </div>
            <!-- <paper-button toggles raised active class="double-column-uploaded-csv" id="double-column-uploaded-csv2">
                Select<br />Uploaded<br />CSV
            </paper-button>
            <paper-button toggles raised class="double-column-new-csv" id="double-column-new-csv2">
                Upload<br />New <br />CSV
            </paper-button> -->
            <div class="double-col-vis-cell-logo" id="double-col-vis-cell-logo2">
                <img class="vis-cell-logo-small" src="@/assets/vis-cell-logo-2.png" />
            </div>
            <div class="double-col-table-cell-logo" id="double-col-table-cell-logo2">
                <img class="table-cell-logo-small" src="@/assets/table-cell-logo-2.png" />
            </div>
        </div>
    </div>
</template>

<style scoped>

.cells-picker-cell{
    margin-top: 2%;
    margin-bottom: 2%;
}
.el-row {
    margin-bottom: 20px;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    /* border-radius: 4px; */
    min-height: 36px;
}

.selection-layout {
    width: 29%;
    min-height: 300px;
    display: block;
    /* position: flex;
    flex-direction: row; */
    background-color: #f7f7f7;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-right: 1%;
}

/* .layout-inline {
    min-height: 120px;
    width: 94%;
    background-color: #ffffff;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-top: 20px;
    margin-bottom: 10px;
    margin-inline: 3%;
    display: inline-block;
} */

/* .layout-aside {
    min-height: 120px;
    width: 94%;
    background-color: #ffffff;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-top: 10px;
    margin-bottom: 20px;
    margin-inline: 3%;
    display: inline-block;
} */

.selection-single-column-cell {
    width: 69%;
    min-height: 300px;
    display: block;
    /* position: flex;
    flex-direction: row; */
    background-color: #f7f7f7;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-left: 31%;
    margin-top: -300px;
}

.selection-double-column-cells-left {
    width: 34%;
    min-height: 300px;
    /* display: block; */
    display: none;
    /* position: flex;
    flex-direction: row; */
    background-color: #f7f7f7;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-left: 31%;
    margin-top: -300px;
}

.selection-double-column-cells-right {
    width: 34%;
    min-height: 300px;
    /* display: block; */
    /* position: flex;
    flex-direction: row; */
    display: none;
    background-color: #f7f7f7;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-left: 66%;
    margin-top: -300px;
}


.cell-types-aside {
    display: block;
    /* display: none; */

}

.cell-types-inline {
    /* display: none; */
    height: 260px;
    width: 94%;
    /* position: flex;
    flex-direction: row; */
    background-color: #ffffff;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-top: 20px;
    margin-bottom: 20px;
    margin-inline: 3%;
    display: inline-block;
}

.cell-type-left {
    height: 260px;
    width: 46%;
    /* position: flex;
    flex-direction: row; */
    background-color: #ffffff;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-top: 20px;
    margin-bottom: 20px;
    margin-inline: 3%;
    display: inline-block;
}

.cell-type-right {
    height: 260px;
    background-color: #ffffff;
    width: 46%;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-right: 3%;
    margin-top: -30%;
    margin-left: 51%;
}

div.container-fluid {
    padding-left: 0px;
    padding-right: 0px;
    background-color: red;
}

paper-button.layout-button {
    height: 120px;
    width: 94%;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%), 0 2px 4px -1px rgb(0 0 0 / 40%);
    margin-inline: 3%;
    display: inline-block;
}

paper-button.single-column {
    margin-top: 20px;
    margin-bottom: 10px;
}

paper-button.double-column {
    margin-top: 10px;
    margin-bottom: 20px;
}

paper-button[active] {
    /* background-color: var(--paper-red-500); */
    /* font: bold; */
    background-color: white;
    font-weight: bold;
}

.layout-button-text {
    /* background-color: blue; */
    margin-left: 15%;
    margin-top: 1%;
    margin-bottom: 1%;
    width: 30%;
    height: 90px;

    text-align: left;
    vertical-align: middle;
    line-height: 30px;
    font-size: 16px;
}

.layout-button-logo {
    /* background-color: red; */
    width: 62%;
    margin-left: 35%;
    margin-top: -93px;
    height: 90px;
}

.single-column-cell-text {}

.single-col-cell-text-1 {
    margin-left: 1.5%;
    /* background-color: green; */
    width: 30%;
    height: 70px;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);

    text-align: center;
    vertical-align: middle;
    font-size: 24px;

    margin-top: 2.5%;
    display: inline-block;
}

.single-col-cell-text-3 {
    margin-left: 1.5%;
    margin-top: 1%;
    /* background-color: green; */
    width: 30%;
    height: 70px;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);

    text-align: center;
    font-size: 22px;

    margin-top: 2.5%;
    display: block;

    line-height: 25px;
}

.single-col-cell-text-2 {
    margin-left: 1.5%;
    /* margin-top: 1%; */
    /* background-color: green; */
    width: 30%;
    height: 70px;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);

    text-align: center;
    font-size: 20px;

    margin-top: 2.5%;
    display: block;

    line-height: 25px;
}

.single-col-text-cell-logo {
    margin-left: 38%;
    margin-top: -27.5%;
    /* background-color: pink; */
    width: 55%;
    height: 235px;
    /* display: none; */
}

.single-column-uploaded-csv {
    margin-left: 33%;
    width: 32%;
    height: 120px;
    margin-top: -29.5%;

    text-align: center;
    font-size: 20px;
    line-height: 90px;


    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    /* display: block; */
    display: none;
}

.single-column-new-csv {
    margin-left: 33%;
    width: 32%;
    height: 120px;
    margin-top: 2%;

    text-align: center;
    font-size: 20px;
    line-height: 90px;

    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);
    /* display: block; */
    display: none;
}

.single-col-vis-cell-logo {
    margin-left: 38%;
    margin-top: -27.5%;
    /* background-color: pink; */
    width: 55%;
    height: 235px;
    display: none;
}

.single-col-table-cell-logo {
    margin-left: 38%;
    margin-top: -27.5%;
    /* background-color: pink; */
    width: 55%;
    height: 235px;
    display: none;
}


.double-col-cell-text {
    margin-left: 2%;
    /* background-color: green; */
    width: 30%;
    height: 80px;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);

    text-align: center;
    vertical-align: middle;
    font-size: 17px;

    margin-top: 3.5%;
    display: inline-block;
    line-height: 30px;
}


.double-col-cell-text-1 {
    margin-left: 2%;
    /* background-color: green; */
    width: 14%;
    height: 70px;
    background-color: #f4f4f5;
    box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
        0 2px 4px -1px rgb(0 0 0 / 40%);

    text-align: center;
    vertical-align: middle;
    font-size: 14px;

    margin-top: 2.5%;
    display: inline-block;
}


.double-column-cell-text-vis {}

/* .double-column-cell-text-table {

} */

.double-col-text-cell-logo {
    width: 380px;
    margin-top: 4%;
    margin-left: 8%;
    display: none;
}

.text-cell-logo-small {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}

.vis-cell-logo-small {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}

.table-cell-logo-small {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}


.cell-type-right-text {
    margin-left: 3%;
    margin-top: 3.5%;
    /* background-color: green; */
    width: 30%;
    height: 89%;
}

.cell-type-right-logo {
    margin-left: 35%;
    margin-top: -53.9%;
    /* background-color: green; */
    width: 62%;
    height: 89%;
}

.selection-layout-logo {
    margin-left: 25%;
}

.text-cell-logo {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}

.vis-cell-logo {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}

.table-cell-logo {
    margin-inline: 0%;
    margin-top: 0%;
    margin-bottom: 0%;
    width: 100%;
    height: 100%;
}

.double-column-uploaded-csv {
    width: 45%;
    margin-top: 4.5%;
    margin-left: 2%;
    height: 80px;

    text-align: center;
    line-height: 20px;
    display: block;
}

.double-column-new-csv {
    width: 45%;
    margin-top: 2%;
    margin-left: 2%;
    height: 80px;
    display: block;

    text-align: center;
    line-height: 20px;
}

.double-col-vis-cell-logo {
    width: 380px;
    margin-top: 4%;
    margin-left: 8%;
    display: none;
}

.double-col-table-cell-logo {
    width: 380px;
    margin-top: 4%;
    margin-left: 8%;
    display: none;
}

.center {
    text-align: center;
    font-size: 16px;
    margin-top: 15px;
}
</style>
