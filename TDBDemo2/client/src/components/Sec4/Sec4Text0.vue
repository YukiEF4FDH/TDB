<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";
import * as Vue from "vue/dist/vue.esm-bundler.js";

var Sec4Text0 = {
  name: "Sec4Text0",
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
export default Sec4Text0;
</script>

<template>
  <div id="Sec4-Text0">
    <h3 id="Sec4-Text0-Title" margin-top="100%">
      4. バイデン米新大統領就任時の日本経済への影響、「分からない」が4 割
    </h3>
    <p class="leftP">
      バイデン氏は国際協調を重視する姿勢を打ち出すな
      ど、米国における政策の転換が予想され、対日政策にも
      注目が集まっている。そこで、バイデン氏が新大統領に
      就任した場合、日本経済にどのような影響を与えると
      思うか尋ねたところ、「プラスの影響」が<ref>16.6％</ref>となり、
      「マイナスの影響」の<ref>14.2％</ref>を上回ったものの、いず
      れも<claim>1 割台にとどまった</claim>。「影響はない」は<ref>29.4％</ref>だっ
      た。「分からない」(<ref>39.9％</ref>)が<claim>約4 割を占めており</claim>、現
      時点では影響を捉えかねている様子がうかがえた。
      企業からは、「米中関係の改善を期待している」（情報
      サービス）、「現在のトランプ大統領から、バイデン氏に
      代わっても、アメリカの内向きな姿勢に変化はないと
      思われる」(運輸・倉庫)などの意見が挙げられた。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
  text-indent: 2em;
  line-height: 2.5;
}
.leftP {
  margin-left: 0%;
  margin-right: 30%;
}

</style>
