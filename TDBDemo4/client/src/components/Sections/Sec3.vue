<template>
	<div id="Sec3">
		<Sec3Text0/>
        <Sec3Chart0/>
	</div>
</template>

<script>
	import Sec3Text0 from '@/components/Sections/Sec3/Sec3Text0.vue'
	import Sec3Chart0 from '@/components/Sections/Sec3/Sec3Chart0.vue'

	export default {
		name: 'Sec3',
		components: {
			Sec3Text0,
            Sec3Chart0
		},
	}
</script>