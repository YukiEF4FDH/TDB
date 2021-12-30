<template>
  <div id="Sec3-Chart0" class="rightC">
    <chart-info>2021 年の懸念材料（上位10 項目、3 つまでの複数回答）</chart-info>
    <table border="0" class="dataframe" id="T4B">
      <thead>
        <tr style="text-align: right">
          <th></th>
          <th></th>
          <th></th>
          <th class="thh">2020年11月調査</th>
          <th class="thh">&nbsp;&nbsp;2019年11月調査</th>
        </tr>
        <tr>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1</th>
          <td>感染症による影響の拡大</td>
          <td class="ic"></td>
          <td  class="t">60.7%</td>
          <td class="t"> - - </td>
        </tr>
        <tr>
          <th>2</th>
          <td>所得（減少）</td>
          <td class="ic"> <img src="up.png" width="20"/> </td>
          <td class="t">22.7%</td>
          <td class="t">11.8% (9)</td>
        </tr>
        <tr>
          <th>3</th>
          <td>米国経済</td>
          <td class="ic"></td>
          <td class="t">22.5%</td>
          <td class="t">22.0% (4)</td>
        </tr>
        <tr>
          <th>4</th>
          <td>雇用（悪化）</td>
          <td class="ic"><img src="up.png" width="20"/></td>
          <td class="t">  21.2%</td>
          <td class="t">15.7% (7)</td>
        </tr>
        <tr>
          <th>5</th>
          <td>中国経済</td>
          <td class="ic"><img src="down.png" width="20"/></td>
          <td class="t">  14.3%</td>
          <td class="t">36.6% (2)</td>
        </tr>
        <tr>
          <th>6</th>
          <td>人手不足</td>
          <td class="ic"><img src="down.png" width="20"/> </td>
          <td class="t"><claim>12.8%</claim></td>
          <td class="t"><con>40.9%</con> (1)</td>
        </tr>
        <tr>
          <th>7</th>
          <td>原油・素材価格（上昇）</td>
          <td class="ic"><img src="down.png" width="20"/> </td>
          <td class="t">
            10.2%
          </td>
          <td class="t">
            19.5% (5)
          </td>
        </tr>
        <tr>
          <th>8</th>
          <td>訪日観光客数の減少</td>
          <td class="ic"><img src="up.png" width="20"/> </td>
          <td class="t"> 10.2%</td>
          <td class="t">2.3% (20)</td>
        </tr>
        <tr>
          <th>9</th>
          <td>貿易摩擦の激化</td>
          <td class="ic"><img src="down.png" width="20"/> </td>
          <td class="t">7.1%</td>
          <td class="t">25.0% (3)</td>
        </tr>
        <tr>
          <th>10</th>
          <td>為替（円高）</td>
          <td class="ic"></td>
          <td  class="t">6.9%</td>
          <td class="t">8.6% (11)</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import * as d3 from "d3";
// import SunburstChart from "@/components/Visualization/SunburstChart.vue";

import con from "@/components/context.vue";
import claim from "@/components/claim.vue";

var f1aData = "default";

export default {
  name: "Sec3Chart0",
  data() {
    var data = null;
    return { data };
  },
  components: { claim,con },
  methods: {
    draw() {
      // for (let i=0; i<Object.assign({},Object.assign({}, this.data).children).length; i++)
      // SunburstChart.methods.draw(this.data, "#svg4");
    },

    getF1AJson() {
      // const path = "http://127.0.0.1:5000/f3a-json";
      // axios
      //   .get(path)
      //   .then((res) => {
      //     f1aData = res.data;
      //     if (f1aData != "default") {
      //       f1aData = JSON.parse(f1aData);
      //       let arr = f1aData.map(function (d) {
      //         return [d.name, d.value];
      //       });
      //       this.data = arr;
      //       this.draw();
      //     }
      //   })
      //   .catch((error) => {
      //     console.error(error);
      //   });
    },
  },
  mounted() {
    // this.getF1AJson();
  },
};
</script>

<style scoped>
chart-info {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  margin-top: 10%;
  margin-left: 30%;
}
.rightC {
  margin-left: 30%;
  margin-top: -29%;
  margin-bottom: 10%;
}

table {
  width: 100%;
}
button {
  width: 100%;
}

table,
td,
th {
  border-spacing: 0;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  margin-top: 1%;
}
.ic {
    text-align: right;
    width: 0;
}
.t {
      text-align: left;
      text-indent: 2em;
}
.thh {
      text-align: left;
      text-indent: 10;
}
thead {
  border-spacing: 0 0 0 1px;
  border-bottom: solid 1px #aaa;
  background-color: #ddd;
}

tbody tr:nth-child(even) {
  background-color: #eee;
  text-align: center;
}

tbody tr:nth-child(odd) {
  background-color: white;
  text-align: center;
}
</style>