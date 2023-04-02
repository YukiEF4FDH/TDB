
<template>
  <div class="markdown-cell" :id="id" @dblclick="onDbClickMDCell($event)">
    <div class="markdown-cell-toolbar" style="display: block;" :id="toolbarId">
      <paper-icon-button icon="editor:editor:text-fields" @click="onClickTitle($event)"></paper-icon-button>
      <paper-icon-button icon="editor:format-bold" @click="onClickBold($event)"></paper-icon-button>
      <paper-icon-button icon="editor:format-italic" @click="onClickItalic($event)"></paper-icon-button>
      <paper-icon-button icon="editor:insert-link"></paper-icon-button>
      <!-- <paper-icon-button icon="editor:insert-photo"></paper-icon-button> -->
      <paper-icon-button icon="editor:format-list-numbered"></paper-icon-button>
      <paper-icon-button icon="editor:format-list-bulleted"></paper-icon-button>
      <button @click="onClickRef($event)">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="40" height="18"
          overflow="hidden" viewBox="10 8 30 19" data-v-55b89ea1="" style="margin-bottom: -11%">
          <g transform="translate(-424 -420)" data-v-55b89ea1="">
            <path
              d="M437.66 430.398C437.419 430.398 437.299 430.531 437.299 430.797L437.299 434.489 438.31 434.489C438.774 434.489 439.163 434.384 439.479 434.174 440.035 433.815 440.314 433.221 440.314 432.392 440.314 431.576 440.045 431.004 439.507 430.676 439.197 430.49 438.817 430.398 438.366 430.398ZM456.308 428.422 460.91 428.422C461.145 428.422 461.342 428.499 461.503 428.654 461.714 428.864 461.819 429.145 461.819 429.498 461.819 429.962 461.652 430.28 461.318 430.453 461.2 430.515 461.064 430.546 460.91 430.546L457.087 430.546C456.834 430.546 456.707 430.667 456.707 430.908L456.707 434.331 460.297 434.331C460.501 434.331 460.678 434.399 460.826 434.535 461.042 434.727 461.151 434.996 461.151 435.342 461.151 435.744 461.008 436.038 460.724 436.224 460.6 436.304 460.458 436.344 460.297 436.344L456.707 436.344 456.707 441.595C456.707 441.812 456.633 442.001 456.484 442.161 456.274 442.39 455.977 442.505 455.594 442.505 455.148 442.505 454.824 442.35 454.619 442.041 454.539 441.917 454.499 441.769 454.499 441.595L454.499 430.24C454.499 429.028 455.102 428.422 456.308 428.422ZM446.197 428.422 450.743 428.422C450.99 428.422 451.194 428.511 451.355 428.691 451.54 428.901 451.633 429.161 451.633 429.47 451.633 429.866 451.485 430.166 451.188 430.37 451.064 430.45 450.916 430.49 450.743 430.49L446.902 430.49C446.673 430.49 446.558 430.611 446.558 430.852L446.558 434.183 450.112 434.183C450.322 434.183 450.504 434.248 450.659 434.378 450.875 434.576 450.984 434.841 450.984 435.175 450.984 435.559 450.851 435.843 450.585 436.029 450.449 436.116 450.291 436.159 450.112 436.159L446.558 436.159 446.558 439.823C446.558 440.052 446.673 440.167 446.902 440.167L450.984 440.167C451.213 440.167 451.404 440.238 451.559 440.38 451.782 440.584 451.893 440.866 451.893 441.224 451.893 441.676 451.735 441.994 451.42 442.18 451.29 442.254 451.145 442.291 450.984 442.291L446.197 442.291C444.966 442.291 444.35 441.679 444.35 440.454L444.35 430.258C444.35 429.034 444.966 428.422 446.197 428.422ZM437.03 428.422 438.746 428.422C439.785 428.422 440.645 428.722 441.325 429.321 442.172 430.064 442.596 431.081 442.596 432.374 442.596 434.248 441.78 435.469 440.147 436.038L442.884 440.965C442.989 441.15 443.041 441.339 443.041 441.53 443.041 441.932 442.85 442.214 442.466 442.375 442.256 442.461 442.03 442.505 441.789 442.505 441.3 442.505 440.932 442.239 440.685 441.707L438.189 436.437 437.299 436.437 437.299 441.614C437.299 441.837 437.228 442.022 437.085 442.171 436.881 442.393 436.597 442.505 436.232 442.505 435.786 442.505 435.471 442.35 435.285 442.041 435.211 441.917 435.174 441.775 435.174 441.614L435.174 430.156C435.174 429 435.793 428.422 437.03 428.422Z"
              stroke="#000000" stroke-linecap="round" stroke-linejoin="bevel" stroke-miterlimit="10" fill="#A9D18E"
              fill-rule="evenodd" data-v-55b89ea1=""></path><text fill="#000000" fill-opacity="0"
              font-family="Arial,Arial_MSFontService,sans-serif" font-size="14.083" x="435.174" y="440.744"
              data-v-55b89ea1="">REF</text>
          </g>
        </svg>
      </button>
      <button @click="onClickClaim($event)">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="40" height="18"
          overflow="hidden" viewBox="5 0 30 24" data-v-55b89ea1="" style="margin-bottom: -11%">
          <g transform="translate(-434 -456)" data-v-55b89ea1="">
            <path
              d="M460.524 456.572C461.602 456.572 462.211 457.076 462.352 458.084L463.911 469.052 465.493 458.084C465.563 457.623 465.747 457.263 466.043 457.006 466.372 456.716 466.786 456.572 467.286 456.572 467.887 456.572 468.344 456.779 468.657 457.193 468.868 457.482 468.973 457.834 468.973 458.248L468.973 473.611C468.973 473.861 468.887 474.076 468.715 474.256 468.489 474.498 468.176 474.619 467.778 474.619 467.348 474.619 467.016 474.482 466.782 474.209 466.641 474.045 466.571 473.845 466.571 473.611L466.84 462.326 465.188 472.99C465.149 473.209 465.063 473.408 464.93 473.588 464.672 473.923 464.333 474.091 463.911 474.091 463.411 474.091 463.043 473.869 462.809 473.423 462.739 473.298 462.688 473.154 462.657 472.99L461.004 462.326 461.274 473.611C461.266 473.869 461.184 474.076 461.028 474.232 460.77 474.49 460.438 474.619 460.032 474.619 459.54 474.619 459.184 474.435 458.965 474.068 458.887 473.935 458.848 473.783 458.848 473.611L458.848 458.248C458.848 457.771 458.989 457.384 459.27 457.088 459.59 456.744 460.008 456.572 460.524 456.572ZM448.887 456.56C449.286 456.56 449.629 456.67 449.918 456.888 450.192 457.107 450.329 457.388 450.329 457.732L450.329 471.056C450.329 471.408 450.497 471.584 450.833 471.584L455.532 471.584C455.836 471.584 456.09 471.681 456.293 471.877 456.575 472.142 456.715 472.506 456.715 472.966 456.715 473.521 456.516 473.927 456.118 474.185 455.961 474.295 455.766 474.349 455.532 474.349L449.754 474.349C448.2 474.349 447.422 473.572 447.422 472.017L447.422 457.732C447.422 457.318 447.614 457.002 447.997 456.783 448.262 456.634 448.559 456.56 448.887 456.56ZM440.333 456.396C441.075 456.396 441.77 456.564 442.418 456.9 443.301 457.361 443.942 458.048 444.34 458.963 444.458 459.228 444.516 459.494 444.516 459.759 444.516 460.252 444.325 460.623 443.942 460.873 443.7 461.029 443.434 461.107 443.145 461.107 442.754 461.107 442.458 460.99 442.254 460.756 442.192 460.693 442.114 460.545 442.02 460.31 441.684 459.474 441.114 459.056 440.309 459.056 439.504 459.056 438.875 459.572 438.422 460.603 437.93 461.736 437.684 463.408 437.684 465.619 437.684 467.509 437.883 468.994 438.282 470.072 438.75 471.369 439.469 472.017 440.438 472.017 441.258 472.017 441.883 471.466 442.313 470.365 442.532 469.81 442.915 469.533 443.461 469.533 443.696 469.533 443.93 469.595 444.165 469.72 444.625 469.963 444.856 470.349 444.856 470.881 444.856 471.216 444.762 471.603 444.575 472.041 443.778 473.869 442.372 474.783 440.356 474.783 438.45 474.783 437.024 473.83 436.079 471.923 435.29 470.338 434.895 468.228 434.895 465.595 434.895 462.588 435.422 460.263 436.477 458.623 437.43 457.138 438.715 456.396 440.333 456.396Z"
              stroke="#000000" stroke-linecap="round" stroke-linejoin="bevel" stroke-miterlimit="10" fill="#FF8B8B"
              fill-rule="evenodd" data-v-55b89ea1=""></path><text fill="#000000" fill-opacity="0"
              font-family="Arial,Arial_MSFontService,sans-serif" font-size="18.3867" x="434.895" y="472.485"
              data-v-55b89ea1="">CLM</text>
          </g>
        </svg>
      </button>
    </div>
    <div class="markdown-cell-container" :id="containerId">
      <markdown-editor v-bind="markdownEditorProps"></markdown-editor>
      <markdown-viewer v-bind="markdownViewerProps"></markdown-viewer>
    </div>
  </div>
