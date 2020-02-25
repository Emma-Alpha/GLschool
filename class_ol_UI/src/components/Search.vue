<template>

  <div>
    <Head></Head>
    <div class="search_container" _r-cid="1" _r-component="p-index">

      <div class="search_tools">
        <div class="mod_filter" r-notemplate="true">


          <div class="filter_item current">
            <a href="javascript:;" data-key="sort" data-val="0" _stat="pages_index:sort_sort_相关">相关</a>
          </div>

          <div class="filter_item">
            <a href="javascript:;" data-key="sort" data-val="1" _stat="pages_index:sort_sort_最新">最新</a>
          </div>

          <div class="filter_item">
            <a href="javascript:;" data-key="sort" data-val="2" _stat="pages_index:sort_sort_最热">最热</a>
          </div>


          <div class="filter_item filter_item_more"><a href="javascript:;" _stat="pages_index:sort_more"><span
            class="icon_text">筛选</span><i class="icon_sm icon_down_sm">
            <svg class="svg_icon svg_icon_down_sm" viewBox="0 0 16 16">
              <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_down_sm"></use>
            </svg>
          </i>
            <i class="icon_sm icon_up_sm">
              <svg class="svg_icon svg_icon_up_sm" viewBox="0 0 16 16">
                <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_up_sm"></use>
              </svg>
            </i></a></div>


          <div class="filter_item filter_item_back none">
            <a href="javascript:;" _stat="pages_index:sort_back">
              <i class="icon_sm icon_down_sm">
                <svg class="svg_icon svg_icon_down_sm" viewBox="0 0 16 16">
                  <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_down_sm"></use>
                </svg>
              </i>
              <span class="icon_text">返回</span></a>
          </div>

        </div>

      </div>

      <div class="wrapper">

        <div class="wrapper_main">


          <div class="result_item result_item_h _quickopen" v-for="data in data_list">
            <a href="https://v.qq.com/x/page/n0852kmvln0.html" class="figure result_figure" target="_blank"
               data-paytype="0" _stat="video:poster_h" data-qpvid="n0852kmvln0" data-qpcid="">
              <img class="figure_pic" :src="'http://106.14.202.117:8888/'+data.video_img"
                   >

              <span class="figure_caption"><span class="figure_info">0.0.0</span></span>

              <span class="mark_quickplay"></span></a>
            <h2 class="result_title"><a href="https://v.qq.com/x/page/n0852kmvln0.html" target="_blank"
                                        _stat="video:poster_h_title"><em class="hl">{{data.title}}</em></a></h2>
            <div class="result_info">
              <div class="info_line">

                <div class="info_item info_item_odd">
                  <span class="label">时　间：</span>
                  <span class="content">上传时间</span>
                </div>

                <!--  -->

              </div>


              <div class="info_line">


              </div>


            </div>
          </div>



        </div>
        <div class="wrapper_side">




          <div class="mod_box mod_box_hotlist" id="hotlist" r-notemplate="true" _r-cid="6" _r-component="hot-board">
            <div class="mod_hd">
              <div class="mod_title">
                <h3 class="title">热搜榜单</h3>
                <div class="bg_rank_ball"></div>
                <div class="mod_tools">
                    <i class="icon_sm icon_right_sm">
                      <svg class="svg_icon svg_icon_right_sm" viewBox="0 0 16 16">
                        <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_right_sm">
                        </use>
                      </svg>
                    </i>
                </div>
              </div>
            </div>
            <div class="mod_bd">
              <div class="mod_hotlist_nav">
                <div class="mod_nav_list">
                  <div :class="chs==0?'list_item  current':'list_item'" data-id="0" @click="chs=0">总榜</div>
                  <div class="list_item" data-id="2" v-for="course in coursecategory_list">{{course.type_name}}</div>
                  <div class="more_btn">
                    <button class="prev_btn btn disabled"><!-- 置灰  disabled -->
                      <i class="icon_sm icon_left_sm">
                        <svg class="svg_icon svg_icon_left_sm" viewBox="0 0 16 16">
                          <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_left_sm">
                          </use>
                        </svg>
                      </i>
                    </button>
                    <button class="next_btn btn">
                      <i class="icon_sm icon_right_sm">
                        <svg class="svg_icon svg_icon_right_sm" viewBox="0 0 16 16">
                          <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_right_sm">
                          </use>
                        </svg>
                      </i>
                    </button>
                  </div>
                </div>
              </div>
              <div class="mod_hotlist ">
                <ol class="hotlist ">

                  <li class="item item_1">
                    <a href="//v.qq.com/x/search/?q=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86&amp;stag=101"
                       _oldstat="action=3&amp;qid=ZAZVJ%5FzgMJSMMqUW0nPq1wjs4vMmFHclf0WsrVtksUsHAD1DnWyagQ&amp;platform=10201&amp;uin=0&amp;guid=21bc7956%2Dde75%2D4b9e%2Db527%2De53cbedca7f2&amp;ival=0&amp;ival1=0&amp;ival2=8&amp;ival4=1&amp;ival5=514&amp;ival7=57&amp;ival8=0&amp;ival9=0&amp;sval=self&amp;sval2=%E5%B9%BF%E4%B8%9C%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2&amp;sval8=edit%3D0%26cur%3D0%26datasource%3D0%26data%5Ftype%3D0%26video%5Ftype%3D0%26pay%5Ftype%3D0%26input%5Fpara%3Dtabid%253D0%2526sort%253D0%2526cur%253D0%2526num%253D15%2526pubtime%253D0%2526duration%253D0%2526plat%253D2%2526pver%253D0%2526comment%253D1%26guidSuffix%3D1542731064%26&amp;sval7=smartbox%5Fabtest%3D1073741824%26hit%5Fcate%3D32%26abtest%5Ffrom%5Flogic%3D104%255F108%255F124%255F127%255F132%255F142%255F143%255F151%255F157%255F159%255F160%255F162%255F175%255F176%255F182%255F195%255F198%255F20%255F203%255F211%255F239%255F245%255F257%255F262%255F273%255F286%255F296%255F306%255F320%255F330%255F331%255F337%255F343%255F358%255F374%255F394%255F4%255F41%255F45%255F49%255F50%255F66%255F69%255F72%255F75%255F76%255F77%255F80%255F83%255F85%255F86%255F87%255F89%255F90%255F92%26query%5Ffrom%3D102%26&amp;cacheKeyNoPage=9151686470643831908%5F0%5F0%5F2%5F0%5F1%5F0%5F6%5F2784796696961998133%5FZAZVJ%5FzgMJSMMqUW0nPq1wjs4vMmFHclf0WsrVtksUsHAD1DnWyagQ">
                      <span class="num">1</span>
                      <span class="name">Python</span>

                      <i class="icon_hold">စ</i>
                    </a>
                  </li>



                </ol>
              </div>
            </div>
          </div>

          <!-- 广告模块 -->
          <!-- <div class="side_ad">
            <div class="ad_inner" r-notemplate="true">
              <img src="//tacs_v1.oa.com/img.php?260x162">
            </div>
          </div> -->

        </div>
        <div class="clear"></div>

      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
  import Head from "./common/Head";
  import Footer from "./common/Footer";
    export default {
        name: "Search",
        components:{
            Head,
            Footer
        },
        data(){
            return{
              title:'',
                data_list:[],
                coursecategory_list:[],
            }
        },
        created(){
          this.get_title();
          this.get_coursecategory()
        },
        methods:{
            get_coursecategory() {
                this.$axios.get(`${this.$settings.Host}/video/video_type/`, {}).then(response => {
                    this.coursecategory_list = response.data
                    console.log(this.coursecategory_list)
                }).catch(error => {
                    console.log(error.response);
                })
            },

            get_title(){
                this.title = this.$route.query.title;
                this.$axios.get(`${this.$settings.Host}/video/search/?title=`+this.title).then(response=>{
                    this.data_list = response.data;
                    console.log(this.data_list)
                }).catch(error=>{
                    console.log(error=>{
                        console.log(error.response)
                    })
                })

            }
        },
    }
</script>

<style src="../../static/css/search.css"></style>

<style scoped>
.mod_quick .quick_link {
    display: block;
    z-index: 11;
    position: relative;
    width: 36px;
    height: 26px;
    padding: 0;
    color: #999;
    text-decoration: none;
    cursor: pointer;
}

  .site_head_absolute .mod_quick .quick_link {
    /* color: #fff; */
    /* color: rgba(255,255,255,.8); */
}
</style>
