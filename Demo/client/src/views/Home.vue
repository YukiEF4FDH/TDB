<template>
  <div class="home">
    <el-container>
    <el-header style="min-height: 370px; margin-bottom: 1%;">
      <HeadOfDoc />
    </el-header>
    <el-main>
      <BodyOfDoc />
    </el-main>
  </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import HeadOfDoc from "@/components/HeadOfDoc.vue";
import BodyOfDoc from "@/components/BodyOfDoc.vue";
import { ElContainer,ElHeader, ElMain } from 'element-plus'

let vm = null;

export default {
  name: "Home",
  components: {
    HeadOfDoc,
    BodyOfDoc,
    ElContainer, ElHeader, ElMain
  },
  data() {
    return {

    };
  },
  methods: {

  },
  mounted() {
    vm = this;
  }
};
</script>

<style>
p {
    display: block;
    margin-block-start: 0px;
    margin-block-end: 0px;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
}

.el-main{
  margin-top: 3%;
}

</style>