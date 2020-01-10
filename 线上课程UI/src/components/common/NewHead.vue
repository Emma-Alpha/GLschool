<template>
  <div class="site_slider site_slider_intrude">
    <!--    焦点图-->
    <div class="slider_inner">
      <a class="slider_item in" id="focus_img" href="#"
         _stat="焦点图:大图"
         target="_blank"
         style="background-color: rgb(172, 55, 20);"
        @mouseover=""
      ></a>
    </div>
    <!--    焦点图轮播-->
    <div class="slider_nav _quicklink slider_nav_watched" _wind="columnname=精选_焦点图&amp;controlname=new_vs_focus">
      <a href="http://v.qq.com/u/history/" _stat="焦点图:轮播图:大标题入口" class="nav_link nav_link_mine" target="_blank"
         data-bgcolor="#3b7580" data-bgimage="//puui.qpic.cn/vupload/0/common_blank.png/0"
         @mouseover="get_hot"

         :style="withe===false?'color:#fff;':''"
      >
        <svg class="svg_slider_icon svg_icon_zj" width="16" height="11">
          <path class="path_1" d="M15 8A7 7 0 0 0 1 8" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round" fill="none"
                :style="withe===false?'fill:url(#__gradient_zb_light)':''"></path>
          <path class="path_2" d="M8.9 5.1a1.5 1.5 0 1 0 2 2 3 3 0 1 1-2-2z" fill="currentColor"></path>
        </svg>
        <span class="">大家在看</span></a>
      <span class="nav_label">
                                <svg class="svg_slider_icon svg_icon_zb" width="12" height="15">
                                    <defs>
                                        <linearGradient x1="41.309%" y1="32.314%" x2="71.734%" y2="100%"
                                                        id="__gradient_zb_light">
                                            <stop stop-color="#FF9630" offset="0%"/>
                                            <stop stop-color="#FF9630" offset="0%"/>
                                            <stop stop-color="#FF1E1E" offset="100%"/>
                                        </linearGradient>
                                    </defs>
                                    <path class="path_1 "
                                          :style="withe===true?'fill:url(#__gradient_zb_light)':''"
                                          d="M3.6 15C-.5 12.2-1.1 8.8 1.7 4.9 3.3 2.8 4.3 2.1 4.3 0c.4.2 5.1 2.6 4 7.5 1-.5 1.7-1.7 2-3.5 2.3 3.8 2.3 6.9-.1 9.4-.4.6-1.2 1.1-1.8 1.6-1.4-.6-3-1.9-3.6-5.6-1.3 1.4-1.7 3.3-1.2 5.6z"/>
                                    <path class="path_2"
                                          d="M.3 7.7c.3-.9.7-1.8 1.4-2.8C3.3 2.8 4.3 2.1 4.3 0 4.5.1 5.8.8 7 2.1c.5 2.7-1.3 5.3-4 5.8-1 .2-1.9.1-2.7-.2z"
                                          fill="#ffb821"/>
                                </svg><span :style="withe===true?'color: #fff':''">重磅推荐</span>
                            </span>

      <a v-for="fuc in results"
         href="#"
         target="_blank"
         class="nav_link"
         data-bgcolor="#81a1c8"
         :data-bgimage="fuc.course_img"
         data-navcolor="undefined"
         @mouseover="find_focus_img(fuc.course_img, fuc.id)"
      ><span class="text text2" :title="fuc.name"><span class="title_text">{{fuc.name}}</span
      >{{fuc.teacher.name}}</span></a>


    </div>
  </div>
</template>

<script>
    export default {
        name: "NewHead",
        data() {
            return {
                focus_img_url: '', //热门图片的定义
                withe: false,
                stop_show: false,
                time: 1,
                results: [],
            }
        },
        created() {
            this.get_banner();
            // this.order_show();
        },
        watch: {
            // stop_show() {
            //     if (this.stop_show === false) {
            //         this.order_show()
            //     }
            // }
        },

        methods: {
            get_hot() {
                this.withe = false;
                this.stop_show = true;
                var url = document.getElementById('focus_img');
                url.style.backgroundImage = 'url(' + this.focus_img_url + ')';
            },

            // order_show() {
            //     let timer = setInterval(() => {
            //         if (this.time < 9) {
            //             let _a = document.getElementsByClassName('nav_link');
            //             let url = _a[this.time].getAttribute('data-bgimage');
            //             this.find_focus_img(url);
            //             ++this.time;
            //         } else {
            //             this.time = 1
            //         }if(this.stop_show === true){
            //             clearInterval(timer)
            //         }
            //     }, 3000)
            // },

            find_focus_img(img_url, num) {
                this.stop_show = true;
                this.withe = true;
                var url = document.getElementById('focus_img');
                url.style.backgroundImage = 'url(' + img_url + ')';
            },
            get_banner() {

                //轮播风景图
                // es6提供了一种允许换行的字符串，叫文档字符串，可以允许在字段中换行并输出js变量
                this.$axios.get(`${this.$settings.Host}/course/`).then(response => {
                    this.results = response.data.results;
                    // this.focus_img_title_url = response.data.
                    console.log(response.data.results);
                    this.focus_img_url = response.data.results[response.data.results.length - 1].course_img;
                    var url = document.getElementById('focus_img');
                    url.style.backgroundImage = 'url(' + this.focus_img_url + ')';
                }).catch(error => {
                    this.$alert("获取轮播图失败", '广东理工学院')
                })
            }
        }
    }
</script>

<style scoped>

  .nav_link {
    background-position-x: 0;
  }

  .site_slider {
    margin-top: 0;
    height: 420px;
    z-index: 1;
    position: relative;
    margin-bottom: 30px;
    overflow: hidden;
  }

  .site_slider .slider_inner {
    position: absolute;
    width: 100%;
    height: 100%;
    transition: transform 1.8s ease, -webkit-transform 1.8s ease;
  }

  @media (max-width: 1280px) {
    .site_slider .slider_item {
      background-size: auto 100%;
    }
  }

  .site_slider .out {
    z-index: 0;
    opacity: 0;
  }

  .site_slider .slider_item {
    position: absolute;
    width: 100%;
    height: 100%;
    background-position: center 0;
    background-repeat: no-repeat;
  }

  .site_slider .in {
    z-index: 1;
    opacity: 1;
  }

  @media (max-width: 1280px) {
    .site_slider_intrude .slider_nav_watched {
      padding-top: 0;
    }
  }

  @media (max-width: 1280px) {
    .site_slider .slider_nav {
      width: 240px;
    }
  }

  .page_channel_choice .slider_nav {
    top: 68px;
  }

  .site_slider .slider_nav {
    -webkit-user-select: none;
    z-index: 2;
    position: absolute;
    right: 0;
    bottom: 0;
    overflow: hidden;
  }

  .site_slider .slider_nav_watched .nav_link_mine {
    margin-bottom: 15px;
  }

  @media (max-width: 1280px) {
    .site_slider .slider_nav_watched .nav_label, .site_slider .slider_nav_watched .nav_link_mine {
      font-size: 20px;
    }
  }

  .site_slider .slider_nav_watched .nav_link {
    height: 29px;
    margin-left: 40px;
    line-height: 29px;
  }
</style>
