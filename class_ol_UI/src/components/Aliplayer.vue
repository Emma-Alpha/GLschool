<template>
  <div>
    <div class="prism-player" id="J_prismPlayer"></div>
    <p>hellow</p>
  </div>
</template>

<script>
    export default {
        name: "Aliplayer",
        data() {
            return {
                playerId: "aliplayer_" + Math.random().toString(36).substr(2),
                scriptTagStatus: 0,
                isReload: false,
                instance: null,

            }
        },
        mounted() {
            var player = new Aliplayer({
                id: 'J_prismPlayer',
                width: '50%',
                autoplay: true,
                //支持播放地址播放,此播放优先级最高
                source: 'https://act.mcake.com/fangli/2018/pc/zhou-nian/video/zhounian-7.mp4',

            }, function (player) {
                player.mute();
                player.play();
            });
            player.on('autoplay', function (data) {
                if (data.paramData) //可以自动播放
                {
                    //隐藏提示
                    console.log(11111)
                } else //不可以自动播放
                {
                    console.log(2222)
                    //显示提示用户点击播放
                }

            });
        }

    }
</script>

<style scoped>
  @import 'https://g.alicdn.com/de/prismplayer/2.7.2/skins/default/aliplayer-min.css';
</style>
