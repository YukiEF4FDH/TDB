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
      1. 2020 年の「後継者不在」状況
    </h3>
    <p class="leftP">
      調査対象となった3014 社について後継者の有無を集計す
      ると、1498 社（構成比49.7％）が「後継者あり」となってい
      る一方で、50.3％にあたる1516 社が「後継者不在」1であるこ
      とが分かった。後継者不在率は2019 年に比べて2.5pt 上昇。
      2011 年と比べると7.0pt 上昇した。過年度の全国調査2を含め
      ると、九州における後継者不在率は全国平均を下回っており、
      熊本県は九州内でも最も低かったものの、上昇傾向が続いて
      おり、過去最高となった。
    </p>
    <h4 id="Sec1-Text0-Title2">
      ◇ 業種別
    </h4>
    <p  class="pp">
      最も後継者不在率が高いのは、建設（59.3％）、
      サービス（54.8％）と続いた。
    </p>
    <p  class="pp">
      2019 年との比較では、建設、卸売、小売、運輸・
      通信、サービス、その他が上昇、製造、不動産が
      低下している。いずれも全国平均を下回っている
      が、中分類でみても不在率の高い建設やサービス
      はほとんどの業種（中分類）が前年を上回ってい
      る。
    </p>
    <h4 id="Sec1-Text0-Title3 ">
      ◇ 地域・都道府県別
    </h4>
    <p>
      地域別の後継者不在状況をみると9 地域中4 地域で前年を下回った。「北海道」では調査開始以来
      一貫して全地域中最も高いものの、3 年連続で前年を下回った。「関東」、「近畿」では過去最低となっ
      た。<br>
      一方、「四国」、「九州」は5 年連続、「中国」2 年連続で上昇。「中部」は3 年ぶり、「北陸」は2 年
      ぶりに増加した。特に、中国以西の西日本地域で後継者不在率が上昇している。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
	text-indent:2em;
  line-height: 2;
}
.pp{
  margin-right:60%;
	text-indent:2em;
  line-height: 2.5;
}
.leftP {
  margin-right:60%;
}
</style>
