<template>
	<div id="Sec2">
		<Sec2Text0/>
		<Sec2Chart0/>
		<Sec2Chart1/>
	</div>
</template>

<script>
	import Sec2Text0 from '@/components/Sections/Sec2/Sec2Text0.vue'
	import Sec2Chart0 from '@/components/Sections/Sec2/Sec2Chart0.vue'
	import Sec2Chart1 from '@/components/Sections/Sec2/Sec2Chart1.vue'

	export default {
		name: 'Sec2',
		components: {
			Sec2Text0,
			Sec2Chart0,Sec2Chart1,
		},
	}
</script>
