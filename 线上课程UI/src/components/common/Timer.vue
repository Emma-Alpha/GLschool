<template>

  <div>
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div>
      <p style="text-align: center;font-size: 30px; padding: 20px 0">最新热门视频</p>
    </div>
    <div id="yangshi">
      <el-card class="box-card" style="width: 900px;height: 350px" :body-style="{padding : '0px'}">
        <div style="width: 450px;height:350px;display: inline-block;float: left">
          <img style="width: 100%" :key="key" v-for="(img,key) in course_list" :src=img.course_img
               v-if="image_index === key && img.is_host" >
          <!--        </el-card>-->
        </div>
        <div style="width: 435px;display: inline-block;float: left">
          <div class="row pre-scrollable">
            <ul class="nav nav-pills  nav-stacked">
              <li v-for="(item,key) in course_list" role="presentation" :key="key"
                  @mouseover=show_image(key) style="margin-left: 15px;background: #F0FFFF" v-if="item.is_host"
                  :class="key===1?'yangshi':''"><a
                :href="'course/detail/'+item.id">{{item.name}}</a>
              </li>
            </ul>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Timer",
        data() {
            return {
                course_list: [],
                image_index: 1,
            }
        },
        created() {
            this.host_image();
        },
        methods: {
            host_image() {
                this.$axios.get(`${this.$settings.Host}/course/`).then(response => {
                    this.course_list = response.data.results
                }).catch(error => {
                    // this.$alert(error.response)
                    this.$message.error("网络错误！")
                })
            },
            show_image(id) {
                this.image_index = id;
            },
        }
    }
</script>

<style scoped>


  #yangshi {
    left: 20%;
    width: 900px;
    height: 350px;
    text-align: center;
    margin: 0 200px;
  }

  .nav-pills > li.active > a, .nav-pills > li.active > a:hover, .nav-pills > li.active > a:focus {
    background: #48D1CC;
  }

  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
  }

  img {
    width: 100%;
  }

  #time_card {

  }
</style>
