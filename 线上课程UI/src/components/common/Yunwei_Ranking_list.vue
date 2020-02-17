<template>
  <div class="mod_row_box" id="new_vs_hot_movie"
       data-istyle="8" data-context="2" __expose="new_vs_hot_movie">

    <div class="mod_bd cf _quickopen _quickopen_duration">

      <div class="mod_column_main">
        <div class="mod_hd mod_column_hd">

          <h2 class="mod_title">

            <a class="title_link " href="javascript:;" data-target="_blank"
               _stat="new_vs_hot_movie:通栏功能区:通栏标题"
               style="font-size: 30px;font-weight: 400;line-height:40px; color: #111">
              运维开发
            </a>

          </h2>


          <div class="mod_page_small">
            <button @click="get_page_previous(course_dict.previous)"
                    :class="course_dict.previous?'btn_prev':'btn_prev disabled'" wind-click="100"
                    _stat="new_vs_hot_movie:通栏功能区:上一页" title="上一页">
              <svg class="svg_icon svg_icon_prev" viewBox="0 0 6 10" width="6" height="10">
                <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-width="1.4"
                      stroke-linecap="round"></path>
              </svg>
            </button>
            <span class="page_num" data-info="12 18" data-count="3" data-page="1">{{danpage}}/{{Math.ceil(course_dict.count/6)}}</span>
            <button @click="get_page_next(course_dict.next)" :class="course_dict.next?'btn_next':'btn_next disabled'"
                    wind-click="100" _stat="new_vs_hot_movie:通栏功能区:下一页" title="下一页">
              <svg class="svg_icon svg_icon_next" viewBox="0 0 6 10" width="6" height="10">
                <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-width="1.4"
                      stroke-linecap="round"></path>
              </svg>
            </button>
          </div>


        </div>
        <div class="mod_column_bd">


          <div class="mod_figure
        mod_figure_v_default
        mod_figure_v_default_2row
        mod_figure_v_default
    " data-rowcount="6" data-rowlen="2">


            <div class="list_item " v-for="course in course_dict.results">


              <a :href="`/video_detail/`+course.id"
                 class="figure" tabindex="-1" data-float="3l93f6h0zkx8c2b"
                 data-floatid="2">


                <img loading="lazy" class="figure_pic" alt="" onerror="picerr(this,'v')"
                     :src="course.video_img"
                     style="visibility: visible;">

                <div class="figure_score">7.5</div>


              </a>


              <div class="figure_detail figure_detail_two_row  ">
                <a href="javascript:;" class="figure_title figure_title_two_row bold"
                   :title="course.name" _stat="new_vs_hot_movie:title:霹雳娇娃"
                   target="scene=%E9%A2%91%E9%81%93%E9%A1%B5&amp;pagename=%E7%B2%BE%E9%80%89%E9%A2%91%E9%81%93&amp;columnname=%E7%B2%BE%E9%80%89_%E7%94%B5%E5%BD%B1&amp;controlname=new_vs_hot_movie&amp;cid=3l93f6h0zkx8c2b&amp;vid=&amp;pid=&amp;datatype=1&amp;playertype=1&amp;controlidx=0&amp;columnidx=3&amp;plat_bucketid=9231007">{{course.name}}</a>

                <div class="figure_desc" :title="course.focus_content">{{course.focus_content}}</div>


              </div>


            </div>


          </div>


        </div>
      </div>
      <div class="mod_column_side">
        <div class="mod_hd mod_column_hd">
          <h2 class="mod_title">运维开发排行榜</h2>
          <div class="bg_rank_ball"></div>

        </div>


        <div class="mod_rank_list mod_rank_list_1column  ">


          <a :href="`/video_detail/`+rank.id" v-for="rank,key in rank_list" class="rank_item rank_item_1 cf" title="叶问4"
             target="scene=%E9%A2%91%E9%81%93%E9%A1%B5&amp;pagename=%E7%B2%BE%E9%80%89%E9%A2%91%E9%81%93&amp;columnname=%E7%B2%BE%E9%80%89_%E7%94%B5%E5%BD%B1&amp;controlname=new_vs_hot_movie&amp;cid=m5zzglrbt5zdv6d&amp;vid=&amp;pid=&amp;datatype=1&amp;playertype=1&amp;controlidx=0&amp;columnidx=3&amp;plat_bucketid=9231007">
            <span :class="key+1 > 3?'rank_num rank_num_4':'rank_num rank_num_1'">{{key+1}}</span>
            <span class="rank_title">{{rank.name}}</span>
            <span class="rank_desc">{{rank.focus_content}}</span>


            <span class="rank_update">{{rank.video_play}}人</span>


          </a>


        </div>


      </div>

    </div>
  </div>

