<template>
  <div>
    <Head></Head>
    <div class="site_container container_player" id="container_player">

      <div class="container_inner">
        <div class="player_container cf" r-notemplate="true" _r-cid="3" _r-component="c-player-wrapper-wide">
          <div class="mod_player_section cf">
            <video-player class="video-player vjs-custom-skin"
                        style="margin-top: 68px; height: 376.875px; width: 640px; margin-left: 15px"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions"
                        @play="onPlayerPlay($event)"
                        @pause="onPlayerPause($event)"
          >
          </video-player>
            <div class="player_container_wide_switch" _stat="videolist:on" style="">
                            <i class="icon_sm icon_left_sm">
                <svg class="svg_icon svg_icon_left_sm" viewBox="0 0 16 16" width="16" height="16">
                  <use xlink:href="#svg_icon_left_sm"></use>
                </svg>
              </i>
              <i class="icon_sm icon_right_sm">
                <svg class="svg_icon svg_icon_right_sm" viewBox="0 0 16 16" width="16" height="16">
                  <use xlink:href="#svg_icon_right_sm"></use>
                </svg>
              </i>
            </div>
          </div>
          <div class="mod_player_side" _wind="pagename=播放列表">
            <div class="player_side_hd">
              <ul class="mod_nav_tabs" style="display: none">
                <li class="nav_item current" tabindex="0"><i class="icon_sm icon_list_sm">
                  <svg class="svg_icon svg_icon_list_sm" viewBox="0 0 16 16" width="16" height="16">
                    <use xlink:href="#svg_icon_list_sm"></use>
                  </svg>
                </i>选集
                </li>
                <li class="nav_item" tabindex="0"><i class="icon_sm icon_interact_sm">
                  <svg class="svg_icon svg_icon_interact_sm" viewBox="0 0 16 16" width="16" height="16">
                    <use xlink:href="#svg_icon_interact_sm"></use>
                  </svg>
                </i>互动
                </li>
              </ul>

              <div class="player_helper _player_helper" style="" tabindex="0">
                <span class="btn_helper">?</span>
              </div>

            </div>
            <div class="player_side_bd">

              <div class="panel_body panel_body_1" _r-cid="10" _r-component="c-video-list">
                <div class="scroll_top vip_show" r-notemplate="true">
                  <div class="player_header player_header_simple">
                    <h2 class="player_title"><a href="/detail/m/mzc00200r2566h7.html" target="_blank"
                                                _stat="videolist:title">{{info.name}}</a></h2>
                    <a href="javascript:" _stat="videolist:followclick" class="btn_collect" title="收藏">
                      <i class="icon icon_collect">
                        <svg class="svg_icon svg_icon_collect" viewBox="0 0 20 20" width="20" height="20">
                          <use xlink:href="#svg_icon_collect"></use>
                        </svg>
                      </i>
                      <i class="icon icon_collected">
                        <svg class="svg_icon svg_icon_collected" viewBox="0 0 20 20" width="20" height="20">
                          <use xlink:href="#svg_icon_collected"></use>
                        </svg>
                      </i>
                    </a>
                  </div>
                </div>

                <div class="scroll_wrap" id="video_scroll_wrap" data-coverchd="true">
                  <div class="player_hint"></div>
                  <div id="mod_follow_act">
                    <div class="hint"></div>
                  </div>


                  <svg class="svg_sprite" display="none" version="1.1" xmlns="http://www.w3.org/2000/svg"
                       r-notemplate="true">
                    <symbol id="svg_icon_vip_flat_sm" viewBox="0 0 16 16">
                      <path
                        d="M14.746 7.105l-2.584 2.959.422 4.038-.014.012c.007.042.024.081.024.125 0 .424-.329.768-.734.768a.713.713 0 0 1-.273-.057l-.011.009-3.57-1.685-3.539 1.647-.008-.005a.695.695 0 0 1-.33.091c-.406 0-.734-.344-.734-.768 0-.032.013-.059.017-.09l-.009-.006.17-1.56c.475-.108.943-.233 1.4-.383l-.098.805 3.115-1.294 3.073 1.292-.351-3.232 2.291-2.737-.486-.085c.346-.434.667-.889.967-1.359l.942.189.006.02a.75.75 0 0 1 .571.733.77.77 0 0 1-.257.573zm-1.618-2.671c-2.169 3.982-5.932 6.722-10.238 7.351a.63.63 0 0 1-.345.073c-.385-.039-.666-.41-.628-.829a.729.729 0 0 1 .607-.669l-.003-.03c3.946-.511 7.401-3.005 9.388-6.636.127-.27.394-.444.688-.414.385.039.666.41.627.829a.785.785 0 0 1-.104.32l.008.005zM7.99 3.014L6.348 6.441l-3.347.579 1.685 2.042a12.73 12.73 0 0 1-1.333.434L1.268 7.107a.773.773 0 0 1-.259-.575c0-.345.221-.626.52-.723l.008-.034 3.928-.776 1.869-3.597h.03a.724.724 0 0 1 .642-.416c.279 0 .513.169.637.409h.028l1.722 3.31c-.318.429-.659.839-1.027 1.224L7.99 3.014z"></path>
                    </symbol>
                    <symbol id="svg_icon_vip_star" viewBox="0 0 20 20">
                      <path
                        d="M134,1284.83h0l-4.4-.66a7.59,7.59,0,0,1-2.1,6.91,7.974,7.974,0,0,1-3.4,1.9l6,3.03h0.2s0.1-.1,0-0.1l-1.2-6.34,4.9-4.55v-0.19Zm-15.4,6.73a9.7,9.7,0,0,0,1.6.19,7.762,7.762,0,0,0,5.4-2.09,6.915,6.915,0,0,0,2.2-5.68l-0.7-.09-3-5.78-0.1-.09a0.1,0.1,0,0,0-.1.09l-3,5.78-6.8.94a0.1,0.1,0,0,0-.1.1v0.09l4.9,4.55Zm3.2,1.7a7.994,7.994,0,0,1-3.4-.76l-0.6,3.32v0.09H118l6-3.03A5.543,5.543,0,0,1,121.8,1293.26Z"
                        transform="translate(-114 -1278.03)"></path>
                    </symbol>
                    <symbol id="svg_icon_gift" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" clip-rule="evenodd" fill="currentColor"
                            d="M17,6V4.5C17,2.567,15.433,1,13.5,1h-1   c-0.981,0-1.865,0.406-2.5,1.056C9.365,1.406,8.481,1,7.5,1h-1C4.567,1,3,2.567,3,4.5V6C1.895,6,1,6.896,1,8v8c0,1.104,0.895,2,2,2   h14c1.105,0,2-0.896,2-2V8C19,6.896,18.105,6,17,6z M11,4.5C11,3.672,11.672,3,12.5,3h1C14.328,3,15,3.672,15,4.5V6h-4V4.5z M5,4.5   C5,3.672,5.672,3,6.5,3h1C8.328,3,9,3.672,9,4.5V6H5V4.5z M3,8h5v8H3V8z M17,16h-5V8h5V16z"></path>
                    </symbol>
                    <symbol id="svg_icon_right_sm" viewBox="0 0 16 16">
                      <path
                        d="M11.71 8.716L7.716 12.71a1.01 1.01 0 0 1-1.427-1.427L9.573 8 6.289 4.716a1.01 1.01 0 0 1 1.427-1.427l3.994 3.994c.198.198.296.458.295.717.001.259-.097.518-.295.716z"></path>
                    </symbol>
                    <symbol id="svg_icon_qr_sm" viewBox="0 0 16 16">
                      <path
                        d="M13.5 11.5a1 1 0 0 1-1-1 1 1 0 0 1 0-2h1a1 1 0 0 1 1 1v1a1 1 0 0 1-1 1zm0-4h-4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1zm-1-4h-2v2h2v-2zm-6 11h-4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1zm-1-4h-2v2h2v-2zm1-3a1 1 0 0 1-1-1v-4a1 1 0 0 1 2 0v4a1 1 0 0 1-1 1zm-3 0h-1a1 1 0 0 1 0-2 1 1 0 0 1 2 0v1a1 1 0 0 1-1 1zm0-4h-1a1 1 0 0 1 0-2h1a1 1 0 0 1 0 2zm6 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm0 4a1 1 0 0 1 2 0v1a1 1 0 0 1-1 1h-1a1 1 0 0 1 0-2zm4 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"></path>
                    </symbol>
                  </svg>

                  <div id="_vip_player_sec" _r-cid="11" _r-component="c-vip">
                    <div class="mod_vip_sidebar status3" style="z-index: unset;">
                    </div>
                  </div>


                  <div style="">
                    <div class="mod_episode_filter _page_list">

                    </div>

                    <div class="mod_figure mod_figure_list mod_figure_list_sm" _wind="columnname=选集"
                         data-tpl="pic-title">
                      <ul class="figure_list" id="_pic_title_list_ul">



                      </ul>

                    </div>

                  </div>

                </div>
              </div>


              <div class="panel_body panel_body_2" id="mod_active_content" r-notemplate="true" _r-cid="12"
                   _r-component="c-active" style="display: none;">
              </div>

            </div>
            <div class="mod_barrage_list none" id="barrage_container" r-notemplate="true" _r-cid="13"
                 _r-component="c-barrage-list"></div>
          </div>
          <div id="dark_layer" class="dark_layer"></div>
        </div>

        <div class="player_headline player_headline_mood cf" _r-cid="14" _r-component="c-intro">
          <div class="mod_intro">
            <div class="video_base _base" r-notemplate="true">
              <h1 class="video_title _video_title">

                {{info.name}}


              </h1>

            </div>

            <div class="video_info_wrap" style="">
              <div class="video_info">
                <div class="tag_item tag_item_intro icon_display">
                  <i class="icon_sm icon_intro_sm">
                    <svg class="svg_icon svg_icon_cup_sm" viewBox="0 0 16 16" width="16" height="16">
                      <use xlink:href="#svg_icon_video_intro"></use>
                    </svg>
                  </i>
                  <span class="icon_text">内容简介</span>
                  <i class="icon_sm icon_arrow_down_sm icon_rotate_down">
                    <svg class="svg_icon svg_icon_cup_sm" viewBox="0 0 16 16" width="16" height="16">
                      <use xlink:href="#svg_icon_arrow_down_xs"></use>
                    </svg>
                  </i>
                </div>


                <div class="video_user _video_user" style="display:none;">


                  <span class="user_name"></span>


                  <a href="javascript:" class="btn_book" title="订阅" _stat="intro:order">
                    订阅
                  </a>

                </div>


                <div class="video_tags _video_tags">


                  <a _stat="intro:tag" href="javascript:;" target="_blank"
                     class="tag_item">{{}}</a>


                  <a _stat="intro:tag" href="javascript:;" target="_blank"
                     class="tag_item">{{}}</a>


                  <a _stat="intro:tag"
                     href="javascript:;"
                     target="_blank" class="tag_item">{{info.level_text}}</a>

                </div>
              </div>
            </div>

          </div>

          <div class="mod_mood" r-notemplate="true" _r-cid="15" _r-component="c-mood">
            <div class="mood_like" _stat="mood:thumbsup">
              <i class="icon_mood icon_mood_like">
                <svg class="svg_icon_mood svg_icon_mood_like" viewBox="0 0 22 22" width="22" height="22">
                  <g class="svg_icon_true">
                    <circle cx="11" cy="11" r="11" fill="#fac82f"></circle>
                    <path class="path_1"
                          d="M11 19c-4.418 0-8-3.437-8-7.676 0-.044.006-.085.007-.128A27.188 27.188 0 0 1 11 10c2.788 0 5.473.422 7.993 1.196.001.043.007.084.007.128C19 15.563 15.418 19 11 19z"
                          fill="#e62929"></path>
                    <path class="path_2"
                          d="M7.712 6.679L5.655 8.715a.976.976 0 0 1-1.371 0 .952.952 0 0 1 0-1.357L5.655 6 4.284 4.642a.952.952 0 0 1 0-1.357.976.976 0 0 1 1.371 0l2.057 2.036a.953.953 0 0 1 0 1.358zM14.288 6.679l2.057 2.036a.976.976 0 0 0 1.371 0 .952.952 0 0 0 0-1.357L16.345 6l1.371-1.358a.952.952 0 0 0 0-1.357.976.976 0 0 0-1.371 0l-2.057 2.036a.953.953 0 0 0 0 1.358z"
                          fill="#000"></path>
                  </g>
                  <g class="svg_icon_false">
                    <path
                      d="M11 11c-4.418 0-8-3.437-8-7.676 0-.044.006-.085.007-.128A27.188 27.188 0 0 1 11 2c2.788 0 5.473.422 7.993 1.196.001.043.007.084.007.128C19 7.563 15.418 11 11 11z"
                      fill="#e62929"></path>
                    <circle cx="11" cy="11" r="11" fill="#777"></circle>
                    <path
                      d="M11 19c-4.418 0-8-3.437-8-7.676 0-.044.006-.085.007-.128A27.188 27.188 0 0 1 11 10c2.788 0 5.473.422 7.993 1.196.001.043.007.084.007.128C19 15.563 15.418 19 11 19zm6.716-10.285a.976.976 0 0 1-1.371 0l-2.057-2.036a.953.953 0 0 1 0-1.358l2.057-2.036a.976.976 0 0 1 1.371 0 .952.952 0 0 1 0 1.357L16.345 6l1.371 1.358a.952.952 0 0 1 0 1.357zm-12.061 0a.976.976 0 0 1-1.371 0 .952.952 0 0 1 0-1.357L5.655 6 4.284 4.642a.952.952 0 0 1 0-1.357.976.976 0 0 1 1.371 0l2.057 2.036a.953.953 0 0 1 0 1.358L5.655 8.715z"
                      fill="#2e2e37"></path>
                  </g>
                </svg>
              </i>
              <span class="icon_text">顶</span>
            </div>
            <div class="mood_value">
              <div class="mood_progress">
                <div class="mood_progress_value _mood_progress" style="width: 60%;"></div>
              </div>
              <span class="mood_plusone">+1</span>
              <div class="mood_text _mood_text">60%</div>
            </div>
            <div class="mood_dislike" _stat="mood:thumbsdown">
              <i class="icon_mood icon_mood_dislike">
                <svg class="svg_icon_mood svg_icon_mood_like" viewBox="0 0 22 22" width="22" height="22">
                  <linearGradient id="svg_defs_dislike" gradientUnits="userSpaceOnUse" x1="11" y1="22" x2="11">
                    <stop offset="0" stop-color="#fac82f"></stop>
                    <stop offset="1" stop-color="#3bb474"></stop>
                  </linearGradient>
                  <g class="svg_icon_true">
                    <circle fill="url(#svg_defs_dislike)" cx="11" cy="11" r="11"></circle>
                    <g class="svg_g_face">
                      <circle fill="#000" cx="6.5" cy="12.5" r="1.5"></circle>
                      <circle fill="#000" cx="15.5" cy="12.5" r="1.5"></circle>
                      <path fill="#000"
                            d="M13.971 19.001c-.23 0-.462-.074-.653-.225-.661-.52-1.463-.794-2.319-.794s-1.658.274-2.319.795c-.439.346-1.089.284-1.45-.138s-.297-1.046.144-1.392c1.018-.801 2.306-1.243 3.625-1.243s2.607.442 3.626 1.244a.962.962 0 0 1 .143 1.391 1.047 1.047 0 0 1-.797.362z"></path>
                    </g>
                  </g>
                  <g class="svg_icon_false">
                    <circle cx="11" cy="11" r="11" fill="#777"></circle>
                    <path
                      d="M15.5 14a1.5 1.5 0 1 1 .001-3.001A1.5 1.5 0 0 1 15.5 14zm-.732 4.639a1.047 1.047 0 0 1-.797.362c-.23 0-.462-.074-.653-.225a3.712 3.712 0 0 0-2.319-.794c-.856 0-1.658.274-2.319.795a1.06 1.06 0 0 1-1.45-.138.961.961 0 0 1 .144-1.392 5.883 5.883 0 0 1 3.625-1.243c1.319 0 2.607.442 3.626 1.244a.962.962 0 0 1 .143 1.391zM6.5 14a1.5 1.5 0 1 1 .001-3.001A1.5 1.5 0 0 1 6.5 14z"
                      fill="#2e2e37"></path>
                  </g>
                </svg>
              </i>
              <span class="icon_text">踩</span>
            </div>
          </div>

        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>

    import Head from "./common/Head";
    import Footer from "./common/Footer";

    export default {

        name: "Detail",
        components: {
            Head,
            Footer,
        },
        data(){
            return{
              info:[],
                playerOptions: {
                    playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                    autoplay: false, //如果true,浏览器准备好时开始回放。
                    muted: false, // 默认情况下将会消除任何音频。
                    loop: false, // 导致视频一结束就重新开始。
                    preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                    language: 'zh-CN',
                    aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                    sources: [{
                        type: "video/mp4",//这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
                        src: "" //url地址
                    }],
                    poster: "", //你的封面地址
                    // width: document.documentElement.clientWidth, //播放器宽度
                    notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                    controlBar: {
                        timeDivider: true,
                        durationDisplay: true,
                        remainingTimeDisplay: false,
                        fullscreenToggle: true  //全屏按钮
                    }
                }
            }
        },
        created() {
            this.get_video_info();
        },
        methods:{

            onPlayerPlay(e){

            },
            onPlayerPause(e){

            },

            get_video_info(){
                this.$axios.get(`${this.$settings.Host}/video/${this.$route.params.id}`).then(response=>{
                    this.info = response.data;
                    console.log("zzzzzzzzzzz",response.data);
                    this.playerOptions.sources[0].src = response.data.file_url
                }).catch(error=>{
                    this.$alert("网络错误!", '广东理工学院')
                })
            }
        }
    }
</script>

<style src="../../static/css/tx_video.css"></style>
<style scoped >
  .container_player {
    z-index: 15;
    padding: 0;
    background: #0f0f1e;
  }

  .site_container {
    z-index: 2;
    position: relative;
    width: 100%;
    word-break: break-all;
  }
</style>
