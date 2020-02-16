<template>
  <div class="site_head site_head_absolute" id="new_vs_header">
    <div class="head_inner">
      <h1 class="site_logo"><a href="javascript:;" class="link_logo" _stat="顶部导航区:主导航_LOGO">广东理工学院</a></h1>


      <img class="unusual_pic none" data-choice="" data-tv="" data-movie="" data-variety="" data-cartoon=""
           data-child="" data-doco="" data-hlw="" data-music="" data-sports=""
           src="javascript:;" alt="">

      <div class="mod_search">
        <form id="searchForm" action="javascript:" method="get" target="_blank" class="search_form cf">
          <label class="search_label" for="keywords">搜索关键词</label>
          <div class="search_keywords">
            <input type="text" name="q" id="keywords" class="search_input" autocomplete="off"
                   _stat="顶部导航区_搜索框" :value="choice_search?'':search_word" @click.prevent="choice_search=true"
                   @blur="choice_search=false">
          </div>
          <input type="hidden" name="stag">
          <input type="hidden" name="smartbox_ab">
          <button class="search_btn" type="submit" _stat="顶部导航区_搜索按钮">
            <svg class="svg_icon svg_icon_search" viewBox="0 0 18 18" width="18" height="18">
              <path
                d="M4.5 4.5c-1.9 1.9-1.9 5.1 0 7.1s5.1 1.9 7.1 0 1.9-5.1 0-7.1-5.2-2-7.1 0zm10.8 12.2l-3.1-3.1c-2.7 2-6.6 1.9-9.1-.6C.3 10.2.3 5.8 3 3 5.7.3 10.2.3 12.9 3c2.5 2.5 2.7 6.4.6 9.1l3.1 3.1c.4.4.4 1 0 1.4-.3.5-.9.5-1.3.1z"
                fill="currentColor"></path>
            </svg>
            <span class="btn_inner">搜一下</span></button>
          <a class="btn_search_hot" href="javascript:;"
             target="_blank" title="热搜榜">
            <svg class="svg_icon_fire" width="12" height="15" viewBox="0 0 12 15">
              <linearGradient x1="41.309%" y1="32.314%" x2="71.734%" y2="100%" id="__gradient_fire">
                <stop stop-color="#FF9630" offset="0%"></stop>
                <stop stop-color="#FF9630" offset="0%"></stop>
                <stop stop-color="#FF1E1E" offset="100%"></stop>
              </linearGradient>
              <path
                d="M6.634 17C2.539 14.21 1.905 10.843 4.73 6.898 6.307 4.845 7.253 4.053 7.253 2c.353.183 5.134 2.569 4.024 7.5 1.01-.505 1.684-1.659 2.025-3.463 2.28 3.767 2.264 6.9-.051 9.4-.489.528-1.211 1.05-1.873 1.563-1.33-.625-2.932-1.875-3.573-5.625C6.524 12.833 6.133 14.708 6.634 17z"
                fill="url(#__gradient_fire)" transform="translate(-3 -2)"></path>
            </svg>
            热搜榜
          </a>
        </form>
        <div class="mod_smartbox none" id="smartbox"></div>
      </div>
      <!-- 快捷入口 开始 -->
      <div class="mod_quick cf">

        <!-- 历史浮层 -->
        <div class="quick_item quick_history" id="modHistory">
          <a href="javascript:;" class="quick_link" target="_blank" _stat="顶部导航区:观看历史">

            <svg class="svg_quick_icon svg_icon_time" viewBox="0 0 26 26" width="26" height="26">
              <circle cx="13" cy="13" r="11" fill="none" stroke="currentColor" stroke-width="2"></circle>
              <path d="M14 13h3c.6 0 1 .4 1 1s-.4 1-1 1h-4c-.6 0-1-.4-1-1V8c0-.6.4-1 1-1s1 .4 1 1v5z"
                    fill="currentColor"></path>
            </svg>

            <span class="quick_text">看过</span></a>
        </div>

        <!-- 上传 -->
        <div class="quick_item quick_upload __lite_hide__">
          <a href="/upload" class="quick_link" _stat="顶部导航区:上传" title="上传">

            <svg class="svg_quick_icon svg_icon_upload" viewBox="0 0 26 26" width="26" height="26">
              <path d="M12 3h2v11c0 .6-.4 1-1 1s-1-.4-1-1V3z" fill="currentColor"></path>
              <path d="M9 7l4-4M17 7l-4-4" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="square"></path>
              <path d="M23 13v7c0 2.2-1.8 4-4 4H7c-2.2 0-4-1.8-4-4v-7" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>

            <span class="quick_text">上传</span></a>
        </div>

        <!-- pc客户端 -->
        <div class="quick_item quick_client __lite_hide__" id="pc_client">
          <a href="javascript:;" _hot="顶部导航区:客户端" class="quick_link" _stat="顶部导航区:客户端">

            <svg class="svg_quick_icon svg_icon_client" viewBox="0 0 26 26" width="26" height="26">
              <path
                d="M15 18v2H7c-2.2 0-4-1.8-4-4V7c0-2.2 1.8-4 4-4h12c2.2 0 4 1.8 4 4v6h-2V7c0-1.1-.9-2-2-2H7c-1.1 0-2 .9-2 2v9c0 1.1.9 2 2 2h8zm0 5v2H9v-2h6zM21 23h2v-6c0-.6-.4-1-1-1s-1 .4-1 1v6z"
                fill="currentColor"></path>
              <path d="M19 21l3 2M25 21l-3 2" fill="none" stroke="currentColor" stroke-width="2"
                    stroke-linecap="square"></path>
            </svg>

          </a>
        </div>

        <div :class="[open_id==0?'quick_item quick_user':'quick_item quick_user open']" id="mod_head_user" @mouseover="open_id=1" >
          <router-link :to="token?'/upload':'/user/login'" class="quick_link _checklogin" id="mod_head_notice_trigger"
                       _stat="顶部导航区:头像" @mouseout="open_id=0">
            <img class="quick_user_avatar" :src="token? avatar:'//puui.qpic.cn/vupload/0/common_avatar.png/0'" data-type="avatar"
                 data-avatarsize="40">
            <span class="account_type" data-type="account_type_logo">
                    <i class="icon icon_qq __account_type_qq none"><svg class="svg_icon svg_icon_qq" viewBox="0 0 20 20"
                                                                        width="8" height="8"><path
                      d="M16.3 13.7c-.3.7-.7 1.3-1.2 1.8 1.1.3.8.9.8.9.5.3.5 2-2.3 2-1.8 0-2.6-.5-2.9-.9H10c-.3 0-.6 0-.9-.1-.3.3-1.1.9-2.9.9-2.7 0-2.7-1.7-2.2-2 0 0-.3-.6 1-.9-.5-.6-.9-1.2-1.2-2-1.1 2-1.7.7-1.6-.9.1-1.4 1.3-2.9 1.6-3.3V9c0-.3.1-.6.4-.9v-.2c0-.3.2-.6.4-.8V7c0-3 2.5-5.5 5.6-5.5S15.7 4 15.7 7v.3c.2.2.3.4.3.6v.2c.2.2.4.5.4.8 0 .2 0 .3-.1.5.3.4 1.5 1.9 1.6 3.3-.1 1.5-.6 2.8-1.6 1z"></path></svg></i>
                    <i class="icon icon_wechat __account_type_wx none"><svg class="svg_icon svg_icon_wechat"
                                                                            viewBox="0 0 20 20" width="8" height="8"><path
                      d="M13.4 7.6h.7c-.6-2.7-3.6-4.8-7.1-4.8-3.9 0-7 2.6-7 6 0 1.9 1.1 3.5 2.8 4.7l-.7 2.1 2.5-1.2c.9.2 1.6.4 2.5.4h.7c-.1-.5-.2-1-.2-1.5-.1-3.2 2.5-5.7 5.8-5.7zM9.7 5.7c.5 0 .9.3.9.9 0 .5-.3.9-.9.9-.5 0-1.1-.4-1.1-.9s.5-.9 1.1-.9zm-5 1.8c-.5 0-1.1-.4-1.1-.9s.5-.9 1.1-.9.9.3.9.9c0 .5-.3.9-.9.9zM19.8 13.1c0-2.8-2.8-5.1-6-5.1-3.3 0-6 2.3-6 5.1s2.6 5.1 6 5.1c.7 0 1.4-.2 2.1-.4l1.9 1.1-.5-1.8c1.5-1 2.5-2.4 2.5-4zm-7.9-.9c-.3 0-.7-.3-.7-.7 0-.3.4-.7.7-.7.5 0 .9.4.9.7 0 .4-.3.7-.9.7zm3.9 0c-.3 0-.7-.3-.7-.7 0-.3.4-.7.7-.7.5 0 .9.4.9.7 0 .4-.4.7-.9.7z"></path></svg></i>
                </span>
            <img src="//puui.qpic.cn/vupload/0/common_blank.png/0" alt="" class="icon_vip_pic none" data-type="viplogo"
                 width="15">
            <i class="triangle_up"><i class="triangle_inner"></i></i>
          </router-link>
          <div class="mod_quick_pop mod_pop_user"  id="mod_head_notice_pop"
               _stat="顶部导航区:头像浮层" @mouseover="open_id=1" @mouseout="open_id=0">
            <div class="pop_info_content quick_pop_user">
              <div class="quick_pop_user_hd">
                <span class="account_type __accout_type_name">账号:</span>
                <a href="https://v.qq.com/biu/u/history/" _stat="顶部导航区:头像浮层:昵称" class="user_name _nickname">无奈之下</a>
                <a href="https://film.qq.com/vip/my/" class="link_vip_icon" _stat="顶部导航区:头像浮层:vipicon">
                  <img src="https://puui.qpic.cn/vupload/0/20190822_0_grey_3x.png/0" alt="" class="icon_vip_pic"
                       data-type="viplogo" width="24">
                </a>
                <a href="javascript:;" class="link_change" data-type="switchlogin" _stat="顶部导航区:头像浮层:切换账号" title="切换账号">切换</a>
                <a href="javascript:;" class="link_quit" data-type="logout" _stat="顶部导航区:头像浮层:退出" title="退出">退出</a>
                <div class="quick_vip_meta" id="quick_user_vip" data-version="3"><span class="vip_now">你的微信<span
                  class="name" title="Jacksonville 😏">Jacksonville 😏</span>是会员</span> <span class="vip_next">	                            <a
                  href="javascript:;" class="btn_em btn_vip_change">切换为微信</a>	                            <a
                  href="javascript:;" class="link_vip __open_vip">为QQ号开通</a>	                            </span></div>
              </div>
              <div class="quick_pop_user_bd">
                <div class="quick_features cf">
                  <a class="feature_item" href="http://v.qq.com/u/comment/" target="_blank"
                     _hot="顶部导航区:头像浮层:user_message" _stat="顶部导航区:头像浮层:user_message">
                    <i class="icon_feature icon_feature_comment"></i>
                    <span class="icon_text" id="nav_user_message">评论消息</span>
                  </a>
                  <a class="feature_item" href="https://v.qq.com/biu/u/history/" target="_blank"
                     _hot="顶部导航区:头像浮层:user_history" _stat="顶部导航区:头像浮层:user_history">
                    <i class="icon_feature icon_feature_cloud"></i>
                    <span class="icon_text">云同步观看记录</span>
                  </a>
                  <a class="feature_item" href="https://v.qq.com/u/wallet/vbshop.html#tab=lottery" target="_blank"
                     _hot="顶部导航区:头像浮层:user_lottery" _stat="顶部导航区:头像浮层:user_lottery">
                    <i class="icon_feature icon_feature_lottery"></i>
                    <span class="icon_text">免费抽奖</span>
                  </a>
                  <a class="feature_item _download_pc" href="javascript:;" _hot="顶部导航区:头像浮层:download"
                     _stat="顶部导航区:头像浮层:download">
                    <i class="icon_feature icon_feature_client"></i>
                    <span class="icon_text">用客户端看抢VIP</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 快捷入口 结束 -->

    </div>

  </div>
