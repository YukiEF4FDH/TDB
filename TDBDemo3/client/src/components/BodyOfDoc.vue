<template>
  <div id="BodyOfDoc" class="body">
    <Sec1/>
		<Sec2/>
		<!-- <Sec3/> -->
    <!-- <Test2/> -->
  </div>
</template>

<script>
import Sec1  from '@/components/Sec1.vue'
import Sec2  from '@/components/Sec2.vue'
// import Sec3  from '@/components/Sec3.vue'
// import Test2 from "@/components/Test2.vue"

export default {
  name: "BodyOfDoc",
  components: {
    Sec1, Sec2, 
    // Sec3,
    // Test2
  },
};
</script>

<style>
.body {
  margin-left: 5%;
  margin-right: 5%;
}
</style>
