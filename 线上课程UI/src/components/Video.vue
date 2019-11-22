<template>
  <div>
    <Header></Header>
    <div id="v-bo">
      <div class="container">
        <div class="player" style="width: 600px;margin: 0 auto">
          <video-player class="video-player vjs-custom-skin"
                        ref="videoPlayer"
                        :playsinline="true"
                        :options="playerOptions"
                        @play="onPlayerPlay($event)"
                        @pause="onPlayerPause($event)"
          >
          </video-player>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import {videoPlayer} from 'vue-video-player';

    var lst = [];
    var video_dist = {};
    var url = window.location.href;
    console.log(url);
    lst = url.split('/');
    console.log(lst[lst.length-1]);

    if(lst[lst.length-1] == 4){
        video_dist['type'] = 'video/mp4';
        video_dist['src'] = '/static/video/小姐姐后生仔.MP4'
    }
    if(lst[lst.length-1] == 2){
        video_dist['type'] = 'video/mp4';
        video_dist['src'] = '/static/video/bg.mp4'
    }
    if(lst[lst.length-1] == 1){
        video_dist['type'] = 'video/mp4';
        video_dist['src'] = '/static/video/小视频.mp4'
    }

    export default {
        data() {
            return {
                playerOptions: {
                    playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                    autoplay: false, //如果true,浏览器准备好时开始回放。
                    muted: false, // 默认情况下将会消除任何音频。
                    loop: false, // 导致视频一结束就重新开始。
                    preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                    language: 'zh-CN',
                    aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                    sources: [
                        video_dist
                        // {
                        //     type:"video/mp4",
                        //     src:"/static/bg.mp4"
                        // }
                        ],
                    poster: "poster.jpg", //你的封面地址
                    width: document.documentElement.clientWidth,
                    notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                    // controlBar: {
                    //     timeDivider: true,
                    //     durationDisplay: true,
                    //     remainingTimeDisplay: false,
                    //     fullscreenToggle: true //全屏按钮
                    // }
                }
            }
        },
        components: {
            videoPlayer,
            Header,
            Footer,
        },
        methods: {
            onPlayerPlay(player) {

            },
            onPlayerPause(player) {

            },
        },
        computed: {
            player() {
                return this.$refs.videoPlayer.player
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style type="text/css">
  .container {
    background-color: #efefef;
  }

  #v-bo {
    margin: 40px auto;
  }


</style>
