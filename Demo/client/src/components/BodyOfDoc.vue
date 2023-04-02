<template>
  <div class="body-of-doc">
    <SectionBlockList />
  </div>
</template>

<script>
import SectionBlockList from "@/components/SectionBlockList.vue"

var vm = null;

export default {
  name: "BodyOfDoc",
  components: {
    SectionBlockList,
  },
  data() {
    return {
      activateTextCellIdSuf: null,
    }
  },
  methods: {

  },
  mounted() {
    vm = this;
  },
};
</script>

<style>
.body-of-doc {
  margin-left: 5%;
  margin-right: 5%;
}
</style>
