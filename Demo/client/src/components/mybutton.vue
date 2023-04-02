<template>
    <div :id="id">
        <el-popconfirm width="220" ref="popConfirm" confirm-button-text="Vis" cancel-button-text="Table"
            :icon="InfoFilled" icon-color="#626AEF" title="Bind To Vis or Table" confirm-button-type="text"
            cancel-button-type="text" hide-icon="true" @confirm="this.confirm" @cancel="this.cancel">
            <template #reference>
                <el-button ref="btn">Bind To Vis or Table</el-button>
            </template>
        </el-popconfirm>
    </div>
</template>

<script>
import $ from 'jquery';
import { ElColumn, ElRow, ElPopconfirm, ElButton } from 'element-plus'
import { InfoFilled } from '@element-plus/icons-vue'
import HorizontalBarChart from '@/components/ChartComponents/HorizontalBarChart.vue';
import ChartCell from '@/components/ChartCell.vue';
import { click } from '@syncfusion/ej2-spreadsheet';
import ref from '@/components/ref.vue';
import claim from '@/components/claim.vue';

let reference_id = 1;
let vm = null;
var timeout = 1000000;
var clickedDataFactIndex_ = null
var clickedDataFactType_ = null
let existingId = ""

export default {
    name: "mybutton",
    props: {
    },
    components: {
        ElPopconfirm, ElButton
        // compile,
    },
    data() {
        return {
            // clickedFragmentId: "0000"
            clickedDataFactIndex: null,
            clickedVisFragmentId: null,
            clickedTableFragmentId: null,
            id: "btn-"+clickedDataFactIndex_
        };
    },
    mounted() {
        vm = this
        let popconfirmEl = this.$refs.popConfirm.$el
        // console.log(popconfirmEl.parentElement.getAttribute('id'))
        let idStrs = popconfirmEl.parentElement.getAttribute('id').split("-")
        vm.clickedDataFactIndex = ""
        for (let i = 1; i < idStrs.length; i++) {
            if (i == 1) {
                vm.clickedDataFactIndex = vm.clickedDataFactIndex + idStrs[i]
            }
            else {
                vm.clickedDataFactIndex = vm.clickedDataFactIndex + "-" + idStrs[i]
            }
        }
        clickedDataFactIndex_ = vm.clickedDataFactIndex
        clickedDataFactType_ = clickedDataFactIndex_.split("-")[3]
        vm.id = "btn-"+clickedDataFactIndex_

        if (clickedDataFactType_ == "claim") {
            document.addEventListener("keyup", function (e) {
                if (e.key=="Control"){
                    claim.methods.removeBtn(vm.clickedDataFactIndex)
                }
            })
        }
    },
    methods: {
        getClickedDataFactId() {
            if (clickedDataFactIndex_)
                return clickedDataFactIndex_
            else
                return null
        },
        // getPromiseFromEvent(item, event) {
        //     return new Promise((resolve) => {
        //         const listener = () => {
        //             item.removeEventListener(event, listener);
        //             resolve();
        //         }
        //         item.addEventListener(event, listener);
        //     })
        // },
        setClickedFragmentId(id) {
            vm.clickedVisFragmentId = id
            // console.log("vm.clickedVisFragmentId")
            // console.log(vm.clickedVisFragmentId)
            // console.log("vm.clickedDataFactIndex")
            // console.log(vm.clickedDataFactIndex)

            const dataFactToBind = document.getElementById(vm.clickedDataFactIndex)
            dataFactToBind.setAttribute("bind-vis", vm.clickedVisFragmentId)
            if (dataFactToBind.className == "reference") {
                ref.methods.bindToVisFragment(vm.clickedDataFactIndex, vm.clickedVisFragmentId)
            }
            else if (dataFactToBind.className == "claim") {
                claim.methods.bindToVisFragment(vm.clickedDataFactIndex, vm.clickedVisFragmentId)
                claim.methods.appendToMyMap(vm.clickedDataFactIndex, vm.clickedVisFragmentId)
            }
        },
        ensureClickedFragmentIdIsSet() {
            // function waitForFoo(resolve, reject) {
            //     if (clickedFragmentId) {
            //         console.log(clickedFragmentId)
            //         resolve(clickedFragmentId);
            //     }
            //     else if (timeout && (Date.now() - start) >= timeout)
            //         reject(new Error("timeout"));
            //     else
            //         setTimeout(waitForFoo.bind(this, resolve, reject), 30);
            // }

            // let start = Date.now();
            // return new Promise(waitForFoo);
        },
        confirm(event) { //Vis

        },
        cancel(event) {
            
        }
    }
}
</script>

<style>

</style>