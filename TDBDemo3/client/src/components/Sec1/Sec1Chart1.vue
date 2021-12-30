<template>
  <div id="Sec1-Chart1" class="rightC">
      <table border="0" class="dataframe" id="T4B">
      <thead>
        <tr style="text-align: right">
          <th></th>
          <th>2020年11月</th>
          <th>2020年10月</th>
          <th>2020年9月</th>
          <th>2020年8月</th>
          <th>2020年7月</th>
          <th>2020年6月</th>
          <th>2020年6月</th>
          <th>2020年6月</th>
          <th>2020年6月</th>
          <th>2020年6月</th>
        </tr>
        <tr>
          <th>業種</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>農・林・水産</th>
          <td
            id="T4B_IND1_20_11"
            hl=""
            bold=""
            :class="{ hl1: hl1 == '21C-1' || hl1 == '21C-2' }"
          >
            100.0%
          </td>
          <td>100.0%</td>
          <td>100.0%</td>
          <td>100.0%</td>
          <td>100.0%</td>
          <td id="T4B_IND1_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            100.0%
          </td>
          <td>100.0%</td>
          <td>100.0%</td>
          <td>100.0%</td>
          <td>0.0%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND2"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_1' }"
          >
            運輸・倉庫
          </th>
          <td
            id="T4B_IND2_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_1' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_1',
            }"
          >
            <!-- @mouseover="set($event)" @mouseleave="set($event)" -->
            91.3%
          </td>
          <td
            id="T4B_IND2_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_1',
              bold: bold == '21A_1',
            }"
          >
            <!-- @mouseover="set($event)" @mouseleave="set($event)" -->
            91.8%
          </td>
          <td>91.9%</td>
          <td>86.3%</td>
          <td>89.7%</td>
          <td id="T4B_IND2_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            92.6%
          </td>
          <td>93.7%</td>
          <td>87.3%</td>
          <td>88.2%</td>
          <td>80.6%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND3"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_2' }"
          >
            金融
          </th>
          <td
            id="T4B_IND3_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_2' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_2',
            }"
          >
            90.9%
          </td>
          <td
            id="T4B_IND3_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_2',
              bold: bold == '21A_2',
            }"
          >
            100.0%
          </td>
          <td>84.6%</td>
          <td id="T4B_IND3_20_8" hl="" bold="" :class="{ hl2: hl2 == '21C-1' }">
            75.0%
          </td>
          <td>92.3%</td>
          <td id="T4B_IND3_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            92.3%
          </td>
          <td>92.3%</td>
          <td>100.0%</td>
          <td>92.9%</td>
          <td>66.7%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND4"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_3' || hl3 == '21B' }"
          >
            製造
          </th>
          <td
            id="T4B_IND4_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_3' ||
                hl1 == '21B' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_3',
            }"
          >
            84.4%
          </td>
          <td
            id="T4B_IND4_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_3' || hl2 == '21B',
              bold: bold == '21A_3',
            }"
          >
            85.4%
          </td>
          <td id="T4B_IND4_20_9" hl="" bold="" :class="{ hl2: hl2 == '21B' }">
            89.0%
          </td>
          <td>89.2%</td>
          <td>86.8%</td>
          <td id="T4B_IND4_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            90.2%
          </td>
          <td>87.4%</td>
          <td>91.7%</td>
          <td>81.5%</td>
          <td>68.0%</td>
        </tr>
        <tr>
          <th>卸売</th>
          <td
            id="T4B_IND5_20_11"
            hl=""
            bold=""
            :class="{ hl1: hl1 == '21C-1' || hl1 == '21C-2' }"
          >
            84.2%
          </td>
          <td>83.6%</td>
          <td>84.6%</td>
          <td>85.4%</td>
          <td>86.6%</td>
          <td id="T4B_IND5_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            87.5%
          </td>
          <td>90.1%</td>
          <td>91.8%</td>
          <td>84.3%</td>
          <td>76.6%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND6"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_4' }"
          >
            不動産
          </th>
          <td
            id="T4B_IND6_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_4' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_4',
            }"
          >
            82.7%
          </td>
          <td
            id="T4B_IND6_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_4',
              bold: bold == '21A_4',
            }"
          >
            83.0%
          </td>
          <td>89.5%</td>
          <td>87.9%</td>
          <td>87.7%</td>
          <td id="T4B_IND6_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            96.5%
          </td>
          <td>89.8%</td>
          <td>93.2%</td>
          <td>90.0%</td>
          <td>45.1%</td>
        </tr>
        <tr>
          <th>建設</th>
          <td
            id="T4B_IND7_20_11"
            hl=""
            bold=""
            :class="{ hl1: hl1 == '21C-1' || hl1 == '21C-2' }"
          >
            81.7%
          </td>
          <td
            id="T4B_IND7_20_10"
            hl=""
            bold=""
            :class="{ hl2: hl2 == '21C-1' }"
          >
            73.8%
          </td>
          <td id="T4B_IND7_20_9" hl="" bold="" :class="{ hl2: hl2 == '21C-1' }">
            76.8%
          </td>
          <td>84.4%</td>
          <td>80.7%</td>
          <td id="T4B_IND7_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            81.1%
          </td>
          <td>85.8%</td>
          <td>89.9%</td>
          <td>79.5%</td>
          <td>58.8%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND8"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_5' }"
          >
            小売
          </th>
          <td
            id="T4B_IND8_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_5' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_5',
            }"
          >
            81.0%
          </td>
          <td
            id="T4B_IND8_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_5',
              bold: bold == '21A_5',
            }"
          >
            85.7%
          </td>
          <td>82.5%</td>
          <td id="T4B_IND8_20_8" hl="" bold="" :class="{ hl2: hl2 == '21C-1' }">
            79.4%
          </td>
          <td id="T4B_IND8_20_7" hl="" bold="" :class="{ hl2: hl2 == '21C-1' }">
            78.5%
          </td>
          <td id="T4B_IND8_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            86.4%
          </td>
          <td>92.9%</td>
          <td>90.5%</td>
          <td>87.1%</td>
          <td>75.0%</td>
        </tr>
        <tr>
          <th
            id="T4B_IND9"
            hl=""
            bold=""
            :class="{ hl3: hl3 == '21A' || hl3 == '21A_6' || hl3 == '21B' }"
          >
            サービス
          </th>
          <td
            id="T4B_IND9_20_11"
            hl=""
            bold=""
            :class="{
              hl1:
                hl1 == '21A' ||
                hl1 == '21A_6' ||
                hl1 == '21B' ||
                hl1 == '21C-1' ||
                hl1 == '21C-2',
              bold: bold == '21A_6',
            }"
          >
            80.6%
          </td>
          <td
            id="T4B_IND9_20_10"
            hl=""
            bold=""
            :class="{
              hl2: hl2 == '21A' || hl2 == '21A_6' || hl2 == '21B',
              bold: bold == '21A_6',
            }"
          >
            81.6%
          </td>
          <td id="T4B_IND9_20_9" hl="" bold="" :class="{ hl2: hl2 == '21B' }">
            82.7%
          </td>
          <td>86.3%</td>
          <td>82.8%</td>
          <td id="T4B_IND9_20_6" hl="" bold="" :class="{ hl1: hl1 == '21C-1' }">
            84.5%
          </td>
          <td>86.4%</td>
          <td>90.2%</td>
          <td>81.1%</td>
          <td>55.3%</td>
        </tr>
        <tr>
          <th></th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
