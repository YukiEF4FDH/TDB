<script>
import { PolymerElement, html } from '@polymer/polymer';
import '@polymer/paper-button/paper-button.js';
import { render, createApp } from 'vue'
import { eventPromise } from '@syncfusion/ej2-grids';
import { ElRow, ElCol, ElButton, ElIcon, ElDropdown, ElDropdownMenu, ElDropdownItem, ElUpload } from 'element-plus'
import {
    Check,
    Delete,
    Plus,
    ArrowDown,
    Right
} from '@element-plus/icons-vue'
// import BarChart_ from "@/components/Visualization/BarChart_.vue";
// import PieChart from "@/components/Visualization/PieChart.vue"
// import GroupedBarChart from '@/components/Visualization/GroupedBarChart.vue';
import ChartCell from "@/components/ChartCell.vue";
import { Chart } from '@syncfusion/ej2-spreadsheet';
import $ from 'jquery'

var vm = null;

var VisCellCreator = {
    name: "VisCellCreator",
    props: {
        index: null,
        sbIndex: null,
    },
    components: {
        ElRow, ElCol, Check, Plus, ElButton, ElIcon, ElDropdown, ArrowDown, ElDropdownMenu, ElDropdownItem, Right, ElUpload,
        // BarChart_, PieChart, GroupedBarChart
        ChartCell,
    },
    data() {
        return {
            selectedFileName: null,
            id: this.index,
            sbId: this.sbIndex,
        };
    },
    methods: {
        barChartClick(event) {
            let el = document.createElement("div")
            el.setAttribute("id", "test-div")
            let thisAddCells = document.getElementById('vis-cell-creator')
            const tbcProps = {
                index: vm.id,
                sbIndex: vm.sbId,
                layout: 'single-column',
                chartData: vm.selectedFileName,
                chartType: 'horizontal-bar-chart',
                startNewLine: false,
            }
            let referenceNode = thisAddCells
            referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);

            const newTC = createApp(ChartCell, tbcProps)
            newTC.mount('#test-div')
            let cnt = $("#test-div").contents();
            $("#test-div").replaceWith(cnt);

            thisAddCells.remove()
            // let visCellCreatorNode = document.getElementById("vis-cell-creator")
            // while (visCellCreatorNode.firstChild) {
            //     visCellCreatorNode.removeChild(visCellCreatorNode.firstChild);
            // }

            // let cellsSelectionNode = document.getElementById("cs-test")
            // //  = visCellCreatorNode.parentNode
            // while (cellsSelectionNode.firstChild) {
            //     cellsSelectionNode.removeChild(cellsSelectionNode.firstChild);
            // }

            // let vnode = <BarChart_ />
            // let el = document.createElement("div")
            // render(vnode, el)

            // cellsSelectionNode.appendChild(el)
        },
        groupedBarChartClick(event) {
            // let visCellCreatorNode = document.getElementById("vis-cell-creator")
            // while (visCellCreatorNode.firstChild) {
            //     visCellCreatorNode.removeChild(visCellCreatorNode.firstChild);
            // }

            // let cellsSelectionNode = document.getElementById("cs-test")
            // //  = visCellCreatorNode.parentNode
            // while (cellsSelectionNode.firstChild) {
            //     cellsSelectionNode.removeChild(cellsSelectionNode.firstChild);
            // }

            // let vnode = <GroupedBarChart />
            // let el = document.createElement("div")
            // render(vnode, el)

            // cellsSelectionNode.appendChild(el)
        },
        pieChartClick(event) {
            let el = document.createElement("div")
            el.setAttribute("id", "test-div")
            let thisAddCells = document.getElementById('vis-cell-creator')
            const tbcProps = {
                index: vm.id,
                sbIndex: vm.sbId,
                layout: 'single-column',
                chartData: vm.selectedFileName,
                chartType: 'pie-chart',
                startNewLine: false,
            }
            let referenceNode = thisAddCells
            referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);

            const newTC = createApp(ChartCell, tbcProps)
            newTC.mount('#test-div')
            let cnt = $("#test-div").contents();
            $("#test-div").replaceWith(cnt);

            thisAddCells.remove()

            let newChartCell = document.getElementById("chart-cell-1-0")
            let newAddCells = document.getElementById("add-cells-1-0")
            let newCellsPicker = document.getElementById("cells-picker-1-0")
            let col2 = newChartCell.parentNode.parentNode
            let dbRow = col2.parentNode

            dbRow.parentElement.insertBefore(newAddCells,dbRow.nextSibling)//.appendChild(newAddCells)
            dbRow.parentElement.insertBefore(newCellsPicker,dbRow.nextSibling)//.appendChild(newAddCells)
            // // let chart = $("#chart-cell-1-0").contents();
            

            // console.log(newChartCell)
            // console.log(newAddCells)
            // console.log(col2)
            // // console.log(col2.firstChild.firstChild)
            // col2.replaceChild(col2.firstChild,newChartCell)
            // console.log(col2)
            // // let cntOfChartCell = ("#"+col2.firstChild.firstChild.id)
            // console.log(dbRow)
        },
        dropdownMenuClick(event) {
            let el = document.getElementsByClassName("el-dropdown-link")[0]
            let fileName = event.currentTarget.innerText
            el.textContent = fileName

            vm.selectedFileName = fileName.split(".")[0]
            // while (el.firstChild) {
            //     el.removeChild(el.firstChild);
            // }

            // let htmlString = `TestData.csv <el-icon class="el-icon--right"> <arrow-down />`
            // el.innerHTML = htmlString.trim();

            // let vnode = 
            // let el = document.createElement("div")
            // render(vnode, el)

            // cellsSelectionNode.appendChild(el)
        },
        onSuccess() {
            console.log("success!!")
        }
    },
    computed: {},
    created() {
    },
    mounted() {
        vm = this;
    },
};


