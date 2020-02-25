<template>
  <div>
    <Head></Head>
    <div class="site_head_placeholder"></div>
    <div class="site_wrapper cf">
      <div class="user_navigate" id="side_nav">

        <!-- 用户信息侧 -->
        <div class="user_info __user_info_side">
          <!-- 头像 -->
          <div class="navi_avatar navi_avater">
            <img :src='user_info_img' alt=""
                 class="avatar_pic __avatar">
            <button class="option_toggle">
              <svg class="svg_side_icon svg_icon_user" viewBox="0 0 18 18" width="18" height="18">
                <circle cx="9" cy="7" r="5" stroke="currentColor" stroke-width="2" fill="none"></circle>
                <path d="M16 15.9A10 10 0 0 0 9 13a10 10 0 0 0-7 3" stroke-linecap="round" stroke-linejoin="round"
                      stroke="currentColor" stroke-width="2" fill="none"></path>
              </svg>
              <span class="inner">切换</span>
            </button>
          </div>

          <!-- 用户名 -->
          <div class="user_name">
            <span class="__nickname">{{user_info_name}}</span>
          </div>
          <div class="user_vipinfo user_holly">

          </div>

        </div>

        <div class="user_channel_info">
          <a href="//c.v.qq.com/vchannelhomepage?url=157955270&amp;type=1" class="channel_link _user" target="_blank">
            <svg class="svg_side_icon svg_icon_user" viewBox="0 0 18 18" width="18" height="18">
              <circle cx="9" cy="7" r="5" stroke="currentColor" stroke-width="2" fill="none"></circle>
              <path d="M16 15.9A10 10 0 0 0 9 13a10 10 0 0 0-7 3" stroke-linecap="round" stroke-linejoin="round"
                    stroke="currentColor" stroke-width="2" fill="none"></path>
            </svg>
            我的个人频道
          </a>
          <div class="channel_info">
            <div class="item">
              <div class="num" id="channelInfoVideo">0</div>
              <div class="text">视频</div>
            </div>
            <div class="item">
              <div class="num" id="channelInfoSubs">0</div>
              <div class="text">订阅</div>
            </div>
            <div class="item">
              <div class="num" id="channelInfoCounts">0</div>
              <div class="text">播放量</div>
            </div>
          </div>
        </div>

        <div class="user_navigate_list">
          <div class="item">
            <a href="/biu/u/history" class="navi_link _time" _hot="uc.side._time">
              <svg class="svg_side_icon svg_icon_time" viewBox="0 0 18 18" width="18" height="18">
                <circle cx="9" cy="9" r="7" stroke="currentColor" stroke-width="2" fill="none"></circle>
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5v5h3" stroke="currentColor" stroke-width="2"
                      fill="none"></path>
              </svg>
              观看历史</a>
          </div>

          <div class="item current">
            <a href="/u/upload.html" class="navi_link _upload" _hot="uc.side._upload">
              <svg class="svg_side_icon svg_icon_upload" viewBox="0 0 18 18" width="18" height="18">
                <path d="M16 10v2a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4v-2m7 1V2m4 4L9 2 5 6" fill="none" stroke-linecap="round"
                      stroke-linejoin="round" stroke="currentColor" stroke-width="2"></path>
              </svg>
              上传视频</a>
          </div>

          <div class="item">
            <a href="/u/videos" class="navi_link _folder" _hot="uc.side._folder">
              <svg class="svg_side_icon svg_icon_folder" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M4 2h1.659a2 2 0 0 1 1.658.882l.7 1.036a2 2 0 0 0 1.657.882H14a2 2 0 0 1 2 2V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z"
                  stroke="currentColor" stroke-width="2" fill="none"></path>
                <path
                  d="M10 1h5a1 1 0 0 1 0 2h-5a1 1 0 1 1 0-2zM8 12h2a1 1 0 0 1 0 2H8a1 1 0 0 1 0-2zm5 0h2a1 1 0 0 1 0 2h-2a1 1 0 0 1 0-2zM3 12h2a1 1 0 0 1 0 2H3a1 1 0 0 1 0-2z"
                  fill="currentColor"></path>
              </svg>
              管理视频</a>
          </div>

        </div>
      </div>
      <div class="site_main">
        <div class="main_content j_upload_page">
          <div class="extra_tips j_first_page" id="ftn_install_tips_cont" style="display: none;">
            <i class="icon_download"></i><span class="inner">下载插件即可上传超大10G视频</span><a id="install_ftn_btn"
                                                                                      href="http://mail.qq.com/cgi-bin/readtemplate?t=browser_addon&amp;check=false&amp;s=install&amp;returnto=https%3A%2F%2Fv.qq.com%2Fu%2Fupload.html"
                                                                                      class="btn_install">开始安装</a>
          </div>
          <div class="upload_option j_upload_option j_first_page">
            <div class="btn_upload j_btn_upload">
              <form
                id="myForm"
                enctype="multipart/form-data"
                name="fileinfo"
                action=""
                target="uploadFrame"
              >
                <div class="img-file">
                  <input
                    style="display: none"
                    @change="upload_file"
                    id="imgFile"
                    class="upload_input"
                    type="file"
                    accept="video/*"
                  />
                </div>
              </form>
              <a class="btn_select_file" onclick="javascript:document.getElementById('imgFile').click()">点击上传</a>
            </div>
          </div>


        </div>
      </div>
    </div>

  </div>
</template>


<script>
    import '../../static/css/upload.css'
    import Head from "./common/Head";

    export default {
        name: "Upload",
        components: {
            Head,
        },
        data() {
            return {
                token: '',
                upload_url: '',
                user_info_img:'',
                user_info_name:'',
            }
        },
        created() {
            this.token = this.$settings.check_user_login();
            this.get_user_Info()
        },
        methods: {
            upload_file() {
                var formdata = new FormData();
                var file = document.getElementById('imgFile').files[0];
                if (file) {
                    formdata.append('file_url', file);
                    formdata.append('name', file.name);
                }
                this.$axios.post(`${this.$settings.Host}/video/upload/`, formdata, {
                    'Content-Type': 'multipart/form-data',
                    headers: {
                        Authorization: 'jwt ' + this.token
                    }
                }).then(response => {
                    console.log(response.data)
                }).catch(error => {
                    console.log(error.response)
                })

            },
            get_user_Info(){
                this.user_info_img = localStorage.getItem('avatar') || sessionStorage.getItem('avatar');
                this.user_info_name = localStorage.getItem('user_nickname') || sessionStorage.getItem('user_nickname');
            },
        }
    }
</script>

<style>
  .site_head_absolute .mod_quick .quick_link {
    color: #111111;
    color: rgba(0, 0, 0) !important;
  }

  .site_head_absolute .mod_search .search_input {
    color: #999;
    text-shadow: 0 0 2px rgba(17, 18, 38, .2);
  }

</style>
