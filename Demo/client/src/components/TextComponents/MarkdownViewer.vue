<template>
  <div ref="viewer" class="markdown-viewer" :id="id">
  <!-- <div ref="viewer" class="markdown-viewer" :id="id" v-html='textHTML'> -->
  </div>
</template>

<script>
import marked from "marked";
import { render, createApp } from 'vue'
import ref from "@/components/ref.vue"
import claim from "@/components/claim.vue"
import $ from 'jquery'
var vm = null;
var markdownViewer = null;

export default {
  name: "MarkdownViewer",
  props: {
    index: null,
    sbIndex: null,
    textM: null,
    textH: null,
    textCellContainerEl: null
  },
  data() {
    return {
      id: "markdown-viewer" + "-" + this.sbIndex + "-" + this.index,
      textMD: this.textM,
      textHTML: this.textH,
      tcContainerEl: this.textCellContainerEl
    };
  },
  beforeMount() { },
  mounted() {
    vm = this;
    markdownViewer = document.querySelector("#" + vm.id);
    let idStrs = vm.id.split('-');
    let idSuf = idStrs[idStrs.length - 2] + '-' + idStrs[idStrs.length - 1];

    let copyOfTCContentContainerEle = vm.tcContainerEl.cloneNode(true)
    let copyOfTextCellContent = copyOfTCContentContainerEle.children[1].cloneNode(true)
    // console.log(copyOfTextCellContent)

    markdownViewer.appendChild(copyOfTextCellContent)

    // console.log(markdownViewer)
    if (markdownViewer) {
      const pp = markdownViewer.parentElement.parentElement
      // console.log( pp )
      // console.log( pp.nextSibling) 
      // const textCell = markdownViewer.parentElement.parentElement.parentElement
      // console.log(textCell)
      // console.log(textCell.nextSibling)
      // let childrenOfTC = textCell.children
      // console.log(childrenOfTC)
      // console.log(childrenOfTC.length)
      // console.log(childrenOfTC[0])
      // console.log(childrenOfTC[1])
      // for (let i=0; i<childrenOfTC.length; i++){
      //   let child_i = childrenOfTC[i]
      //   console.log(child_i.className)
      // }
    }

    // let textNode = document.createElement('div')
    // textNode.className = "mdviewer-container"
    // textNode.id = "mdviewer-container" + "-" + idSuf

    // // Handle the <ref> and <claim> tags in the textHTML.
    // // Since Vue wont allow comiling directly, the process would be tricky...
    // let re = /([\s\S]*?)((<ref>([\s\S]+?)<\/ref>)|(<claim>([\s\S]+?)<\/claim>))/g;
    // let textStr = vm.textHTML
    // console.log(textStr)
    // let dataFactsMatchedArr = [...textStr.matchAll(re)];
    // // array[x]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> (x、y=.) 的信息
    // // array[x][0]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> or null(???)
    // // array[x][1]: xxx
    // // array[x][2]: <ref>yyy</ref> or <claim>zzz</claim>
    // // array[x][3]: <ref>yyy</ref> or null
    // // array[x][4]: yyy or null
    // // array[x][5]: <claim>zzz</claim> or null
    // // array[x][6]: zzz or null
    // let newTextStr = ""
    // for (let i = 0; i < dataFactsMatchedArr.length; i++) {
    //   if (dataFactsMatchedArr[i][1] != null) {
    //     let xStr = dataFactsMatchedArr[i][1]
    //     if (dataFactsMatchedArr[i][2] != null && (dataFactsMatchedArr[i][4] != null || dataFactsMatchedArr[i][6] != null)) {
    //       let yStr = dataFactsMatchedArr[i][4] ? dataFactsMatchedArr[i][4] : dataFactsMatchedArr[i][6]
    //       let vnode = <span>{yStr}</span>
    //       if (dataFactsMatchedArr[i][3])
    //         vnode = <ref>{yStr}</ref>
    //       else if (dataFactsMatchedArr[i][5])
    //         vnode = <claim>{yStr}</claim>
    //       let el = document.createElement("div")
    //       render(vnode, el)
    //       vnode = el.firstChild
    //       newTextStr = newTextStr + xStr + vnode.outerHTML
    //     }
    //   }
    //   if (i == dataFactsMatchedArr.length - 1) {
    //     let lastDataFactTailIndex = textStr.length
    //     if (dataFactsMatchedArr[i][3]) {
    //       lastDataFactTailIndex = dataFactsMatchedArr[i].index + dataFactsMatchedArr[i][1].length + dataFactsMatchedArr[i][3].length
    //     }
    //     else if (dataFactsMatchedArr[i][5]) {
    //       lastDataFactTailIndex = dataFactsMatchedArr[i].index + dataFactsMatchedArr[i][1].length + dataFactsMatchedArr[i][5].length
    //     }
    //     if (lastDataFactTailIndex < textStr.length)
    //       newTextStr = newTextStr + textStr.substring(lastDataFactTailIndex)
    //   }
    // }
    // if (newTextStr == null || newTextStr.length <= 0)
    //   newTextStr = vm.textHTML

    // textNode.innerHTML = "<p>" + newTextStr + "</p>"
    // vm.textHTML = textNode.innerHTML
  },
  methods: {
    updateByEditing(mdViewerId, newTextMD) {
      let markdownViewer = document.querySelector("#" + mdViewerId);


    }
  },
};
</script>

<style scoped>
.markdown-viewer {
  /* width: calc(100% - 42px); */
  width: 50%;
  height: 100%;
  border-left: 1px dashed grey;
  flex: 1;
  line-height: 1.6;
  max-width: 1016px;
  /* min-height: 100%; */
  max-height: 219px;
  padding-left: 8px;
  padding-right: 4px;
  word-wrap: break-word;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
}
</style>