</template>

<script>
    export default {
        name: "yunwei_Ranking_list",
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
                danpage: 1,
                rank_list: [],
            };
        },
        watch: {
            // 每次点击不同课程时，要重新获取课程列表
            category() {
                this.get_course()
            }
        },


        created() {
            this.get_course();
            this.ranking_list();
        },

        methods: {

            get_page_next(url) {
                this.$axios.get(url).then(response => {
                    this.course_dict = response.data;
                    this.danpage += 1;
                }).catch(error => {
                    this.$alert("网络错误!", '广东理工学院')
                })
            },
            get_page_previous(url) {
                this.$axios.get(url).then(response => {
                    this.course_dict = response.data;
                    this.danpage -= 1;
                }).catch(error => {
                    this.$alert("网络错误!", '广东理工学院')
                })
            },

            handleClick(tab, event) {
                this.category = tab.$attrs.id;
            },

            get_course() {
                this.$axios.get(`${this.$settings.Host}/video/type/`, {
                    params: {
                        fenlei: 2
                    }
                }).then(response => {
                    this.course_dict = response.data;
                    console.log("21312312", this.course_dict)
                }).catch(error => {
                    this.$alert("网络错误!", '广东理工学院')
                })
            },

            ranking_list() {
                this.$axios.get(`${this.$settings.Host}/video/num/`, {
                    params: {
                        fenlei: 2
                    }
                }).then(response => {
                    console.log(response.data)
                    this.rank_list = response.data
                }).catch(error => {
                    this.$alert("网络错误！", "广东理工学院")
                })
            }
        }
    }
</script>

