<template>
  <div id="fa-body">
    <div>
      <p style="text-align: center;font-size: 30px; padding: 20px 0">最新教学视频</p>
    </div>
    <!--    <p style="text-align: center" id="title" class="Hiragino Sans GB">未来因你而来,广东理工学院欢迎你</p>-->
    <div id="fa">
      <el-tabs v-model="activeName" @tab-click="handleClick" id="row_Card" style="font-size: 0">
        <el-tab-pane v-for="(college,key) in college_list" :label="college.name"
                     :key="college.id"  :id="college.id" :name="'college_'+college.id">
          <el-row>
            <el-col :span="6" style="padding: 10px 10px;display:inline-block;float:None"
                    v-for="(course,key) in course_dict" :key="key" >
              <a :href="'/video/' + course.id" target="view_window">
                <el-card :body-style="{ padding: '0px'}">
                  <img :src=course.course_img class="image">
                  <div style="padding: 14px;">
                    <span style="font-size: 30px">{{course.name}}</span>
                    <div class="bottom clearfix">
                      <time class="time">{{course.brief}}</time>
                      <el-button type="text" class="button">{{course.teacher.name}}</el-button>
                    </div>
                  </div>
                </el-card>
              </a>
            </el-col>
          </el-row>
        </el-tab-pane>
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
                category: 0,
                activeName: 'college_1',
                college_list: [],
                course_dict: [{
                    'college': {},
                    'teacher': {},
                    'name': '',
                },],
            };
        },
        watch: {
            // 每次点击不同课程时，要重新获取课程列表
            category(){
              this.get_course()
            }
        },

        created() {
            this.get_college();
            this.get_course();
        },

        methods: {

            handleClick(tab,event){
                this.category = tab.$attrs.id;
            },

            get_course() {
                let filter = {
                    college : 1
                };
                if(this.category > 0){
                    filter.college = this.category
                }
                this.$axios.get(`${this.$settings.Host}/course/`,{
                    params:filter
                }).then(response => {
                    this.course_dict = response.data
                }).catch(error => {
                    this.$alert("网络错误!", '广东理工学院')
                })
            },

            get_college() {
                this.$axios.get(`${this.$settings.Host}/course/college/`).then(response => {
                    this.college_list = response.data
                }).catch(error => {
                    this.$alert("网络错误！", "广东理工学院")
                })
            },
        }
    }
</script>

<style scoped>
  #fa a {
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
