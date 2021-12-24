<template>
  <span
    class="reference"
    :id="this.id"
    @mouseover="setHover($event)"
    @mouseleave="setLeave($event)"
  >
    <slot> </slot>
  </span>
</template>

<script>
import * as d3 from "d3";
import Curve from "@/components/Curve.vue";

let reference_id = 0;
let colorP={}; 
export default {
  name: "ref",
  data() {
    return {
      id: "ref" + reference_id,
      text: "default",
    };
  },
  created() {
    this.id = "ref" + reference_id++; // data.id更新

    const _default = this.$slots.default();
    if (_default && _default.length > 0) this.text = _default[0].children; // data.text更新
  },
  methods: {
    setHover: function () {
      if (this.id == "ref0") {
        d3.select("#svg1")
          .selectAll("rect")
          .each(function (d) {
            d3.select("#" + this.id).attr("fill", "#cacaca");
          });

        d3.select(document.getElementById("F1A_1_1a"))
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5");

        d3.select(document.getElementById("F1A_1_1b"))
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5");

        d3.select("#Sec1")
          .append("svg")
          .attr("id", "svg1Curve0")
          .text(function (d) {
            return d;
          });

        let cId = "#svg1Curve0";
        Curve.methods.drawCurve(cId);
      } else if (this.id == "ref2") {
        d3.select("#svg2").selectAll("rect").attr("fill", "#cacaca");

        d3.select(document.getElementById("#svg2bar1"))
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5");
      } else if (this.id == "ref3") {
        d3.select("#svg2").selectAll("rect").attr("fill", "#cacaca");

        d3.select(document.getElementById("#svg2bar2"))
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5");

        d3.select("#Sec2")
          .append("svg")
          .attr("id", "svg2Curve2")
          .text(function (d) {
            return d;
          });

          let cId = "#svg2Curve2";
        Curve.methods.drawCurve(cId);
      } 
      else if (this.id == "ref5") {
      let index = 0;

         d3.select("#svg4").selectAll("path").each(function (d) {
            colorP[this.id] = document.getElementById(this.id).getAttribute("fill");
          });
        d3.select("#svg4").selectAll("path").attr("fill", "#cacaca");

        d3.select(document.getElementById("path1"))
          .attr("fill", "#cae6b6")
          .attr("stroke", "#aabe9b")
          .attr("stroke-width", "5");

        d3.select("#Sec3")
          .append("svg")
          .attr("id", "svg4Curve1")
          .text(function (d) {
            return d;
          });

          let cId = "#svg4Curve1";
        Curve.methods.drawCurve(cId);
      } 
      console.log(this.id);
    },
    setLeave: function () {
      if (this.id == "ref0") {
        d3.select(document.getElementById("F1A_1_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_2_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_3_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_4_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_5_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_6_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_7_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_8_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_9_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );
        d3.select(document.getElementById("F1A_10_1a")).attr(
          "fill",
          "rgb(215, 25, 28)"
        );

        d3.select(document.getElementById("F1A_1_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_2_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_3_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_4_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_5_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_6_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_7_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_8_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_9_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );
        d3.select(document.getElementById("F1A_10_1b")).attr(
          "fill",
          "rgb(253, 174, 97)"
        );

        d3.select(document.getElementById("F1A_1_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_2_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_3_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_4_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_5_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_6_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_7_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_8_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_9_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );
        d3.select(document.getElementById("F1A_10_2")).attr(
          "fill",
          "rgb(255, 255, 191)"
        );

        d3.select(document.getElementById("F1A_1_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_2_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_3_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_4_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_5_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_6_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_7_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_8_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_9_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );
        d3.select(document.getElementById("F1A_10_3")).attr(
          "fill",
          "rgb(171, 221, 164)"
        );

        d3.select(document.getElementById("F1A_1_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_2_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_3_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_4_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_5_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_6_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_7_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_8_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_9_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_10_4")).attr(
          "fill",
          "rgb(43, 131, 186)"
        );
        d3.select(document.getElementById("F1A_1_1a")).attr(
          "stroke-width",
          "0"
        );
        d3.select(document.getElementById("F1A_1_1b")).attr(
          "stroke-width",
          "0"
        );
        var elem = document.getElementById("svg1Curve0");
        elem.remove();
      }
      else if (this.id=="ref3")
      {
        d3.select(document.getElementById("#svg2bar1"))
        .attr("fill", "rgb(215, 25, 28)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar2"))
        .attr("fill", "rgb(253, 174, 97)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar3"))
        .attr("fill", "rgb(255, 255, 191)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar4"))
        .attr("fill", "rgb(171, 221, 164)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar5"))
        .attr("fill", "rgb(43, 131, 186)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar6"))
        .attr("fill", "rgb(215, 25, 28)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar7"))
        .attr("fill", "rgb(253, 174, 97)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar8"))
        .attr("fill", "rgb(255, 255, 191)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg2bar9"))
        .attr("fill", "rgb(171, 221, 164)").attr("stroke-width", "0");
        
        let elem = document.getElementById("svg2Curve2");
        elem.remove();
      }
       else if (this.id=="ref5")
      {
        console.log(colorP);
      

        d3.select("#svg4").selectAll("path").each(function (d) {
          d3.select(document.getElementById(this.id))
          .attr("fill", colorP[this.id]).attr("stroke-width", "0");
        });
        
        let elem = document.getElementById("svg4Curve1");
        elem.remove();
      }
    },
  },
};
</script>

<style>
.reference {
  font-weight: bold;
  padding-left: 0.2em;
  padding-right: 0.2em;
}

.reference {
  /* background-color: #bfb; */
  /* background-color: #ff0000; */
  background-image: url("../pics/ref.png");
  background-size: 120%;
  background-repeat: no-repeat;
}
</style>
