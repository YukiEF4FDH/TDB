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
    <h3 id="Sec2-Text0-Title">2. 2020 年の事業承継動向</h3>
    <h4 id="Sec2-Text0-Title3 ">
      ◇ 就任経緯 <br />
      〜同族承継による就任は年々減少〜
    </h4>
    <p class="leftP">
      2018 年以降の事業承継が判明した346
      社について、先代経営者との関係性（就任経緯別）をみると、 2020
      年の事業承継は「同族承継」により引き継いだ割合が46.7％で全項目中最も高かった。しかし、
      2019 年（55.4％）と比較すると8.7pt
      低下するなど「同族承継」による事業承継は減少している。
    </p>
    <p class="leftP">
      一方、「内部昇格」による事業承継は31.1%となり、2019 年 （23.1％）から8.0pt
      上昇し「同族承継」に次ぐ割合となっ た。「外部招聘」は2 年連続で低下した。 
    </p>
    <p class="leftP">
      熊本企業の事業承継は依然として親族など同族間での事業
      引き継ぎが多いものの、「内部昇格」が上昇していることから、
      社内で実績のある幹部人材が社長に就任している傾向がみて とれる。
    </p>
  </div>
</template>

<style scoped>
h3 {
  text-decoration: underline;
}
p {
  text-indent: 2em;
  line-height: 2.45;
}
.leftP {
  margin-right: 54%;
}
</style>
