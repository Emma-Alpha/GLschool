<template>
  <div class="block">
    <el-carousel height="318px">
      <el-carousel-item>
        <img src="/static/image/fj_1.jpg" alt="">
      </el-carousel-item>
      <el-carousel-item>
        <img src="/static/image/fj_2.jpg" alt="">
      </el-carousel-item>
      <el-carousel-item>
        <img src="/static/image/fj_3.jpg" alt="">
      </el-carousel-item>
      <el-carousel-item>
        <img src="/static/image/fj_4.jpg" alt="">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
    export default {
        name: "banner"
    }
</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }
  img {
    width: 100%;
  }
</style>
