<template>
  <span class="claim" :ref="claim" :id="this.id">
    <slot>
      {{ text }}
    </slot>
  </span>
</template>

<script>
import $ from 'jquery';
let claim_id = 1;
let vm = null;
import { render } from 'vue'
import * as d3 from "d3";
import mybutton from "@/components/mybutton.vue"
import { ElPopconfirm, ElButton } from 'element-plus'
import Spreadsheet from '@/components/SpreadsheetComponents/Spreadsheet.vue';

const cell_ClaimCount_Map = new Map();
const claimContnt_ClaimId_Map = new Map();
const claimId_bindVisFragmentsId_Map = new Map();

const myMap = new Map();

export default {
  name: "claim",
  props: {
    textData: null,
  },
  data() {
    return {
      id: "claim" + claim_id,
      text: this.textData,
      bindVis: null,
      bindTable: null,
    };
  },
  created() {
    this.id = "claim" + claim_id; // data.id更新
    claim_id++;

    const _default = this.$slots.default();
    if (_default && _default.length > 0)
      this.text = _default[0].children; // data.text更新
  },
  mounted() {
    let claimEl = document.getElementById(this.id)
    if (!claimEl) // mounted from Markdown Components, display=none
    {
      this.id = null
    }
    else {
      let claimElParent = claimEl.parentElement
      let claimElParentParent = claimElParent.parentElement
      let strs = claimElParentParent.id.split("-")
      let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];

      if (!cell_ClaimCount_Map.get(suf)) {
        cell_ClaimCount_Map.set(suf, 1)
      }
      else {
        let claimCountOfThisCell = cell_ClaimCount_Map.get(suf)
        cell_ClaimCount_Map.set(suf, claimCountOfThisCell + 1)
      }

      let newId = "cell-" + suf + "-claim-" + cell_ClaimCount_Map.get(suf)
      this.id = newId
      claimEl.setAttribute("id", newId)

      let textContent = claimElParent.innerText
      let claimContent = this.text
      let claimIndexInCell = suf// + "-" + textContent.indexOf(claimContent)
      let claimId = newId

      claimContnt_ClaimId_Map.set(claimContent, claimId)
    }

    if (claimEl) {
      claimEl.addEventListener('mouseover', this.setHover)
      claimEl.addEventListener('mouseout', this.setOut)
      claimEl.addEventListener('click', this.setClick)
    }

  },
  methods: {
    appendToMyMap(id, visFragmentId) {
      if (!myMap.has(id)) {
        let arr = new Array()
        arr.push(visFragmentId)
        myMap.set(id, arr)
      }
      else {
        let arr = myMap.get(id)
        arr.push(visFragmentId)
        myMap.set(id, arr)
      }
      console.log(myMap)
    },
    setHover(event) {
      console.log("hover")
      let target = event.currentTarget;
      let targetId = target.getAttribute("id")
      let hoveredTarget = document.getElementById(targetId)
      target = hoveredTarget

      console.log(target.id)
      console.log(myMap.get(target.id))
      if (myMap.has(target.id)) {
        let visArr = myMap.get(target.id)
        for (let boundVisFragmentId in visArr) {
          // console.log(target.getAttribute("bind-vis"))
          //let boundVisFragmentId = target.getAttribute("bind-vis")
          boundVisFragmentId = visArr[boundVisFragmentId]
          let boundVisFragment = document.getElementById(boundVisFragmentId)
          // let boundVisFragmentTextId = boundVisFragmentId.replace("rect", "text")
          console.log(boundVisFragment)
          let boundVisFragmentTextId = ""
          if (boundVisFragmentId.includes("rect")) {
            boundVisFragmentTextId = boundVisFragmentId.replace("rect", "text")
          }
          else {
            boundVisFragmentTextId = boundVisFragmentId.replace("arc", "text")
          }
          let boundVisFragmentText = document.getElementById(boundVisFragmentTextId)

          d3.select(boundVisFragment)
            .attr("fill", "#fbb")
            .attr("stroke", "#d39d9c")
            .attr("stroke-width", "5")

          d3.select(boundVisFragmentText)
            .attr("fill", "#d39d9c")
            .attr("font-weight", 700)
            .attr("font-size", 16)
        }
      }
      if (target.hasAttribute("bind-table")) {
        let tableId = target.getAttribute("table-id")
        let range = target.getAttribute("bind-table")
        Spreadsheet.methods.handleHover("claim", tableId, range)
      }
    },
    setOut(event) {
      let target = event.currentTarget;
      let targetId = target.getAttribute("id")
      let hoveredTarget = document.getElementById(targetId)
      target = hoveredTarget

      console.log(target.id)
      console.log(myMap.get(target.id))
      if (myMap.has(target.id)) {
        let visArr = myMap.get(target.id)
        for (let boundVisFragmentId in visArr) {
          // console.log(target.getAttribute("bind-vis"))
          //let boundVisFragmentId = target.getAttribute("bind-vis")
          boundVisFragmentId = visArr[boundVisFragmentId]
          let boundVisFragment = document.getElementById(boundVisFragmentId)
          let boundVisFragmentTextId = ""
          if (boundVisFragmentId.includes("rect")) {
            boundVisFragmentTextId = boundVisFragmentId.replace("rect", "text")
          }
          else {
            boundVisFragmentTextId = boundVisFragmentId.replace("arc", "text")
          }
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
      }
      if (target.hasAttribute("bind-table")) {
        let tableId = target.getAttribute("table-id")
        let range = target.getAttribute("bind-table")
        Spreadsheet.methods.handleLeave("claim", tableId, range)
      }
    },
    setClick(event) {
      console.log("CLICK")
      let target = event.currentTarget;
      let targetRect = target.getBoundingClientRect();

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
    removeBtn(claimId) {
      let mybtnId = "btn-" + claimId
      let mybtnEl = document.getElementById(mybtnId)
      mybtnEl.remove()
    },
    bindToVisFragment(claimId, visFragmentId) {
      claimId_bindVisFragmentsId_Map.set(claimId, visFragmentId)

      let claimEl = document.getElementById(claimId)
      console.log(claimEl)
      let rectEl = document.getElementById(visFragmentId)
      let rectTextId = ""
      if (visFragmentId.includes("rect")) {
        rectTextId = visFragmentId.replace("rect", "text")
      }
      else {
        rectTextId = visFragmentId.replace("arc", "text")
      }
      let textEl = document.getElementById(rectTextId)
      // let mybtnId = "btn-" + claimId
      // let mybtnEl = document.getElementById(mybtnId)
      // mybtnEl.remove()

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
    getExistClaimId(claimContent_) {
      return claimContnt_ClaimId_Map.get(claimContent_)
    },
    getBindVisFragmentsId(claimId_) {
      return claimId_bindVisFragmentsId_Map.get(claimId_)
    },
    appendNewClaim(claimContent_, idSuf) {
      let newCount = 0
      if (cell_ClaimCount_Map.get(idSuf)) {
        newCount = cell_ClaimCount_Map.get(idSuf) + 1
      }
      else {
        newCount = 1
      }
      cell_ClaimCount_Map.set(idSuf, newCount)
      let newId = "cell-" + idSuf + "-claim-" + newCount

      claimContnt_ClaimId_Map.set(claimContent_, newId)
      return newId
    },
    removeDeletedClaim(newClaimContnt_ClaimId_Map) {
      let keys = [...claimContnt_ClaimId_Map.keys()];
      for (let key in keys) {
        if (!newClaimContnt_ClaimId_Map.get(key)) {
          let deletedClaimId = claimContnt_ClaimId_Map.get(key)
          if (claimId_bindVisFragmentsId_Map.get(deletedClaimId)) {
            claimId_bindVisFragmentsId_Map.delete(deletedClaimId)
          }
          claimContnt_ClaimId_Map.delete(key)
        }
      }
    }
  }
}
</script>

<style>
.claim {
  font-weight: bold;
  padding-left: 0.2em;
  padding-right: 0.2em;
}

.claim {
  background-image: url("../pics/claim.png");
  background-size: 120%;
  background-repeat: no-repeat;
  background-position: center;
}
</style>