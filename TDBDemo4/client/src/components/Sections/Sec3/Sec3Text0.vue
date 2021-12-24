<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";
import * as Vue from "vue/dist/vue.esm-bundler.js";

var Sec3Text0 = {
  name: "Sec3Text0",
  components: {
    ref,
    claim,
  },
  data() {
    return {
      textMD: "This <ref>is</ref> *default* textMD",
      textHTML: "This <ref>is</ref> *default* textHTML",
    };
  },
  methods: {
    getTextMD() {
      const path = "http://127.0.0.1:5000/sec2-text0-md";
      axios
        .get(path)
        .then((res) => {
          this.textMD = res.data[0].CONTENT;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  computed: {
    compiledMarkdown() {
      this.getTextMD();
      var gottenMD = marked(this.textMD, {
        sanitize: false,
      });
      this.textHTML = gottenMD; // 更新本component的data
      return gottenMD;
    },
  },
  created() {
    this.getTextMD();
  },
  updated() {
    console.log(this.textHTML);
  },
};
export default Sec3Text0;
</script>

<template>
  <div id="Sec3-Text0">
    <!-- <div v-html="compiledMarkdown"></div> -->
    <h3 id="Sec3-Text0-Title">
      3 「新しい生活様式」がすでに定着している企業は 10.0%
    </h3>
    <p class="leftP">
      「新しい生活様式」に対応した企業活動が社会全体として定着するのはいつ頃と考えているかを尋ねたところ、
      『2021 年中の定着を見込む』企業は、<ref>36.2%</ref>となり、<claim>3 社に 1 社が
      2021 年中に「新しい生活様式」に対応した企業活動が定着する</claim>と見込んでいた。
    </p>
    <p class="leftP">
      他方、『2020 年中の定着を見込む』企業は、<ref>17.5%</ref>
      となった。そのうち、<ref>10.0%</ref>の企業が「すでに定着している」と考えていた。
      とりわけ「電気通信」や「娯楽サービス」では、3割超の企業で既に定着しているとしており、
      サービス業を中心にその割合が高い。
    </p>
    <p class="leftBP">
      他方、「新しい生活様式に対応した企業活動は定着しない」とみている企業は
      <ref>11.9%</ref>となった。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
  margin-top: 12%;
}
p {
  text-indent: 2em;
  line-height: 2;
}
.leftP {
  margin-left: 20%;
}
.leftBP {
  margin-left: 20%;
}
</style>
