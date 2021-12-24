<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";
import * as Vue from "vue/dist/vue.esm-bundler.js";

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
      2.『マイナスの影響』は 5 カ月ぶりに全業界で 8 割超、『プラスの影響』は「小売」がトップ
    </h3>
    <p class="leftP">
      『マイナスの影響がある』割合を業界別にみると、9業界中6業界（運輸・倉庫、金融、製造、不動産、小売、サービス）で10月を下回った。特に、
			『製造』『サービス』では3カ月連続で減少しており、マイナスの影響は僅かながらも緩和している。しかし、6月以降5カ月ぶりに<claim>全業界で8割を超える</claim>など、依然として
		<claim>
			大半の企業がマイナスの影響を認識しており</claim>、不透明な状況は続いている。
    </p>
    <p class="leftP">
      他方、『プラスの影響がある』では、 『小売』が <ref>10.3%</ref> で<claim>最も高かった</claim>。
      次いで、 『金融』( <ref>9.1%</ref> ) 、『製造』( <ref>5.8%</ref> )が続く。
      9 業界中 6 業界( 小売、 金融、 製造、 サービス、 不動産、 運輸・倉庫) では 10 月を上回り 、飲食料品を取り扱う業種が上位に並んだ。
      しかし、 『卸売』『建設』のように 10 月を下回る業界もある など、 プラスの影響は一部の企業にとどまり、依然として<claim>大半の企業が業績にマイナスの影響を受けている</claim>。
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
