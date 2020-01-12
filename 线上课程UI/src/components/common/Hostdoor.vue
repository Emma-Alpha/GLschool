<template>
  <div class="mod_row_box" _wind="columnname=精选_热点短视频&amp;controlname=multi_feed_V" id="multi_feed_V" data-istyle="48"
       data-context="2" __expose="multi_feed_V">

    <div class="mod_hd">


      <h2 class="mod_title">

        <a class="title_link " href=" https://v.qq.com/channel/feeds_hotspot" data-target="_blank"
           _stat="multi_feed_V:通栏功能区:通栏标题">
          热点短视频
        </a>

      </h2>


      <div class="mod_title_tabs ">
        <button
                :class = "tis===-1?'tab_item tab_item_0 current': 'tab_item tab_item_0 '"
                data-type="为你推荐" data-content="10" data-seq="1"
                @mouseover="tis=-1"
                _stat="multi_feed_V:通栏功能区:通栏标题tab:推荐" wind-click="500">为你推荐
        </button>

        <button v-for="(i ,key) in coursecategory_list" :key="key"
                :class = "tis===key?'tab_item tab_item_ current':'tab_item tab_item_'"
                :data-type=i.name data-content="10" data-seq="1"
                _stat="multi_feed_V:通栏功能区:通栏标题tab:吃鸡" wind-click="500"
                @mouseover="tis=key"
        >{{i.name}}
        </button>


      </div>


      <div class="mod_page_small">
        <button class="btn_prev disabled" wind-click="100" _stat="multi_feed_V:通栏功能区:上一页" title="上一页">
          <svg class="svg_icon svg_icon_prev" viewBox="0 0 6 10" width="6" height="10">
            <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-width="1.4"
                  stroke-linecap="round"></path>
          </svg>
        </button>
        <span class="page_num" data-info="10 9" data-count="2" data-page="1">1/2</span>
        <button class="btn_next" wind-click="100" _stat="multi_feed_V:通栏功能区:下一页" title="下一页">
          <svg class="svg_icon svg_icon_next" viewBox="0 0 6 10" width="6" height="10">
            <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-width="1.4"
                  stroke-linecap="round"></path>
          </svg>
        </button>
      </div>


    </div>

    <div class="mod_bd cf ">

      <div class="mod_figure_1fp2r ">


        <div class="mod_focus_player" data-multi="_multi_feed_V_data">

          <div class="fp_player_title"><a class="title_link" href="https://v.qq.com/x/page/s0871ve1xb7.html"
                                          data-target="_blank">《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！</a></div>
          <video-player class="video-player vjs-custom-skin"
                        style="margin-top: 32px"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions"
                        @play="onPlayerPlay($event)"
                        @pause="onPlayerPause($event)"
          >
          </video-player>

          <div class="fp_playlist __playlist" id="mod_player_multi_feed_V_tab">
            <div class="fp_playlist_inner">


              <a href="https://v.qq.com/x/page/s0871ve1xb7.html" data-vid="s0871ve1xb7"
                 class="item item_0 item_s0871ve1xb7  current" _stat="multi_feed_V:播放列表:《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！"
                 data-url="https://v.qq.com/x/page/s0871ve1xb7.html"><span class="title"
                                                                           title="《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！">《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！</span><span
                class="desc"></span></a>


              <a href="https://v.qq.com/x/page/j0856j6wrju.html" data-vid="j0856j6wrju"
                 class="item item_1 item_j0856j6wrju " _stat="multi_feed_V:播放列表:盘点正午十部好剧《都挺好》《琅琊榜》全提名，但第一却是它！"
                 data-url="https://v.qq.com/x/page/j0856j6wrju.html"><span class="title"
                                                                           title="盘点正午十部好剧《都挺好》《琅琊榜》全提名，但第一却是它！">盘点正午十部好剧《都挺好》《琅琊榜》全提名，但第一却是它！</span><span
                class="desc"></span></a>


            </div>
            <div class="fp_switch">
              <svg class="svg_icon svg_icon_switch" viewBox="0 0 8 13" width="8" height="13">
                <path class="svg_path_prev" d="M1.5 6.5L7 12M1.5 6.5L7 1" fill="none" stroke="currentColor"
                      stroke-width="2" stroke-linecap="round"></path>
                <path class="svg_path_next" d="M6.5 6.5L1 1M6.5 6.5L1 12" fill="none" stroke="currentColor"
                      stroke-width="2" stroke-linecap="round"></path>
              </svg>
            </div>
          </div>

          <svg class="svg_sprite" width="1" height="1">
            <symbol id="svg_icon_preview" viewBox="0 0 17 15">
              <path
                d="M4 10v2H2c-1.1 0-2-.9-2-2V2C0 .9.9 0 2 0h9c1.1 0 2 .9 2 2v4h-2V2H2v8h2zM11 15c-1.6 0-3.3-.8-5.1-2.5-.8-.8-.8-2-.1-2.8l.1-.1C7.7 7.8 9.4 7 11 7c1.6 0 3.3.9 4.9 2.6.7.8.7 1.9 0 2.7-1.6 1.8-3.3 2.7-4.9 2.7zm0-2c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z"
                fill="currentcolor"></path>
              <circle cx="11" cy="11" r="1" fill="currentcolor"></circle>
            </symbol>
          </svg>

        </div>


        <div class="figure_2row">
          <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default" data-rowcount="5"
               data-rowlen="2">
            <div class="list_item active">


              <a href="https://v.qq.com/x/page/s0871ve1xb7.html"
                 target="scene=%E9%A2%91%E9%81%93%E9%A1%B5&amp;pagename=%E7%B2%BE%E9%80%89%E9%A2%91%E9%81%93&amp;columnname=%E7%B2%BE%E9%80%89_%E7%83%AD%E7%82%B9%E7%9F%AD%E8%A7%86%E9%A2%91&amp;controlname=multi_feed_V&amp;cid=&amp;vid=s0871ve1xb7&amp;pid=&amp;datatype=1&amp;playertype=1&amp;controlidx=0&amp;columnidx=2&amp;plat_bucketid=9231007"
                 class="figure" tabindex="-1" _stat="multi_feed_V:img:undefined" data-float="s0871ve1xb7"
                 data-quickopen="true">


                <img loading="lazy" class="figure_pic" alt="《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！" onerror="picerr(this,'h')"
                     src="//puui.qpic.cn/qqvideo/0/s0871ve1xb7/332" style="visibility: visible;">


                <div class="figure_caption" style="padding-bottom: 19px">


                  01:48


                </div>


              </a>


              <div class="figure_detail figure_detail_two_row  figure_detail_preview">
                <a href="https://v.qq.com/x/page/s0871ve1xb7.html" class="figure_title figure_title_two_row "
                   title="《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！" _stat="multi_feed_V:title:《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！"
                   target="scene=%E9%A2%91%E9%81%93%E9%A1%B5&amp;pagename=%E7%B2%BE%E9%80%89%E9%A2%91%E9%81%93&amp;columnname=%E7%B2%BE%E9%80%89_%E7%83%AD%E7%82%B9%E7%9F%AD%E8%A7%86%E9%A2%91&amp;controlname=multi_feed_V&amp;cid=&amp;vid=s0871ve1xb7&amp;pid=&amp;datatype=1&amp;playertype=1&amp;controlidx=0&amp;columnidx=2&amp;plat_bucketid=9231007">《白发》罗云熙化身宠妹狂魔，守护张雪迎一生一世！</a>


                <div class="figure_btn_preview figure_btn_preview_s0871ve1xb7" data-vid="s0871ve1xb7">
                  <svg class="svg_icon svg_icon_preview" viewBox="0 0 17 15" width="17" height="15">
                    <use xlink:href="#svg_icon_preview"></use>
                  </svg>
                  <span class="icon_text">预览</span>
                </div>

              </div>


            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
    export default {
        name: "Hostdoor",
        data() {
            return {
                tis: -1,
                coursecategory_list: [],  // 获取课程分类信息
                course_id: 0,
                tabIndex: 2, // 当前选项卡显示的下标
                course_name: '',  // 课程名称
                course_list: [],
                lesson: 1,
                course_lesson_list: [],
                playerOptions: {
                    playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                    autoplay: true, //如果true,浏览器准备好时开始回放。
                    muted: true, // 默认情况下将会消除任何音频。
                    loop: false, // 导致视频一结束就重新开始。
                    preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                    language: 'zh-CN',
                    aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                    sources: [
                        {
                            type: "video/mp4",
                            src: "/static/video/05cacb4e02f9d9e.mp4"
                        }
                    ],
                    poster: "/static/image/banner1.svg", //你的封面地址
                    width: document.documentElement.clientWidth,
                    notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                    controlBar: {
                        timeDivider: true,
                        durationDisplay: true,
                        remainingTimeDisplay: false,
                        fullscreenToggle: true //全屏按钮
                    },
                }
            }
        },
        created() {
            this.get_coursecategory()
        },
        methods: {
            onPlayerPause(player) {
                console.log(1)

            },
            onPlayerPlay(player) {
                console.log(2)
            },
            get_coursecategory() {
                this.$axios.get(`${this.$settings.Host}/course/coursecategory`, {}).then(response => {
                    this.coursecategory_list = response.data
                }).catch(error => {
                    console.log(error.response)
                })
            },

        }
    }
</script>

<style scoped>

</style>
