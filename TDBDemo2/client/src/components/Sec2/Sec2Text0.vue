<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";

var Sec2Text0 = {
  name: "Sec2Text0",
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
export default Sec2Text0;
</script>

<template>
  <div id="Sec2-Text0">
    <!-- <div v-html="compiledMarkdown"></div> -->
    <h3 id="Sec2-Text0-Title">
      2. 2021 年の景気は「悪化」見込みが32.4％、特に『金融』『建設』『不動産』が高水準
    </h3>
    <p class="leftP">
      2021 年の景気について、「回復」局面になると見込む企業は2020 年の景気見通し（2019 年11
      月実施）から<claim>6.4 ポイント増</claim>の<ref>13.4％</ref>となった。企業からは、「ワクチン接種で感染者が世界的に
      抑えられれば、大きく改善が見込まれる」（機械・器具卸売）など、ワクチンの開発に期待する声
      が多く聞かれた。また、「踊り場」局面は<ref>31.1％</ref>と2020 年見通し（<ref>33.4％</ref>）より<claim>減少した</claim>。「悪化」
      局面を見込む企業は<ref>32.4％</ref>と2020 年見通しより<claim>減少した</claim>ものの、<claim>3 割を上回り</claim>依然として高水準
      となっている。
    </p>
    <p class="leftP">
      「回復」局面と見込む企業を業界別にみると、『運輸・倉庫』(<ref>24.1％</ref>)や『製造』(<ref>17.2％</ref>)が高
      い。対して「悪化」局面では、『金融』(<ref>57.1％</ref>)、『建設』(<ref>49.0％</ref>)、『不動産』(<ref>43.8％</ref>)の高水準
      が目立つ。企業からは、「世の中全体が暗い感じ。一部の好景気業界はあるものの、ごく一部に限
      られており、全体としては良くない」（建設）や「金融緩和による資金供給や補助金などの資金供
      給がなければ、実質破綻となる企業・個人が多く存在すると考える」（不動産）、「2020 年というよ
      りも2019 年10 月の消費税アップから景気は冷え込んできている」（飲食料品卸売）などの意見が
      聞かれた。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
	text-indent:2em;
  line-height: 1.45;
}
.leftP {
  margin-left: 34%;
}
</style>