export default VisCellCreator;

</script>


<template>
    <el-row id="vis-cell-creator">
        <el-col :span="12">
            <div class="vis-cell-picker">
                <div class="pick-vis-type">
                    <el-col>
                        <div class="text center">Pick an Exisiting File</div>
                        <el-dropdown trigger="click" class="center" style="margin-top: -3%;" :hide-on-click="true">
                            <span class="el-dropdown-link" id="selectedItem">
                                Uploaded CSV<el-icon class="el-icon--right">
                                    <arrow-down />
                                </el-icon>
                            </span>
                            <template #dropdown>
                                <el-dropdown-menu>
                                    <el-dropdown-item @click="dropdownMenuClick($event)">Table1.csv</el-dropdown-item>
                                    <el-dropdown-item @click="dropdownMenuClick($event)">Table2A.csv</el-dropdown-item>
                                    <el-dropdown-item @click="dropdownMenuClick($event)">Table2B.csv</el-dropdown-item>
                                    <el-dropdown-item @click="dropdownMenuClick($event)">Table2C.csv</el-dropdown-item>
                                    <el-dropdown-item @click="dropdownMenuClick($event)">Table3.csv</el-dropdown-item>
                                </el-dropdown-menu>
                            </template>
                        </el-dropdown>
                    </el-col>
                </div>
                <hr class="center" />
                <div class="pick-new-csv    ">
                    <el-upload action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                        on-success="onSuccess">
                        <el-icon class="center" style="margin-top: -2%;">
                            <Plus />
                        </el-icon>
                        <div class="text center">Pick a New CSV File</div>
                    </el-upload>
                </div>
            </div>
        </el-col>
        <el-col :span="12">
            <div class="vis-cell-picker" style="overflow-y: scroll;">
                <el-row>
                    <el-col :span="12">
                        <img src="@/assets/bar-chart.png" @click="barChartClick($event)"
                            style="width: 95%; height: 95%;" />
                    </el-col>
                    <el-col :span="12">
                        <img src="@/assets/grouped-bar-chart.png" @click="groupedBarChartClick($event)"
                            style="width: 95%; height: 95%;" />
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <img src="@/assets/stacked-bar-chart.png" style="width: 95%; height: 95%;" />
                    </el-col>
                    <el-col :span="12">
                        <img src="@/assets/stacked-bar-chart-normalized.png" style="width: 95%; height: 95%;" />
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <img src="@/assets/horizontal-bar-chart.png" style="width: 95%; height: 95%;"  @click="barChartClick($event)"/>
                    </el-col>
                    <el-col :span="12">
                        <img src="@/assets/pie-chart.png" @click="pieChartClick($event)"
                            style="width: 95%; height: 95%;" />
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <img src="@/assets/scatterplot.png" style="width: 95%; height: 95%;" />
                    </el-col>
                    <el-col :span="12">
                        <img src="@/assets/bubble-chart.png" style="width: 95%; height: 95%;" />
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <img src="@/assets/bar-chart.png" style="width: 95%; height: 95%;" />
                    </el-col>
                    <el-col :span="12">
                        <img src="@/assets/grouped-bar-chart.png" style="width: 95%; height: 95%;" />
                    </el-col>
                </el-row>
            </div>
        </el-col>
    </el-row>
</template>

<style scoped>
.vis-cell-picker {
    cursor: pointer;
    position: relative;
    background: #fff;
    border: 2px dashed #b8c0cc;
    border-radius: 4px;
    transition: border .2s ease;
    box-sizing: border-box;
    min-height: 300px;
    max-height: 300px;
}

.vis-cell-picker .pick-vis-type {
    position: absolute;
    /* top: 50%; */
    width: 100%;
    /* transform: translateY(-50%); */
    /* background: pink; */
    height: 50%;
}

.vis-cell-picker .pick-new-csv {
    position: absolute;
    top: 50%;
    width: 100%;
    /* transform: translateY(-50%); */
    /* background: #666; */
    height: 50%;
}

.vis-cell-picker .text {
    line-height: 16px;
    margin-top: 16px;
    /* color: #666; */
}

div {
    margin: 0;
    padding: 0;
    border: 0;
    vertical-align: baseline;
}

.center {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}

.vis-cell-picker>hr {
    border-color: darkgrey;
    border-style: solid;
    border-top: none;
    border-width: 1px;
    position: absolute;
    right: -0.5%;
}

.demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
}
</style>
