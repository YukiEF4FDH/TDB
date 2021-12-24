<template>
  <span
    class="claim"
    :claim_id="this.id"
    @mouseover="setHover($event)"
    @mouseleave="setLeave($event)"
  >
    <slot> </slot>
  </span>
</template>

<script>
import * as d3 from "d3";
import Curve from "./Curve.vue";

let claim_id = 0;
// let oldColor="";

export default {
  name: "claim",
  data() {
    return {
      id: 0,
      text: "default",
    };
  },
  created() {
    this.id = "claim" + claim_id++; // data.id更新

    const _default = this.$slots.default();
    if (_default && _default.length > 0) this.text = _default[0].children; // data.text更新
  },
  methods: {
    setHover: function () {
      if (this.id == "claim0") {
        d3.select("#svg1")
          .selectAll("rect")
          .each(function (d) {
            d3.select("#" + this.id).attr("fill", "#cacaca");
          });
        d3.select(document.getElementById("F1A_1_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_2_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");

        d3.select(document.getElementById("F1A_1_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_2_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select("#Sec1")
          .append("svg")
          .attr("id", "svgCurve3")
          .text(function (d) {
            return d;
          });

        Curve.methods.drawCurve2("svgCurve3");
      } else if (this.id == "claim1") {
        d3.select("#svg1")
          .selectAll("rect")
          .each(function (d) {
            d3.select("#" + this.id).attr("fill", "#cacaca");
          });
        d3.select(document.getElementById("F1A_1_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_2_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");

        d3.select(document.getElementById("F1A_1_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_2_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_3_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");

        d3.select(document.getElementById("F1A_3_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_4_1a"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select(document.getElementById("F1A_4_1b"))
          .attr("fill", "#fbb")
          .attr("stroke", "#d39d9c")
          .attr("stroke-width", "5");
        d3.select("#Sec1")
          .append("svg")
          .attr("id", "svg1Curve4")
          .text(function (d) {
            return d;
          });

        Curve.methods.drawCurve2("svg1Curve4");
      } else if (this.id == "claim4") {
        let index = 1;
        while (index <= 9) {
          d3.select(document.getElementById("#svg3bar"+index))
            .attr("fill", "#fbb")
            .attr("stroke", "#d39d9c")
            .attr("stroke-width", "5");
            index++;
        }

        d3.select("#Sec2")
          .append("svg")
          .attr("id", "svg2Curve1")
          .text(function (d) {
            return d;
          });

        Curve.methods.drawCurve2("svg2Curve1");
      }
      // d3.select(document.getElementById("F1A_1_1b")).attr("fill", "#cae6b6").attr("stroke", "#aabe9b").attr("stroke-width","5");
    },
    setLeave: function () {
      if (this.id == "claim0") {
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
        d3.select("#svg1")
          .selectAll("rect")
          .each(function (d) {
            d3.select("#" + this.id).attr("stroke-width", "0");
          });
        let elem = document.getElementById("svgCurve3");
        elem.remove();
      } 
      else if (this.id == "claim1") {
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
        d3.select("#svg1")
          .selectAll("rect")
          .each(function (d) {
            d3.select("#" + this.id).attr("stroke-width", "0");
          });
        let elem = document.getElementById("svg1Curve4");
        elem.remove();
      }
      else if (this.id=="claim4")
      {
        d3.select(document.getElementById("#svg3bar1"))
        .attr("fill", "rgb(215, 25, 28)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar2"))
        .attr("fill", "rgb(253, 174, 97)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar3"))
        .attr("fill", "rgb(255, 255, 191)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar4"))
        .attr("fill", "rgb(171, 221, 164)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar5"))
        .attr("fill", "rgb(43, 131, 186)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar6"))
        .attr("fill", "rgb(215, 25, 28)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar7"))
        .attr("fill", "rgb(253, 174, 97)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar8"))
        .attr("fill", "rgb(255, 255, 191)").attr("stroke-width", "0");
        d3.select(document.getElementById("#svg3bar9"))
        .attr("fill", "rgb(171, 221, 164)").attr("stroke-width", "0");
        
        let elem = document.getElementById("svg2Curve1");
        elem.remove();
      }
    },
  },
};
</script>

<style>
.claim {
  font-weight: bold;
  padding-left: 0.2em;
  padding-right: 0.2em;
}

.claim {
  /* background-color: #fbb; */
  background-image: url("../pics/claim.png");
  background-size: 120%;
  background-repeat: no-repeat;
}
</style>
