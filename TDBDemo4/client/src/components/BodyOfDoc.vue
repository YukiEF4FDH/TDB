<template>
  <div id="BodyOfDoc" class="body">
    <Sec1 />
    <Sec2 />
    <Sec3 />
  </div>
</template>

<script>
import Sec1 from "@/components/Sections/Sec1.vue";
import Sec2 from "@/components/Sections/Sec2.vue";
import Sec3 from "@/components/Sections/Sec3.vue";

export default {
  name: "BodyOfDoc",
  components: {
    Sec1,
    Sec2,
    Sec3,
  },
};
</script>

<style>
.body {
  margin-left: 5%;
  margin-right: 5%;
}
</style>
