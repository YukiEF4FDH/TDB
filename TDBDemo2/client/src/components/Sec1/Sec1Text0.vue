<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";

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
      1. 2020 年の景気は「悪化」局面が54.2％、リーマン時以来12 年ぶり5 割超に上昇
    </h3>
    <p class="leftP">
      2020 年の景気動向について尋ねたところ、
      「回復」局面であったと考える企業は<ref>3.0％</ref>にとどまり、
      2019 年の景気動向（前回調査、2019 年11 月実施）と同水準となり、
      <claim>2年連続で1ケタ台</claim>となった。他方、「踊り場」局面とした企業は<ref>29.1％</ref>で、
      <claim>前年から大きく減少した</claim>。また、「悪化」局面とした企業は同 <claim>21.5 ポイント増</claim>の<ref>54.2％</ref>で、
      リーマン・ショックのあった2008 年以来<claim>12 年ぶりに5 割超えの水準へと上昇した</claim>。
      「分からない」は<claim>13.8％</claim>だった。
    </p>
    <p  class="leftP">
      2020 年を「回復」局面とした企業からは、「コロナの収束状況にもよるが、ほぼ悪い材料が出尽
      くした」（機械製造）といった声が聞かれたほか、新型コロナによる環境の変化を前向きに捉えて
      いる様子もみられた。また、「踊り場」局面とみる企業からは、「取引先によっては、コロナ特需を
      受けた業種もあれば、先行き不透明に陥っている業種もあり、結果として慎重な動きになっている」（不動産）や
      「今後どちらに向かうかは各企業の経営戦略次第」（建設）など、
      新型コロナの状況の変化による浮き沈みについて指摘する意見が多い。
    </p>
    <p  class="leftP">
      他方、「悪化」局面とみている企業からは新型コロナの影響として、「各企業ともに慎重になっている。計画した
      ものはこなすものの、新しい開発品の話がほとんど止まっている」（化学品製造）といった声のほか、「事業用賃貸
      の家賃値下げ交渉が多々あり、情勢を考慮すると対応せざるを得ない」（土地売買）といった意見が、業界や地域を
      問わず多く聞かれた。
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
