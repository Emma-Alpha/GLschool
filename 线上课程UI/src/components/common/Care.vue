<template>
  <div id="fa-body">
    <div>
      <p style="text-align: center;font-size: 30px; padding: 20px 0">最新教学视频</p>
    </div>
    <!--    <p style="text-align: center" id="title" class="Hiragino Sans GB">未来因你而来,广东理工学院欢迎你</p>-->
    <div id="fa">
      <el-tabs v-model="activeName" @tab-click="handleClick" id="row_Card" style="font-size: 0">
        <el-tab-pane label="信息技术学院" name="first">
          <el-row>
            <el-col :span="6" style="padding: 10px 10px;display:inline-block;float:None" v-for="item,key in img_list" v-bind:key="item.id">
              <a :href="'/video/' + key" target="view_window">
                <el-card :body-style="{ padding: '0px'}">
                  <img :src=item.img_url class="image">
                  <div style="padding: 14px;">
                    <span style="font-size: 30px">{{item.title}}</span>
                    <div class="bottom clearfix">
                      <time class="time">{{item.time_title}}</time>
                      <el-button type="text" class="button">操作按钮</el-button>
                    </div>
                  </div>
                </el-card>
              </a>
            </el-col>
          </el-row>
          <div class="block">
            <span class="demonstration">大于 7 页时的效果</span>
          </div>
        </el-tab-pane>
        <el-tab-pane label="经济管理学院" name=""></el-tab-pane>
        <el-tab-pane label="外国语学院" name=""></el-tab-pane>
        <el-tab-pane label="电气与电子工程学院" name="fourth"></el-tab-pane>
        <el-tab-pane label="会计学院" name=""></el-tab-pane>
        <el-tab-pane label="建设学院" name=""></el-tab-pane>
        <el-tab-pane label="工业自动化系" name=""></el-tab-pane>
        <el-tab-pane label="汽车工程系" name=""></el-tab-pane>
        <el-tab-pane label="艺术系" name=""></el-tab-pane>
        <el-tab-pane label="体育系" name=""></el-tab-pane>
        <el-tab-pane label="国际商学院" name=""></el-tab-pane>
        <el-tab-pane label="产业学院" name=""></el-tab-pane>
      </el-tabs>
    </div>
    <div style="width:1200px;margin: 0 40px">
      <img src="/static/image/推荐.jpg" alt="">
    </div>
  </div>

</template>

<script>
    export default {
        name: "Care",
        data() {
            return {
                activeName: 'first',
                img_list: [
                    {'img_url': "/static/image/jiji.JPG", 'title': "java大神", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/ww.jpeg", 'title': "可爱文文在教学", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/tz.jpeg", 'title': "团长开团", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/cq.JPG", 'title': "性感啊钦", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/qq.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/jj2.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/yy.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                    {'img_url': "/static/image/laoyu.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                    // {'img_url': "/static/image/table.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                    // {'img_url': "/static/image/table.JPG", 'title': "你楸啥", 'time_title': "在线性感教学"},
                ]
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            }
        }
    }
</script>

<style scoped>
    #fa a{
    text-decoration: none;
  }

  .el-col {
    display: inline-block;
    /*-webkit-box-sizing: border-box;*/
    box-sizing: border-box;
  }

  #title {
    color: #999999;
  }


  #fa-body {
    position: relative;
  }

  #fa {
    position: relative;
    height: 700px;
  }

  #row_Card {
    position: absolute;
    left: 5%;
    width: 1150px;
    height: 120px;
  }


  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .banner_nav {
    background-color: red;
  }
</style>
