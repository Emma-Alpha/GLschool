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
            <img src="//thirdqq.qlogo.cn/g?b=oidb&amp;k=u8ovAQBCkFQibURggAH2PaQ&amp;s=640&amp;t=1556857804" alt=""
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
            <span class="__nickname">无奈之下</span>
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
              <div class="num" id="channelInfoVideo">2</div>
              <div class="text">视频</div>
            </div>
            <div class="item">
              <div class="num" id="channelInfoSubs">1</div>
              <div class="text">订阅</div>
            </div>
            <div class="item">
              <div class="num" id="channelInfoCounts">1982</div>
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

          <div class="item">
            <a href="/biu/u/playlist" class="navi_link _collect" _hot="uc.side._collect">
              <svg class="svg_side_icon svg_icon_collect" viewBox="0 0 18 18" width="18" height="18">
                <path d="M4.7 11C3.3 9.7 2 8 2 6.1 2 1.3 7.3 1 9 4c1.6-3 7-2.8 7 2" stroke="currentColor"
                      stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"></path>
                <path d="M12 17a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm1-6V9h-2v2H9v2h2v2h2v-2h2v-2h-2z" fill="currentColor"
                      fill-rule="nonzero"></path>
              </svg>
              收藏<span class="mark_dot none" id="sidenav_notice_playlist"></span></a>
          </div>

          <div class="item">
            <a href="/biu/u/subscribe" class="navi_link _follow" _hot="uc.side._follow">
              <svg class="svg_side_icon svg_icon_follow" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M8.5 14.2l-3 1.6a1 1 0 0 1-1.4-1l.5-3.4a1 1 0 0 0-.3-.9L2 8.1a1 1 0 0 1 .5-1.7L5.8 6a1 1 0 0 0 .8-.5l1.5-3a1 1 0 0 1 1.8 0l1.5 3a1 1 0 0 0 .8.5l3.4.5a1 1 0 0 1 .5 1.7l-2.4 2.4a1 1 0 0 0-.3 1l.5 3.3a1 1 0 0 1-1.4 1l-3-1.6a1 1 0 0 0-1 0z"
                  stroke="currentColor" stroke-width="2" fill="none"></path>
              </svg>
              订阅</a>
          </div>

          <div class="item">
            <a href="/u/doki.html" class="navi_link _doki">
              <svg class="svg_side_icon svg_icon_doki" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M14.6 10.3a4.1 4.1 0 1 0-5.9-5.9m.6 0a.5.5 0 0 1 0 .1l5.2 5.1a.5.5 0 0 1 0 .7l-4.8 4.8a1 1 0 0 1-1.4 0l-4.8-4.8a4.1 4.1 0 1 1 5.8-5.8z"
                  fill="none" stroke="currentColor" stroke-width="2"></path>
              </svg>
              我的doki</a>
          </div>

          <div class="item">
            <a href="/u/comment/" class="navi_link _message" _hot="uc.side._message">
              <svg class="svg_side_icon svg_icon_message" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M3.8 13.4A1.8 1.8 0 0 1 2 11.6V3.8C2 2.8 2.8 2 3.8 2h10.4c1 0 1.8.8 1.8 1.8v7.8a1.8 1.8 0 0 1-1.8 1.8h-6L5.4 16"
                  stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                  fill="none"></path>
                <path d="M6.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"
                      fill="currentColor"></path>
              </svg>
              评论</a>
          </div>

          <div class="item">
            <a href="/u/message/" class="navi_link _notice" _hot="uc.side._notice">
              <svg class="svg_side_icon svg_icon_notice" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M14 7v1.6l2.7 3c.2.4.1 1-.2 1.3a.8.8 0 0 1-.5.1H2c-.5 0-.8-.4-.8-.9l.1-.5 2.7-3V7m10 0A5 5 0 0 0 4 7M6 14c.5 1.2 1.7 2 3 2s2.5-.8 3-2"
                  stroke-linecap="round" stroke-linejoin="round" stroke="currentColor" stroke-width="2"
                  fill="none"></path>
              </svg>
              消息</a>
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

          <div class="item" role="realname-auth">
            <a href="//v.qq.com/u/realname.html" class="navi_link _realname">
              <svg class="svg_side_icon svg_icon_realname" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M9 2a37.7 37.7 0 0 0 3.8.8l3 .5c.4 3.9.1 6.8-.8 8.7s-3 3.2-6 4c-3-.8-5-2.1-6-4s-1.2-4.8-.8-8.8l3-.4A37.7 37.7 0 0 0 9 2z"
                  stroke="currentColor" stroke-width="2" fill="none"></path>
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 9l2 2 5-5" stroke="currentColor"
                      stroke-width="2" fill="none"></path>
              </svg>
              实名认证</a>
          </div>


          <div class="item none" id="fans_admin">
            <a href="//cp.doki.qq.com" target="_blank _fansadmin" class="navi_link" _hot="uc.side._fans">
              <svg class="svg_side_icon svg_icon_stars" viewBox="0 0 18 18" width="18" height="18">
                <path
                  d="M20 8.2v.1l-.1.2-.1.1-9 8.9-.1.2-.2.1-.1.1h-.2l-.2.1h-.4l-.1-.1-.2-.2-.1-.2-9-8.8v-.1L0 8.2v-.8l3-5 .1-.1.1-.1.3-.2.6-.1h12.2v.1c.1 0 .2 0 .3.2l.2.2 3 5v.7zM15.4 4H4.6L2.2 7.9l7.8 7.7 7.8-7.7L15.4 4zM10 13h-.4l-.1-.1-.2-.2-.1-.2-4-4a1 1 0 0 1 .3-1.4 1 1 0 0 1 1.4.4l3.1 3.1 3.1-3.1a1 1 0 0 1 1.4-.4c.5.3.6 1 .4 1.4l-4 4-.2.2-.2.1-.1.1h-.2l-.2.1z"
                  fill="currentColor"></path>
              </svg>
              明星社区</a>
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
            }
        },
        created() {
            this.token = this.$settings.check_user_login()
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
