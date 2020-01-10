<template>
  <div class="block">
    <el-carousel height="318px">
      <el-carousel-item :key="key" v-for="(image_url,key) in banner_list">
<!--        <a v-if=item.is_http ><img :src=item.images alt=""></a>-->
        <a :href="image_url.link" v-if="image_url.is_http"><img :src=image_url.image alt=""></a>
        <router-link :to="image_url.link" v-else><img :src=image_url.image alt=""></router-link>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
    export default {
        name: "banner",
        data(){
            return{
                banner_list:[]
            }
        },
        created(){
            this.get_banner()
        },
        methods:{
            get_banner(){
                //轮播风景图
                // es6提供了一种允许换行的字符串，叫文档字符串，可以允许在字段中换行并输出js变量
                this.$axios.get(`${this.$settings.Host}/banner/`).then(response=>{
                    this.banner_list = response.data
                }).catch(error=>{
                    this.$alert("获取轮播图失败",'广东理工学院')
                })
            }
        }
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