import StackedBarWithLine from "@/components/Visualization/StackedNormalizedHorizontalBarWithLine.vue"

var f1aData = "default";

export default {
  name: "Sec1Chart1",
  data() {
    var data = null;
    return {
      data,
    };
  },
  components: {},
  methods: {
    draw() {
    //   StackedBarWithLine.methods.draw(this.data,'#svg01',0.5,0);
    },
    drawCurvedLine() {
    },
    getF1AJson() {
      const path = "http://127.0.0.1:5000/f1a-json";
      axios
        .get(path)
        .then((res) => {
          f1aData = res.data;
          if (f1aData != "default") {
            f1aData = JSON.parse(f1aData);
            var columns = Object.keys(f1aData[0]);
            columns = columns.slice(0, columns.length - 1);
            // // console.log(columns);
            f1aData.columns = columns;
            // console.log("f1aData");
            // console.log(f1aData);

            // f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
            f1aData = f1aData.sort((a, b) => b[1] / b.total - a[1] / a.total);
            this.data = f1aData;
            this.draw();
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.getF1AJson();
    // this.drawCurvedLine();
  },
};
</script>

<style scoped>
chart-info {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  text-align: center;
  margin-left: 30%;
  margin-top: 10%;
}
.rightC {
  margin-left: 40%;
  margin-top: 0%;
  margin-right: 2%;
}
#svgCurve2 {
  position: absolute;
  border: 2px dashed purple;
  width: 200px;
  height: 120px;
  left: 11%;
}
#svgCurve2 {
  font-size: 14px;
  color: #0000ff;
  font-weight: bold;
  text-align: center;
  margin-left: 30%;
}

table { width: 98%; }
button { width: 100%; }

table, td, th {
  border-spacing: 0;
  border-collapse: collapse;
  margin-top: 7ex;
  margin-bottom: 7ex;
  margin-left: auto;
  margin-right: auto;
  text-align: center; 
}

th {
    height: 2ex;
}


thead {
  border-spacing: 0 0 0 1px;
  border-bottom: solid 1px #aaa;
  background-color: #ddd;
}

tbody tr:nth-child(even)
{background-color: #eee; text-align: center; }

tbody tr:nth-child(odd)
{ background-color: white;text-align: center; } 

</style>