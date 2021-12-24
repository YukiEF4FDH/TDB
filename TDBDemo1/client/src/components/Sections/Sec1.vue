<template>
	<div id="Sec1">
			<Sec1Text0/>
			<Sec1Chart0/>
	</div>
</template>

<script>
	import Sec1Text0 from '@/components/Sections/Sec1/Sec1Text0.vue'
	import Sec1Chart0 from '@/components/Sections/Sec1/Sec1Chart0.vue'

	export default {
		name: 'Sec1',
		components: {
			Sec1Text0,
			Sec1Chart0
		},
	}
</script>
