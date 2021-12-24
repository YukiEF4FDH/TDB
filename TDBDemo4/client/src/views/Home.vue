<template>
  <div class="home">
    <HeadOfDoc />
    <BodyOfDoc />
  </div>
</template>

<script>
// @ is an alias to /src
import HeadOfDoc from "@/components/HeadOfDoc.vue";
import BodyOfDoc from "@/components/BodyOfDoc.vue";

export default {
  name: "Home",
  components: {
    HeadOfDoc,
    BodyOfDoc,
  },
};
</script>