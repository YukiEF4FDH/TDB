<template>
	<span class="claim" :claim_id="this.id" @mouseover="setHover($event)" @mouseleave="setLeave($event)">
		<slot>	</slot>
	</span>
</template>

<script>
	import * as d3 from 'd3';
	import Curve from './Curve.vue';
	
	let claim_id = 0;
	// let oldColor="";
	
	export default {
		name: 'claim',
		data() {
			return {
				id: 0,
				text: 'default'
			}
		},
		created() {
			this.id = claim_id++; // data.id更新
		
			const _default = this.$slots.default();
			if (_default && _default.length > 0)
				this.text = _default[0].children; // data.text更新
		},
		methods: {
			setHover: function () {
				// oldColor = d3.select(document.getElementById("F1A_5_1a")).attr("fill");
				// console.log(d3.select(document.getElementById("F1A_5_1a"))._groups[0][0].attributes);
				// d3.select(document.getElementById("F1A_5_1a")).attr("fill", "yellow");

				d3.select("#svg1")
        .selectAll("rect")
        .each(function (d) {
            d3.select("#" + this.id).attr("fill", "#cacaca");
        });

				d3.select(document.getElementById("F1A_1_1a")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_2_1a")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_3_1a")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_4_1a")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_1_1b")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_2_1b")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_3_1b")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");
				d3.select(document.getElementById("F1A_4_1b")).attr("fill", "#fbb").attr("stroke", "#d39d9c").attr("stroke-width","5");

				d3.select('#Sec3').append("svg").attr("id","svgCurve3").text(function(d) { return d; });

				Curve.methods.drawCurve2();

				// d3.select(document.getElementById("F1A_1_1b")).attr("fill", "#cae6b6").attr("stroke", "#aabe9b").attr("stroke-width","5");

			},
			setLeave: function () {
				d3.select(document.getElementById("F1A_1_1a")).attr("fill", "rgb(215, 25, 28)");
				d3.select(document.getElementById("F1A_2_1a")).attr("fill", "rgb(215, 25, 28)");
				d3.select(document.getElementById("F1A_3_1a")).attr("fill", "rgb(215, 25, 28)");
				d3.select(document.getElementById("F1A_4_1a")).attr("fill", "rgb(215, 25, 28)");

				d3.select(document.getElementById("F1A_1_1a")).attr("stroke-width","0");
				d3.select(document.getElementById("F1A_2_1a")).attr("stroke-width","0");
				d3.select(document.getElementById("F1A_3_1a")).attr("stroke-width","0");
				d3.select(document.getElementById("F1A_4_1a")).attr("stroke-width","0");


				var elem = document. getElementById("svgCurve3"); 
				elem. remove();
			},
		}
	}
</script>

<style>
	.claim {
		font-weight: bold;
		padding-left: .2em;
		padding-right: .2em;
	}
	
	.claim {
		/* background-color: #fbb; */
		background-image: url("../pics/claim.png");
		background-size: 120%;
		background-repeat: no-repeat;
	}
</style>
