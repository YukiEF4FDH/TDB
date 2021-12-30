<script>
import axios from "axios";
import marked from "marked";
import ref from "@/components/ref.vue";
import claim from "@/components/claim.vue";

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
      3. 2021 年景気の懸念材料、新型コロナ関連の項目が上位に
    </h3>
    <p class="leftP">
      2021 年の景気に悪影響を及ぼす懸念材料を尋ねたところ、新型コロナなどの「感染症による影
      響の拡大」が60.7％で突出して高かった（複数回答3 つまで、以下同）。次いで、「所得（減少）」
      （22.7％）や「米国経済」(22.5％）のほか、「雇用(悪化)」（21.2％）や「中国経済」（14.3％）、
      インバウンド需要を大きく左右する「訪日観光客数の減少」（10.2％）といった、海外経済と関連
      する項目が続いた。また、2019 年まで
      多くの企業が懸念材料に挙げていた
      「人手不足」は、12.8％と大幅に減少し
      ており、新型コロナによる業務量の減
      少などの影響を受け、変化が表れてい
      た様子がうかがえる。
    </p>
    <p class="bottomP">
      企業からも、「税収が落ち込み、経済
      対策に回せる予算がなくなる」（精密機
      械、医療機械・器具製造）や「今後の個
      人消費傾向によるところが大きい。イ
      ンバウンド需要を回復していかないと
      色々なところに影響が出続ける」（輸送
      用機械・器具製造）、「新型コロナの動向
      次第で、世界的経済状況の悪化があり
      得る」（不動産）などの声が挙げられた。
      <br><br><br><br>
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
  text-indent: 2em;
  line-height: 1.45;
}
.leftP {
  margin-left: 0%;
  margin-right: 72%;
}
.bottomP {
  margin-bottom: 10%;
}
</style>