</template>

<script>
import marked from "marked";
import MarkdownEditor from "@/components/TextComponents/MarkdownEditor.vue";
import MarkdownViewer from "@/components/TextComponents/MarkdownViewer.vue";
import { createApp } from "vue/dist/vue.esm-bundler.js";
import '@polymer/paper-icon-button/paper-icon-button.js';
import '@polymer/iron-icons/iron-icons.js';
import '@polymer/iron-icons/editor-icons.js';

var vm = null;

var MarkdownCell = {
  name: "MarkdownCell",
  props: {
    index: null,
    sbIndex: null,
    textData: null,
    layout: null,
    tcContentContainerEl: null,
    // data...
  },
  components: {
    'markdown-editor': MarkdownEditor,
    'markdown-viewer': MarkdownViewer,
  },
  data() {
    return {
      id: "markdown-cell-" + this.sbIndex + "-" + this.index,
      toolbarId: "markdown-cell-toolbar-" + this.sbIndex + "-" + this.index,
      containerId: "markdown-cell-container-" + this.sbIndex + "-" + this.index,
      sbIndex: this.sbIndex,
      index: this.index,
      markdownEditorProps: {
        index: this.index,
        sbIndex: this.sbIndex,
        textM: this.textData,
        textH: marked.parse(this.textData),
        layout: this.layout,
      },
      markdownViewerProps: {
        index: this.index,
        sbIndex: this.sbIndex,
        textM: this.textData,
        textH: marked.parse(this.textData),
        textCellContainerEl: this.tcContentContainerEl,
      },
      textMD: this.textData,
      textHTML: marked.parse(this.textData),
      textCellContainer: this.tcContentContainerEl,
    };
  },
  methods: {
    onDbClickMDCell(event) {
      let targetId = event.currentTarget.id;
      let strs = targetId.split('-');
      let suf = strs[strs.length - 2] + '-' + strs[strs.length - 1];

      let editingMDViewer = document.getElementById('markdown-viewer-' + suf)
      let editingMDEditor = document.getElementById('markdown-editor-' + suf)
    },
    onClickTitle(event){
      MarkdownEditor.methods.onClickTitle(event.currentTarget.parentElement.parentElement)
    },
    onClickBold(event){
      MarkdownEditor.methods.onClickBold(event.currentTarget.parentElement.parentElement)
    },
    onClickItalic(event){
      MarkdownEditor.methods.onClickItalic(event.currentTarget.parentElement.parentElement)
    },
    onClickRef(event){
      MarkdownEditor.methods.onClickRef(event.currentTarget.parentElement.parentElement)
    },
    onClickClaim(event){
      MarkdownEditor.methods.onClickClaim(event.currentTarget.parentElement.parentElement)
    }
  },
  mounted() {
    vm = this;
    console.log("mount md cell: "+vm.id)

    var thisMDCell = document.getElementById(vm.id);
    thisMDCell.style.display = "none"

    // console.log(vm.markdownViewerProps)
    // console.log(vm.textCellContainer)

    // var thisMDCellContainer = document.getElementById(vm.containerId);
    // var thisMDCellToolBar = document.getElementById(vm.containerId);
    // console.log(thisMDCell.offsetHeight)
    // console.log(thisMDCellToolBar.offsetHeight)
    // console.log(thisMDCellContainer.offsetHeight)

    // thisMDCellContainer.style.height = thisMDCell.offsetHeight-thisMDCellToolBar.offsetHeight.offsetHeight
  },
};

export default MarkdownCell;
</script>

<style scoped>
.markdown-cell {
  /* display: none; */
  display: flex;
  flex-direction: column;
  position: relative;
  box-shadow: 0 4px 5px 0 rgb(0 0 0 / 14%), 0 1px 10px 0 rgb(0 0 0 / 12%),
    0 2px 4px -1px rgb(0 0 0 / 40%);
  width: 100%;
  height: 100%;
  /* margin-top: 1%; */
  min-height: 219px;
  overflow: visible;
}

.markdown-cell-toolbar {
  background-color: #f7f7f7;
  border-bottom: 1px solid #dadada;
  display: block;
  margin-bottom: 4px;
  overflow: show;
  padding-left: 4px;
  white-space: nowrap;
  width: 100%;
  height: 46.5px;
}

.markdown-cell-container {
  display: flex;
  flex-direction: row;
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  /* margin-top: 0%; */
  height: 100%;
}

button {
  margin-top: 8px;
  margin-bottom: 8px;
  margin-left: 8px;
  margin-right: 8px;
  background-color: none;
  padding: 5px;
  display: inline-block;
  max-height: 30px;
}
</style>
