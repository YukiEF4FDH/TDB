<template>
  <div class="markdown-editor" :id="id" :index-as-editor="mdEditorCount">
    <div :id="monacoEditorContainerId" class="monaco-editor-container"></div>
  </div>
</template>

<script>
import marked from "marked";
import * as monaco from "monaco-editor/esm/vs/editor/editor.api.js";
import "monaco-editor/esm/vs/basic-languages/markdown/markdown.contribution";
import ref from "@/components/ref.vue"
import claim from "@/components/claim.vue"
import { render } from 'vue'
var vm = null;
var mdEditorCount_ = 0;

export default {
  name: "MarkdownEditor",
  props: {
    index: null,
    sbIndex: null,
    textM: null,
    textH: null,
    layout: null,
  },
  data() {
    return {
      id: "markdown-editor" + "-" + this.sbIndex + "-" + this.index,
      monacoEditorContainerId: "monaco-editor-container" + "-" + this.sbIndex + "-" + this.index,
      textMD: this.textM,
      textHTML: this.textH,
      editingTextMD: null,
      layoutType: this.layout,
      mdEditorCount: null,
    };
  },
  beforeMount() { },
  mounted() {
    vm = this;
    vm.mdEditorCount = mdEditorCount_;
    mdEditorCount_++

    let markdownEditor = document.getElementById(vm.id);
    let monacoEditorContainer = document.getElementById(vm.monacoEditorContainerId);

    if (vm.layout == 'double-column')
      monacoEditorContainer.style.width = "100%"

    let monacoInstance = monaco.editor.create(monacoEditorContainer, {
      value: vm.textMD,
      language: "markdown",
      minimap: {
        enabled: false
      },
      lineNumbers: 'off',
      glyphMargin: false,
      folding: false,
      // Undocumented see https://github.com/Microsoft/vscode/issues/30795#issuecomment-410998882
      lineDecorationsWidth: 0,
      lineNumbersMinChars: 0,
    });
    // mdEditorCount++;

    //console.log(monaco.editor.getEditors().find())

    let idStrs = monacoEditorContainer.id.split('-');
    let idSuf = idStrs[idStrs.length - 2] + '-' + idStrs[idStrs.length - 1];

    monacoInstance.onDidChangeModelContent((event) => {
      let newValue = monacoInstance.getValue();
      vm.textMD = newValue;
      let newHTML = marked.parse(newValue);
      vm.textHTML = newHTML;

      let mdViewerId = "markdown-viewer" + "-" + idSuf;
      let mdViewer = document.getElementById(mdViewerId)

      let tmpDiv = document.createElement('div');
      tmpDiv.innerHTML = newHTML.trim();
      let textContent = tmpDiv.firstChild.innerText;

      // Handle the <ref> and <claim> tags in the textHTML.
      // Since Vue wont allow comiling directly, the process would be tricky...
      let re = /([\s\S]*?)((<ref>([\s\S]+?)<\/ref>)|(<claim>([\s\S]+?)<\/claim>))/g;
      let textStr = newHTML
      let newRefContnt_RefId_Map = new Map()
      let newClaimContnt_ClaimId_Map = new Map()
      let dataFactsMatchedArr = [...textStr.matchAll(re)];
      // array[x]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> (x、y=.) 的信息
      // array[x][0]: xxx<ref>yyy</ref> or xxx<claim>zzz</claim> or null(???)
      // array[x][1]: xxx
      // array[x][2]: <ref>yyy</ref> or <claim>zzz</claim>
      // array[x][3]: <ref>yyy</ref> or null
      // array[x][4]: yyy or null
      // array[x][5]: <claim>zzz</claim> or null
      // array[x][6]: zzz or null
      let newTextStr = ""
      for (let i = 0; i < dataFactsMatchedArr.length; i++) {
        if (dataFactsMatchedArr[i][1] != null) {
          let xStr = dataFactsMatchedArr[i][1]
          if (dataFactsMatchedArr[i][2] != null && (dataFactsMatchedArr[i][4] != null || dataFactsMatchedArr[i][6] != null)) {
            let yStr = dataFactsMatchedArr[i][4] ? dataFactsMatchedArr[i][4] : dataFactsMatchedArr[i][6]
            console.log(textContent.indexOf(yStr))
            let vnode = <span>{yStr}</span>
            if (dataFactsMatchedArr[i][3])
              vnode = <ref>{yStr}</ref>
            else if (dataFactsMatchedArr[i][5])
              vnode = <claim>{yStr}</claim>
            let el = document.createElement("div")
            render(vnode, el)
            vnode = el.firstChild

            if (dataFactsMatchedArr[i][3]) {
              let refContent = yStr
              let newId = 0
              if (ref.methods.getExistRefId(refContent)) {
                newId = ref.methods.getExistRefId(refContent)
                if (ref.methods.getBindVisFragmentId(newId)) {
                  vnode.setAttribute("bind-vis", ref.methods.getBindVisFragmentId(newId))
                }
              }
              else
                newId = ref.methods.appendNewRef(refContent, idSuf)
              vnode.setAttribute("id", newId)
              newRefContnt_RefId_Map.set(refContent, newId)
            }
            else if (dataFactsMatchedArr[i][5]) {
              let claimContent = yStr
              let newId = 0
              if (claim.methods.getExistClaimId(claimContent)) {
                newId = claim.methods.getExistClaimId(claimContent)
                if (claim.methods.getBindVisFragmentsId(newId)) {
                  vnode.setAttribute("bind-vis", claim.methods.getBindVisFragmentsId(newId))
                }
              }
              else
                newId = claim.methods.appendNewClaim(claimContent, idSuf)
              vnode.setAttribute("id", newId)
              newClaimContnt_ClaimId_Map.set(claimContent, newId)
            }

            newTextStr = newTextStr + xStr + vnode.outerHTML
          }
        }
        if (i == dataFactsMatchedArr.length - 1) {
          let lastDataFactTailIndex = textStr.length
          if (dataFactsMatchedArr[i][3]) {
            lastDataFactTailIndex = dataFactsMatchedArr[i].index + dataFactsMatchedArr[i][1].length + dataFactsMatchedArr[i][3].length
          }
          else if (dataFactsMatchedArr[i][5]) {
            lastDataFactTailIndex = dataFactsMatchedArr[i].index + dataFactsMatchedArr[i][1].length + dataFactsMatchedArr[i][5].length
          }
          if (lastDataFactTailIndex < textStr.length)
            newTextStr = newTextStr + textStr.substring(lastDataFactTailIndex)
        }
      }
      if (newTextStr == null || newTextStr.length <= 0)
        newTextStr = newHTML
      newHTML = newTextStr

      ref.methods.removeDeletedRef(newRefContnt_RefId_Map)
      claim.methods.removeDeletedClaim(newClaimContnt_ClaimId_Map)

      mdViewer.innerHTML = newHTML
    });

    let wid = document.getElementById(vm.id).parentElement.parentElement.offsetWidth
    let hei = document.getElementById(vm.id).parentElement.parentElement.offsetHeight
    document.getElementById(vm.id).parentElement.style.height = document.getElementById(vm.id).parentElement.parentElement.offsetHeight
    document.getElementById(vm.id).style.height = document.getElementById(vm.id).parentElement.offsetHeight

    if (vm.layoutType == 'double-column') {
      monacoInstance.layout({ width: wid / 2, height: hei });
      //monacoInstance.layout({ width: (wid / 2) / 2, height: hei });
    }
    else {
      monacoInstance.layout({ width: wid / 2, height: hei });
    }
  },
  methods: {
    onClickTitle(ele) {
      let editorId = ele.id.replace("cell", "editor")
      let editorEle = document.getElementById(editorId)
      let monacoIndex = editorEle.getAttribute("index-as-editor")
      let monacoInstance = monaco.editor.getEditors()[monacoIndex]
      // console.log(monacoInstance.getValue())

      var line = monacoInstance.getPosition();
      var range = new monaco.Range(line.lineNumber, 1, line.lineNumber, 1);
      var id = { major: 1, minor: 1 };
      var text = "### ";
      var op = { identifier: id, range: range, text: text, forceMoveMarkers: true };
      monacoInstance.executeEdits("my-source", [op]);
    },
    onClickBold(ele) {
      let editorId = ele.id.replace("cell", "editor")
      let editorEle = document.getElementById(editorId)
      let monacoIndex = editorEle.getAttribute("index-as-editor")
      let monacoInstance = monaco.editor.getEditors()[monacoIndex]
      // console.log(monacoInstance.getValue())

      var selection = monacoInstance.getSelection();
      let selectedText = monacoInstance.getModel().getValueInRange(monacoInstance.getSelection())
      console.log(selectedText)
      // let selectedText = monacoInstance.getValueInRange(selection)
      var id = { major: 1, minor: 1 };
      var text = " **" + selectedText + "** ";
      var op = { identifier: id, range: selection, text: text, forceMoveMarkers: true };
      monacoInstance.executeEdits("my-source", [op]);
    },
    onClickItalic(ele) {
      let editorId = ele.id.replace("cell", "editor")
      let editorEle = document.getElementById(editorId)
      let monacoIndex = editorEle.getAttribute("index-as-editor")
      let monacoInstance = monaco.editor.getEditors()[monacoIndex]
      // console.log(monacoInstance.getValue())

      var selection = monacoInstance.getSelection();
      let selectedText = monacoInstance.getModel().getValueInRange(monacoInstance.getSelection())
      console.log(selectedText)
      // let selectedText = monacoInstance.getValueInRange(selection)
      var id = { major: 1, minor: 1 };
      var text = " *" + selectedText + "* ";
      var op = { identifier: id, range: selection, text: text, forceMoveMarkers: true };
      monacoInstance.executeEdits("my-source", [op]);
    },
    onClickRef(ele) {
      let editorId = ele.id.replace("cell", "editor")
      let editorEle = document.getElementById(editorId)
      let monacoIndex = editorEle.getAttribute("index-as-editor")
      let monacoInstance = monaco.editor.getEditors()[monacoIndex]
      // console.log(monacoInstance.getValue())

      var selection = monacoInstance.getSelection();
      let selectedText = monacoInstance.getModel().getValueInRange(monacoInstance.getSelection())
      console.log(selectedText)
      // let selectedText = monacoInstance.getValueInRange(selection)
      var id = { major: 1, minor: 1 };
      var text = "<ref>" + selectedText + "</ref>";
      var op = { identifier: id, range: selection, text: text, forceMoveMarkers: true };
      monacoInstance.executeEdits("my-source", [op]);
    },
    onClickClaim(ele) {
      let editorId = ele.id.replace("cell", "editor")
      let editorEle = document.getElementById(editorId)
      let monacoIndex = editorEle.getAttribute("index-as-editor")
      let monacoInstance = monaco.editor.getEditors()[monacoIndex]
      // console.log(monacoInstance.getValue())

      var selection = monacoInstance.getSelection();
      let selectedText = monacoInstance.getModel().getValueInRange(monacoInstance.getSelection())
      console.log(selectedText)
      // let selectedText = monacoInstance.getValueInRange(selection)
      var id = { major: 1, minor: 1 };
      var text = "<claim>" + selectedText + "</claim>";
      var op = { identifier: id, range: selection, text: text, forceMoveMarkers: true };
      monacoInstance.executeEdits("my-source", [op]);
    }
  },
};
</script>

<style scoped>
.markdown-editor {
  /* box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
    0 2px 4px -1px rgb(0 0 0 / 40%);
  min-height: 200px;
  display: flex;
  flex-direction: row;
  width: 50%; */
  /* width: 50%;
  min-height: 200px;
  display: flex;
  flex-direction: row; */
  width: 50%;
  height: 100%;
  box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
    0 2px 4px -1px rgb(0 0 0 / 40%);
  max-height: 219px;

}

.monaco-editor-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
}
</style>