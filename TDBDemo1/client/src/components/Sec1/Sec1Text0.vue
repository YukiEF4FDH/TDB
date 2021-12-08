<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";
import * as Vue from "vue/dist/vue.esm-bundler.js";

var Sec1Text0 = {
  name: "Sec1Text0",
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
      const path = "http://127.0.0.1:5000/sec1-text0-md";
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
      // gottenMD = gottenMD.replace("<ref>", "<span class=\"reference\">");
      // gottenMD = gottenMD.replace("</ref>", "</span>");
      // console.log(gottenMD);

    //   // var res = Vue.compile(gottenMD);
    //   var res = new Vue.h("div", {}, gottenMD);
    //   // var res = Vue.compile('<div><span>aaa</span></div>');
    //   console.log(res);
    //   gottenMD = res.children;

      return gottenMD;
    },
  },
  created() {
    this.getTextMD();
  },
  updated() {
    console.log(this.textHTML); // 已经更新了
  },
};
export default Sec1Text0;
</script>

<template>
  <div id="Sec1-Text0">
    <!-- <div v-html="compiledMarkdown"></div> -->
    <h3 id="Sec1-Text0-Title">
      1.「今後マイナスの影響がある」が 11.1%、10 月より 2.5 ポイント増加
    </h3>
    <p class="leftP">
      新型コロナウイルス感染症により自社の業績にどのような影響があるか尋ねたところ、『マイナスの影響がある』(「既にマイナスの影響がある」
      と「今後マイナスの影響がある」の合計)と見込む企業は<ref>83.7% </ref>
      となった。<claim>10 月より 0.5 ポイント増加し</claim>、<claim>3 カ月ぶりに増加に転じた</claim>。特に「今後マイナスの影響がある」は、<claim>10 月 より 2.5 ポイント増加 </claim>しており、感染拡大の第 3
      波の影響により、先行きを懸念する企業が増えたとみられる。
    </p>
    <p  class="leftP">
      他方、『プラスの影響がある』(「既にプラスの影響がある」と「今後プラスの影響がある」の合計)と見込む企業は
      <ref>4.6%</ref>となり、<claim>2 月以降微増傾向を示している</claim>。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
	text-indent:2em;
}
.leftP {
  margin-right:60%;
}
</style>
