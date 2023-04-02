<template>
  <div class="text-cell" :id="id" @dblclick="onDbClickTextCell($event)">
    <div :id="mdContainerId">
    </div>
  </div>
</template>

<script>
import MarkdownCell from "@/components/TextComponents/MarkdownCell.vue";
import { render, createApp } from 'vue'
import BodyOfDoc from "@/components/BodyOfDoc.vue";
import AddCells from '@/components/AddCells.vue';
import ref from "@/components/ref.vue"
import claim from "@/components/claim.vue"
import { ElColumn, ElRow, ElPopconfirm, ElButton } from 'element-plus'

import mybutton from "@/components/mybutton.vue";
import marked from "marked";
var vm = null;

var TextCell = {
  props: {
    index: null,
    sbIndex: null,
    layout: null,
    textData: null,
    startNewLine: false,
    // data...
  },
  data() {
    return {
      id: "text-cell-" + this.sbIndex + "-" + this.index,
      sbId: "section-block-" + this.sbIndex,
      mdContainerId: "md-cell-container-" + this.sbIndex + "-" + this.index,
      markdownCellPops: {
        index: this.index,
        sbIndex: this.sbIndex,
        textData: this.textData, // the original md text, not HTML
        layout: this.layout,
        tcContentContainerEl: null,
      },
      layoutType: this.layout,
      startNewLineForDBL: this.startNewLine,
    };
  },
  components: {
    'markdown-cell': MarkdownCell,
    AddCells,
    ref,
    claim,
    // compile,
  },
  methods: {
    onDbClickTextCell(event) {
      let targetId = event.currentTarget.id;
      let idStrs = targetId.split('-');
      let idSuf = idStrs[idStrs.length - 2] + '-' + idStrs[idStrs.length - 1];

      let thisMDCell = document.getElementById("markdown-cell" + "-" + idSuf)
      let thisTextNode = document.getElementById("text-content-container" + "-" + idSuf)

      thisMDCell.style.display = "flex"
      thisMDCell.style.flexDirection = "column"
      thisTextNode.style.display = "none"

      if (BodyOfDoc.activateTextCellIdSuf) {
        let idSuf = BodyOfDoc.activateTextCellIdSuf
        let thisMDCell = document.getElementById("markdown-cell" + "-" + idSuf)
        let thisMDViewer = document.getElementById("markdown-viewer" + "-" + idSuf)
        let thisTextNode = document.getElementById("text-content-container" + "-" + idSuf)

        thisTextNode.innerHTML = thisMDViewer.innerHTML

        thisMDCell.style.display = "none"
        thisTextNode.style.display = "block"

        BodyOfDoc.activateTextCellIdSuf = null
      }

      BodyOfDoc.activateTextCellIdSuf = idSuf;
    },
    endEdit() {

    }
  },
  mounted() {
    vm = this;

    let thisCell = document.getElementById(vm.id)
    var containerOfThisCell = document.querySelector("#" + vm.id).closest(".el-row");
    var nearestSecBlockOfThisCell = document.querySelector("#" + vm.id).closest(".section-block");
    let idStrs = vm.id.split('-');
    let idSuf = idStrs[idStrs.length - 2] + '-' + idStrs[idStrs.length - 1];

    var wrap = function (toWrap, wrapper) {
      toWrap.parentNode.appendChild(wrapper);
      return wrapper.appendChild(toWrap);
    };

    // Parse the Text Content for this Text Cell to the textNode
    // Add the textNode as the child of text-cell.
    let textNode = document.createElement('div')
    textNode.className = "text-content-container"
    textNode.id = "text-content-container" + "-" + idSuf

    // Handle the <ref> and <claim> tags in the textData.
    // Since Vue wont allow comiling directly, the process would be tricky...
    let re = /([\s\S]*?)((<ref>([\s\S]+?)<\/ref>)|(<claim>([\s\S]+?)<\/claim>))/g;
    let textStr = marked.parse(vm.textData)
    let newRefContnt_RefId_Map = new Map()
    let refsMatchArray = [...textStr.matchAll(re)];
    // array[x]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> (x、y=.) 的信息
    // array[x][0]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> or null(???)
    // array[x][1]: xxx
    // array[x][2]: <ref>yyy</ref> or <claim>zzz</claim>
    // array[x][3]: <ref>yyy</ref> or null
    // array[x][4]: yyy or null
    // array[x][5]: <claim>zzz</claim> or null
    // array[x][6]: zzz or null
    let newTextStr = ""
    for (let i = 0; i < refsMatchArray.length; i++) {
      if (refsMatchArray[i][1] != null) {
        let xStr = refsMatchArray[i][1]
        if (refsMatchArray[i][2] != null && (refsMatchArray[i][4] != null || refsMatchArray[i][6] != null)) {
          let yStr = refsMatchArray[i][4] ? refsMatchArray[i][4] : refsMatchArray[i][6]
          let vnode = <span>{yStr}</span>
          if (refsMatchArray[i][3])
            vnode = <ref>{yStr}</ref>
          else if (refsMatchArray[i][5])
            vnode = <claim>{yStr}</claim>
          let el = document.createElement("div")
          render(vnode, el)
          vnode = el.firstChild
          newTextStr = newTextStr + xStr + vnode.outerHTML
        }
      }
      if (i == refsMatchArray.length - 1) {
        let lastDataFactTailIndex = textStr.length
        if (refsMatchArray[i][3]) {
          lastDataFactTailIndex = refsMatchArray[i].index + refsMatchArray[i][1].length + refsMatchArray[i][3].length
        }
        else if (refsMatchArray[i][5]) {
          lastDataFactTailIndex = refsMatchArray[i].index + refsMatchArray[i][1].length + refsMatchArray[i][5].length
        }
        if (lastDataFactTailIndex < textStr.length)
          newTextStr = newTextStr + textStr.substring(lastDataFactTailIndex)
      }
    }
    if (newTextStr == null || newTextStr.length <= 0)
      newTextStr = vm.textData

    textNode.innerHTML = "<p>" + newTextStr + "</p>"
    thisCell.appendChild(textNode)

    vm.markdownCellPops.tcContentContainerEl = textNode
    let mdVnode = createApp(MarkdownCell, vm.markdownCellPops)
    mdVnode.mount("#" + vm.mdContainerId)
    // document.getElementById(vm.mdContainerId).style.display="none"

    // Handle the layout of the text cell according to the js file.
    // (Double Column or Single Column)
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
        elRowOfThisCell.parentNode.parentNode.appendChild(addCellsNode)
      }
      else { // This Cell: the 1st one.
        let wrapper = <el-column style="width: 50%;"></el-column>
        let el = document.createElement("div")
        render(wrapper, el)
        wrapper = el.childNodes[0]
        thisCell = wrap(thisCell, wrapper)

        // This is POINTLESS but the rendering below won't work if I remove it.
        wrapper = <el-row ></el-row >
        el = document.createElement("div")
        render(wrapper, el)
        wrapper = el.childNodes[0]

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

    document.addEventListener('click', function (event) {
      let idSuf = BodyOfDoc.activateTextCellIdSuf
      if (idSuf == null)
        return;

      let activateTextCellId = "text-cell" + "-" + idSuf
      let activateTextCell = document.getElementById(activateTextCellId)
      if (activateTextCell.contains(event.target))
        return;

      let thisMDCell = document.getElementById("markdown-cell" + "-" + idSuf)
      let thisMDViewer = document.getElementById("markdown-viewer" + "-" + idSuf)
      let thisTextNode = document.getElementById("text-content-container" + "-" + idSuf)

      thisTextNode.innerHTML = thisMDViewer.innerHTML

      thisMDCell.style.display = "none"
      thisTextNode.style.display = "block"

      // console.log(thisTextNode.children)
      for (let i = 0; i < thisTextNode.children.length; i++) {
        let child = thisTextNode.children[i]
        if (child.children) {
          for (let j = 0; j < child.children.length; j++) {
            let child_j = child.children[j]
            if (child_j.className == "reference") {
              child_j.addEventListener('mouseover', ref.methods.setHover)
              child_j.addEventListener('mouseout', ref.methods.setOut)
              child_j.addEventListener('click', ref.methods.setClick)
            }
            else if (child_j.className == "claim") {
              child_j.addEventListener('mouseover', claim.methods.setHover)
              child_j.addEventListener('mouseout', claim.methods.setOut)
              child_j.addEventListener('click', claim.methods.setClick)
            }
          }
        }
      }

      BodyOfDoc.activateTextCellIdSuf = null
    });

    // let el = document.createElement("div")
    // let vnode = <mybutton/>
    // render(vnode, el)
    // document.getElementById(vm.id).appendChild(el)
  },
};
export default TextCell;
</script>

<style scoped>
/* .text-cell-container {
  width: 100%
} */

.text-cell {
  min-height: 38px;
  /* background: pink; */
  display: flex;
  flex-direction: column;
  width: 100%;
  /* margin-bottom: 1%; */
  /* margin-top: 1%; */
  /* height: 219px; */
}

.text-content-container {
  width: 100%;
  height: 100%;
  display: block;
}

p {
  margin-top: 0;
  margin-bottom: 0;
}

/* .text-cell-container-row {
  width: 100%;
} */
</style>
