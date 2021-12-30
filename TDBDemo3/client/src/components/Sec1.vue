<template>
	<div id="Sec1">
		<!-- <svg id="svgSec1"> -->
			<Sec1Text0/>
			<Sec1Chart0/>
			<Sec1Chart1/>
			<Sec1Chart2/>
		<!-- </svg> -->
	</div>
</template>

<script>
	import Sec1Text0 from '@/components/Sec1/Sec1Text0.vue'
	import Sec1Chart0 from '@/components/Sec1/Sec1Chart0.vue'
	import Sec1Chart1 from '@/components/Sec1/Sec1Chart1.vue'
	import Sec1Chart2 from '@/components/Sec1/Sec1Chart2.vue'

	export default {
		name: 'Sec1',
		data() {},
		components: {
			Sec1Text0,
			Sec1Chart0,
			Sec1Chart1,
			Sec1Chart2,
		},
		methods: {},
	}
</script>

<style scoped>
</style>
