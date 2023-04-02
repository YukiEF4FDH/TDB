<template>
  <span class="reference" :ref="reference" :id="this.id">
    <slot>
      {{ text }}
    </slot>
  </span>
</template>

<script>
import $ from 'jquery';
let reference_id = 1;
let vm = null;
import mybutton from "@/components/mybutton.vue"
import { ElPopconfirm, ElButton } from 'element-plus'
import { render } from 'vue'
import * as d3 from "d3";
import Spreadsheet from '@/components/SpreadsheetComponents/Spreadsheet.vue';

const cell_RefCount_Map = new Map();
const refContnt_RefId_Map = new Map();
const refId_bindVisFragmentId_Map = new Map();

let rectA = null
let rectB = null
let rectC = null

export default {
  name: "ref",
  components: {
    // mybutton, ElButton, ElPopconfirm
  },
  props: {
    textData: null,
  },
  data() {
    return {
      id: "ref-" + reference_id,
      text: this.textData,
      bindVis: null,
      bindTable: null,
    };
  },
  created() {
    this.id = "ref" + reference_id; // data.id更新
    reference_id++;

    const _default = this.$slots.default();
    if (_default && _default.length > 0)
      this.text = _default[0].children; // data.text更新
  },
  mounted() {
    let refEl = document.getElementById(this.id)

    if (!refEl) // mounted from Markdown Components, display=none
    {
      this.id = null
    }
    else {
      let refElParent = refEl.parentElement
      let refElParentParent = refElParent.parentElement
      let strs = refElParentParent.id.split("-")
      let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];

      if (!cell_RefCount_Map.get(suf)) {
        cell_RefCount_Map.set(suf, 1)
      }
      else {
        let refCountOfThisCell = cell_RefCount_Map.get(suf)
        // console.log(refCountOfThisCell)
        cell_RefCount_Map.set(suf, refCountOfThisCell + 1)
      }

      let newId = "cell-" + suf + "-ref-" + cell_RefCount_Map.get(suf)
      this.id = newId
      refEl.setAttribute("id", newId)

      let textContent = refElParent.innerText
      let refContent = this.text
      let refIndexInCell = suf// + "-" + textContent.indexOf(refContent)
      let refId = newId

      // refIndexInCell_RefContent.set(refIndexInCell, refContent)
      // refIndexInCell_RefId.set(refIndexInCell, refId)
      refContnt_RefId_Map.set(refContent, refId)
    }

    if (refEl) {
      refEl.addEventListener('mouseover', this.setHover)
      refEl.addEventListener('mouseout', this.setOut)
      refEl.addEventListener('click', this.setClick)
    }
  },
  methods: {
    setHover(event) {
      console.log("hover")
      let target = event.currentTarget;
      let targetId = target.getAttribute("id")
      let hoveredTarget = document.getElementById(targetId)
      target = hoveredTarget

      let rectRef = target.getBoundingClientRect()

      if (target.hasAttribute("bind-vis")) {
        // console.log(target.getAttribute("bind-vis"))
        let boundVisFragmentId = target.getAttribute("bind-vis")
        let boundVisFragment = document.getElementById(boundVisFragmentId)
        let fragmentStr = boundVisFragmentId.split("-")
        let fragment = fragmentStr[fragmentStr.length - 2]
        // console.log(fragment)
        let boundVisFragmentTextId = boundVisFragmentId.replace(fragment, "text")
        let boundVisFragmentText = document.getElementById(boundVisFragmentTextId)

        let rectVis = boundVisFragment.getBoundingClientRect()
        rectB = rectVis

        console.log(rectA)
        console.log(rectB)

        console.log(rectA.x+rectA.width*0.5)
        console.log(rectA.y+rectA.height*0.5)
        console.log(rectB.x+rectB.width*0.5)
        console.log(rectB.y+rectB.height*0.5)

        let x1 = rectA.x+rectA.width*0.5
        let y1 = rectA.y+rectA.height*0.5
        let x2 = rectB.x+rectB.width*0.5
        let y2 = rectB.y+rectB.height*0.5

        let newSvg = document.createElement("svg")
        newSvg.style.display = "absolute"
        newSvg.style.display = "absolute"
        newSvg.style.display = "absolute"

        d3.select(boundVisFragment)
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5")

        d3.select(boundVisFragmentText)
          .attr("fill", "#aabe9b")
          .attr("font-weight", 700)
          .attr("font-size", 16)
      }
      if (target.hasAttribute("bind-table")) {
        let tableId = target.getAttribute("table-id")
        let range = target.getAttribute("bind-table")
        Spreadsheet.methods.handleHover("ref", tableId, range)
      }
    },
    setOut(event) {
      let target = event.currentTarget;
      let targetId = target.getAttribute("id")
      let hoveredTarget = document.getElementById(targetId)
      target = hoveredTarget
      if (target.hasAttribute("bind-vis")) {
        // console.log(target.getAttribute("bind-vis"))
        let boundVisFragmentId = target.getAttribute("bind-vis")
        let boundVisFragment = document.getElementById(boundVisFragmentId)
        let fragmentStr = boundVisFragmentId.split("-")
        let fragment = fragmentStr[fragmentStr.length - 2]
        // console.log(fragment)
        let boundVisFragmentTextId = boundVisFragmentId.replace(fragment, "text")
        let boundVisFragmentText = document.getElementById(boundVisFragmentTextId)

        d3.select(boundVisFragment)
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("fill", "steelblue")
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("stroke", "")
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("stroke-width", "")

        d3.select(boundVisFragmentText)
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("fill", "")
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("font-weight", "plain")
          .transition() // <------- TRANSITION STARTS HERE --------
          .delay(function (d, i) { return 100 * i; })
          .duration(1000)
          .attr("font-size", 10)
      }
      if (target.hasAttribute("bind-table")) {
        let tableId = target.getAttribute("table-id")
        let range = target.getAttribute("bind-table")
        Spreadsheet.methods.handleLeave("ref", tableId, range)
      }
    },
    setClick(event) {
      // console.log("CLICK")
      let target = event.currentTarget;
      let targetRect = target.getBoundingClientRect();
      rectA = targetRect

      let dynamicId = "btn-" + target.id
      let mybtn = <mybutton id={dynamicId} />
      let el = document.createElement('div')
      let newY = targetRect.y + 20
      let newTop = targetRect.top + 20
      el.style.position = "fixed"
      el.style.x = targetRect.x + "px"
      el.style.y = newY + "px"
      el.style.left = targetRect.left + "px"
      el.style.top = newTop + "px"
      render(mybtn, el)
      target.parentNode.appendChild(el)
    },
    bindToVisFragment(refId, visFragmentId) {
      refId_bindVisFragmentId_Map.set(refId, visFragmentId)

      let refEl = document.getElementById(refId)
      let rectEl = document.getElementById(visFragmentId)
      console.log(rectEl)
      let rectTextId = ""
      if (visFragmentId.includes("rect")){
        rectTextId = visFragmentId.replace("rect", "text")
      }
      else{
        rectTextId = visFragmentId.replace("arc", "text")
      }
      let textEl = document.getElementById(rectTextId)
      let mybtnId = "btn-" + refId
      let mybtnEl = document.getElementById(mybtnId)
      mybtnEl.remove()

      d3.select(rectEl)
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("fill", "steelblue")
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("stroke", "")
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("stroke-width", "")

      d3.select(textEl)
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("fill", "")
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("font-weight", "plain")
        .transition() // <------- TRANSITION STARTS HERE --------
        .delay(function (d, i) { return 100 * i; })
        .duration(1000)
        .attr("font-size", 10)

    },
    getExistRefId(refContent_) {
      return refContnt_RefId_Map.get(refContent_)
    },
    getBindVisFragmentId(refId_) {
      return refId_bindVisFragmentId_Map.get(refId_)
    },
    appendNewRef(refContent_, idSuf) {
      let newCount = 0
      if (cell_RefCount_Map.get(idSuf)) {
        newCount = cell_RefCount_Map.get(idSuf) + 1
      }
      else {
        newCount = 1
      }
      cell_RefCount_Map.set(idSuf, newCount)
      let newId = "cell-" + idSuf + "-ref-" + newCount

      refContnt_RefId_Map.set(refContent_, newId)
      return newId
    },
    removeDeletedRef(newRefContnt_RefId_Map) {
      let keys = [...refContnt_RefId_Map.keys()];
      for (let key in keys) {
        if (!newRefContnt_RefId_Map.get(key)) {
          let deletedRefId = refContnt_RefId_Map.get(key)
          if (refId_bindVisFragmentId_Map.get(deletedRefId)) {
            refId_bindVisFragmentId_Map.delete(deletedRefId)
          }
          refContnt_RefId_Map.delete(key)
        }
      }
    }
  }
}
</script>

<style>
.reference {
  font-weight: bold;
  padding-left: 0.2em;
  padding-right: 0.2em;
}

.reference {
  background-image: url("../pics/ref.png");
  background-size: 120%;
  background-repeat: no-repeat;
  background-position: center;
}
</style>