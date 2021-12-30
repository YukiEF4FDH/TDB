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
import Sec1Chart0 from "@/components/Sec1/Sec1Chart0.vue";

// let reference_id = 0;
// let oldColor="";
let reference_id = 0;

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
      // oldColor = d3.select(document.getElementById("F1A_5_1a")).attr("fill");
      // console.log(d3.select(document.getElementById("F1A_5_1a"))._groups[0][0].attributes);
      d3.select("#svg1")
        .selectAll("rect")
        .each(function (d) {
          if (this.id != "F1A_1_1a" && this.id != "F1A_1_1b") {
            d3.select("#" + this.id).attr("fill", "#cacaca");
          }
        });

      d3.select(document.getElementById("F1A_1_1a"))
        .attr("fill", "#cae6b6")
        .attr("stroke", "#aabe9b")
        .attr("stroke-width", "5");
      d3.select(document.getElementById("F1A_1_1b"))
        .attr("fill", "#cae6b6")
        .attr("stroke", "#aabe9b")
        .attr("stroke-width", "5");

      // d3.select("#svg1").append("text").enter().attr("x","0").attr("y","0");

      d3.select("#Sec1")
        .append("svg")
        .attr("id", "svgCurve2")
        .text(function (d) {
          return d;
        });

      Curve.methods.drawCurve();

      console.log(this.id);
    },
    setLeave: function () {
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

      d3.select(document.getElementById("F1A_1_1a")).attr("stroke-width", "0");
      d3.select(document.getElementById("F1A_1_1b")).attr("stroke-width", "0");

      var elem = document.getElementById("svgCurve2");
      elem.remove();
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
  /* background-image: url("../pics/ref.png"); */
  background-image: url("../pics/ref.png");

  background-size: 120%;
  background-repeat: no-repeat;
}
</style>
