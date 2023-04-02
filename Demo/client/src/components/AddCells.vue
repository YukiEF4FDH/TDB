<script>
import { PolymerElement, html } from '@polymer/polymer';
import '@polymer/paper-button/paper-button.js';
// import ref from "@/components/ref.vue";
import { render } from 'vue'
import CellsPicker from "@/components/CellsPicker.vue"
import TextCell from "@/components/TextCell.vue"

let vm = null;
// let count_ac = 0;

var AddCells = {
    name: "AddCells",
    components: {
        CellsPicker,TextCell
    },
    // props: {
    //     index: null,
    //     sbIndex: null,
    // },
    data() {
        return {
            id: "add-cells-0",
        };
    },
    methods: {
        onHover(event) {
            if (document.getElementById(event.target.id).style.opacity != 100)
                document.getElementById(event.target.id).style.opacity = 100
        },
        onLeave(event) {
            if (document.getElementById(event.target.id).style.opacity != 0)
                document.getElementById(event.target.id).style.opacity = 0
        },
        onClickNewCells(event) {
            let parentNode = event.target.parentNode
            let parentParentNode = parentNode.parentNode

            let strs = parentParentNode.id.split('-');
            let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];

            let cellPickerNode = document.getElementById('cells-picker-'+suf)
            cellPickerNode.style.removeProperty('display');

            let thisAddCells = document.getElementById("add-cells-" + suf)
            thisAddCells.style.display = 'none';
        },
        onClickNewSection(event){
            let parentNode = event.target.parentNode
            let parentParentNode = parentNode.parentNode

            let strs = parentParentNode.id.split('-');
            let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];

            let cellPickerNode = document.getElementById('cells-picker-'+suf)
            cellPickerNode.style.removeProperty('display');

            let thisAddCells = document.getElementById("add-cells-" + suf)
            thisAddCells.style.display = 'none';
        }
    },
    computed: {},
    created() {
        // count_ac += 1;
        // this.id_ac = "id_ac" + count_ac;


    },
    mounted() {
        vm = this;
        const thisEleId = vm.$refs.ac.id
        vm.id = thisEleId

        //let parentNode = event.target.parentNode
        let parentParentNode = document.getElementById(vm.id)//parentNode.parentNode

        let strs = parentParentNode.id.split('-');
        let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];
        let cellsPickerNodeId = "cells-picker-" + suf
        let el = document.createElement("div")
        let vnode = <CellsPicker />
        render(vnode, el)
        let cellPickerEle = el.firstElementChild
        cellPickerEle.setAttribute("id", cellsPickerNodeId)
        let cellPickerNode = el.firstChild

        let referenceNode = parentParentNode
        referenceNode.parentNode.insertBefore(cellPickerNode, referenceNode.nextSibling);

        cellPickerNode.style.display = 'none';
    },
};


export default AddCells;

</script>

<template>
    <div class="add-cell" @mouseover="onHover($event)" @mouseleave="onLeave($event)" ref="ac">
        <div class="add-cell-buttons">
            <paper-button raised class="indigo" @click="onClickNewCells($event)" style="height: 10px;"> New
                Cell(s)</paper-button>
            <paper-button raised class="indigo" @click="onClickNewSection($event)" style="height: 10px;"> New
                Section</paper-button>
        </div>
        <hr>
    </div>
</template>

<style scoped>
paper-button.indigo {
    background-color: white;
    color: black;
}

.add-cell {
    align-items: center;
    align-self: center;
    display: flex;
    flex-flow: column;
    height: 16px;
    position: relative;
    width: 100%;
    margin-top: 2%;
    margin-bottom: 2%;
    opacity: 0;
    transition: opacity 200ms;
}

.add-cell-buttons {
    display: flex;
    font-family: var(--colab-chrome-font-family);
    margin-top: -4px;
    z-index: 20;
}

.add-cell>hr {
    border-color: darkgrey;
    border-style: solid;
    border-top: none;
    border-width: 1px;
    left: 20px;
    position: absolute;
    right: 20px;
    top: 0;
    /* transition: visibility 0s 250ms, opacity 200ms; */
    /* visibility: hidden; */
}
</style>