</template>

<script>
    export default {
        name: "Head",
        data() {
            return {
                search_word: '热门搜索',
                choice_search: false,
                open_id: 0,
                token: '',
                nickname: '',
                avatar:''
            }
        },
        created(){
          this.token = this.$settings.check_user_login();
          this.User_info()
        },
        methods:{
            User_info(){
                if(this.token){
                    this.nickname = localStorage.getItem('user_nickname') || sessionStorage.getItem('user_nickname')
                    this.avatar = localStorage.getItem('avatar') || sessionStorage.getItem('avatar')
                }
            },
        }
    }
</script>

<style scoped>
  .site_logo {
    position: relative;
    width: 152px;
    margin-top: 16px;
    float: left;
    overflow: hidden;
  }

  .site_logo .link_logo {
    display: block;
    width: 152px;
    height: 36px;
    background: url('../../../static/image/Gdlgxylogo.png') 0 -36px;
    background-size: cover;
    text-indent: -300px;
  }

  .mod_search .search_btn {
    position: absolute;
    top: -1px;
    right: -1px;
    bottom: -1px;
    width: 77px;
    height: 38px;
    padding-right: 6px;
    border: none;
    border-radius: 0 20px 20px 0;
    outline: 0;
    background: #ff5c38;
    color: #fff;
    font-size: 15px;
    line-height: 40px;
    cursor: pointer;
  }
</style>