<style scoped>
  #fa a {
    text-decoration: none;
  }

  .mod_rank_list {
    padding: 12px 0;
    border-radius: 4px;
    background-color: #f8f8f8;
  }

  .mod_rank_list {
    padding: 12px 0;
    border-radius: 4px;
    background-color: #f8f8f8;
  }

  .mod_rank_list .rank_item {
    display: block;
    position: relative;
    padding: 21px 30px 10px 35px;
  }

  .mod_rank_list .rank_item:last-child {
    padding-bottom: 23px
  }

  .mod_rank_list .rank_num {
    position: absolute;
    left: 30px;
    margin-top: -4px;
    color: #666;
    font-size: 26px;
    line-height: 30px
  }

  .mod_rank_list .rank_num_1, .mod_rank_list .rank_num_2, .mod_rank_list .rank_num_3 {
    color: #ff183e;
    font-size: 28px
  }

  .mod_rank_list .rank_num_10 {
    left: 22px
  }

  .mod_rank_list .figure_pic {
    display: none
  }

  .mod_rank_list .rank_desc, .mod_rank_list .rank_title {
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
  }

  .mod_rank_list .rank_title {
    margin-right: 80px;
    color: #111;
    font-size: 18px;
    font-weight: 700;
    line-height: 24px
  }

  .mod_rank_list .rank_title:hover {
    color: #ff5c38
  }

  .mod_rank_list .rank_desc {
    color: #999;
    font-size: 13px
  }

  .mod_rank_list .rank_update {
    position: absolute;
    top: 20px;
    right: 20px;
    color: #999;
    font-size: 13px;
    white-space: nowrap
  }

  .mod_rank_list .none {
    display: none
  }

  @supports (-webkit-background-clip:text) {
    .mod_rank_list .rank_num_1, .mod_rank_list .rank_num_2, .mod_rank_list .rank_num_3 {
      -webkit-text-fill-color: transparent;
      -webkit-background-clip: text;
      background-image: linear-gradient(180deg, #ffb821 0, #ff5c38 45%, #ff1459)
    }
  }

  .mod_rank_list_1column .rank_item {
    margin: 0 20px;
    padding: 20px 30px 18px 40px;
    border-top: 1px solid #eee;
  }

  .mod_rank_list_1column .rank_item:first-child {
    border-top: none;
  }

  .mod_rank_list_1column .rank_num {
    left: 4px
  }

  .mod_rank_list_1column .rank_update {
    right: 0
  }

  .mod_rank_list_1column .rank_item_10, .mod_rank_list_1column .rank_item_9 {
    display: none
  }

  .mod_rank_list_2column {
    -webkit-column-count: 2;
    -webkit-column-gap: 0;
    padding: 5px 0 0 5px;
    column-gap: 0;
    column-count: 2
  }

  .mod_rank_list_2column .rank_item {
    -webkit-column-break-inside: avoid;
    padding: 17px 0 5px 45px
  }

  .mod_rank_list_2column .rank_num {
    left: 16px
  }

  .mod_rank_list_2column .rank_num_10 {
    left: 12px
  }

  .mod_rank_list_2column .rank_title {
    margin-right: 20px;
    font-size: 15px
  }

  .mod_rank_list_2column .rank_desc {
    display: none
  }

  .mod_rank_list_2column .rank_update {
    display: block;
    position: static
  }

  .mod_rank_list_2column_v {
    padding-top: 12px
  }

  .mod_rank_list_2column_v .rank_item {
    padding-bottom: 15px
  }

  .mod_rank_list_2column_v .rank_item_10, .mod_rank_list_2column_v .rank_item_9 {
    display: none
  }

  .mod_listings_title {
    position: relative;
    padding-top: 10px;
    overflow: hidden;
    font-size: 0;
    letter-spacing: -3px;
    white-space: nowrap
  }

  .mod_listings_title:before {
    z-index: -2;
    position: absolute;
    top: 8px;
    left: 0;
    width: 100%;
    height: 2px;
    background: #f8f8f8;
    content: ""
  }

  .mod_listings_title .title_item {
    *zoom: 1;
    display: inline-block;
    *display: inline;
    position: relative;
    width: 198px;
    margin-right: 18px;
    margin-bottom: 20px;
    padding-top: 26px;
    letter-spacing: 0;
    line-height: 20px;
    text-align: center;
    vertical-align: top
  }

  .mod_listings_title .title_item .title {
    display: inline-block;
    color: #111;
    font-size: 15px;
    font-weight: 700
  }

  .mod_listings_title .title_item .desc {
    display: block;
    margin-top: -1px;
    color: #999;
    font-size: 13px
  }

  .mod_listings_title .icon_aspect {
    display: inline-block;
    position: relative;
    right: -62px;
    width: 56px;
    height: 28px;
    margin-top: -11px;
    margin-left: -56px;
    overflow: hidden;
    border-radius: 16px 16px 16px 0;
    background: #ff5c38;
    background: linear-gradient(90deg, #ffb821 0, #ff5c38 45%, #ff1459);
    background-color: #ff183e;
    color: #fff;
    font-size: 13px;
    line-height: 29px;
    vertical-align: top
  }

  .mod_listings_title .dot {
    position: absolute;
    top: -6px;
    left: 50%;
    width: 10px;
    height: 10px;
    margin-left: -5px;
    border-radius: 100%;
    background: #d7d7d7
  }

  .mod_listings_title .dot:after {
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    position: absolute;
    bottom: -1px;
    left: 2px;
    width: 6px;
    height: 6px;
    transform: rotate(45deg);
    background-color: inherit;
    content: ""
  }

  .mod_listings_title .dot:before {
    z-index: -1;
    position: absolute;
    right: -4px;
    left: -4px;
    height: 10px;
    background-color: #fff;
    content: ""
  }

  .mod_listings_title .dot_1 {
    background: #ff183e
  }

  .mod_listings_title .dot_2 {
    background: #ff5c38
  }

  .mod_listings_title .dot_3 {
    background: #ffb821
  }
</style>
