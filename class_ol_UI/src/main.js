// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'  // 注册路由路径
// 导入gt极验证
import '../static/js/tx.js'
// 全局变量和全局方法
import settings from "./settings";
import axios from 'axios';  // 从node_modules目录中导入包
import VideoPlayer from 'vue-video-player'

// 设置全局样式

import '../static/css/reset.css'
import '../static/css/tengxun.css'
import '../static/css/iconfont.eot'
import '../static/css/iconfont.css'

import jQuery from 'jquery/dist/jquery'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap'


// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false;

Vue.prototype.$axios = axios;


Vue.prototype.$settings = settings;


Vue.use(VideoPlayer);
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');

import VueWechatTitle from 'vue-wechat-title'
Vue.use(VueWechatTitle)

// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import VueVideoPlayer from 'vue-aliplayer';
Vue.use(VueVideoPlayer);

// 调用插件
Vue.use(ElementUI);

import VueAliplayerV2 from 'vue-aliplayer-v2';

Vue.use(VueAliplayerV2);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,  // 注册路由规则对象相当于router:router
  components: {App},
  template: '<App/>'
});
