<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";
import * as vue from 'vue';
import VRuntimeTemplate from "v-runtime-template";

var Sec1Text0 = {
  name: "Sec1Text0",
  components: {
    ref,
    claim,
    VRuntimeTemplate 
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
      // return h(compile('<ref>xxx</ref>'));
      // return gottenMD;
      // return '<reference>xxx</reference>';
      console.log(vue.compile());
      return '<p>xxx</p>';
    },
  },
  render(h)
  {
    return h(vue.compile('<ref>xxx</ref>'));
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
  <!-- <div>{{compiledMarkdown}}</div> -->
  <!-- <div v-html="compiledMarkdown"></div> -->
    <!-- <v-runtime-template :template="compiledMarkdown"></v-runtime-template> -->
  <!-- <Sec1Text0: code="compiledMarkdown"/> -->
  <div id="Sec1-Text0">
    <h3 id="Sec1-Text0-Title">
      1.「今後マイナスの影響がある」が 11.1%、10 月より 2.5 ポイント増加
    </h3>
    <p>
      新型コロナウイルス感染症により自社の業績にどのような影響があるか尋ねたところ、『マイナスの影響がある』(「既にマイナスの影響がある」
      と「今後マイナスの影響がある」の合計)と見込む企業は<ref>83.7% </ref>
      となった。<claim>10 月より 0.5 ポイント増加し</claim>、<claim>3 カ月ぶりに増加に転じた</claim>。
      特に「今後マイナスの影響がある」は、<claim>10 月 より 2.5 ポイント増加 </claim>しており、感染拡大の第 3
      波の影響により、先行きを懸念する企業が増えたとみられる。
    </p>
    <p>
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
  text-indent: 2em;
  margin-right: 60%;
}
</style>
