<template>

  <div>
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div>
      <p style="text-align: center;font-size: 30px; padding: 20px 0">最新热门视频</p>
    </div>
    <div id="yangshi">
      <el-card class="box-card" style="width: 900px;height: 350px" :body-style="{padding : '0px'}">
        <div style="width: 450px;height:350px;display: inline-block;float: left">
          <!--        <el-card class="box-card" style="width: 400px;height:350px;display: inline-block;float: left" :body-style="{padding:'0px'}">-->
          <img style="width: 100%" v-for="(img,key) in img_list" :src=img.img_url alt=""
               :style="index==key?'display:Block':'display:None'">
          <!--        </el-card>-->
        </div>
        <div style="width: 435px;display: inline-block;float: left">
          <div class="row pre-scrollable">
            <ul class="nav nav-pills  nav-stacked">
              <li v-for="(item , key) in zhibo_list" role="presentation" :class="index==key?'active':''"
                  @mouseover=add_index(key) style="margin-left: 15px;background: #F0FFFF"><a href.pervent="#">{{item.title}}</a></li>
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
                "index": 0,
                "zhibo_list": [
                    {"title": "HTML"},
                    {"title": "JS"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                    {"title": "MySQL"},
                ],
                "img_list": [
                    {"img_url": "/static/image/banner3.png"},
                    {"img_url": "/static/image/banner1.png"},
                    {"img_url": "/static/image/qq-个人.jpeg"},
                    {"img_url": "/static/image/Helloworld.jpg"},
                    {"img_url": "/static/image/强强.JPG"},
                    {"img_url": "/static/image/余余.JPG"},
                ]
            }
        },
        methods: {
            add_index(x) {
                this.index = x
            }
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
  .nav-pills > li.active > a, .nav-pills > li.active > a:hover, .nav-pills > li.active > a:focus{
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
