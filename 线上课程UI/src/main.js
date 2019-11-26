// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router/index'  // 注册路由路径

// 设置全局样式
import '../static/css/reset.css'

import axios from 'axios';  // 从node_modules目录中导入包
// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false;

Vue.prototype.$axios = axios;

// 全局变量和全局方法
import settings from "./settings";
Vue.prototype.$settings = settings;

// 导入gt极验证
import '../static/js/gt.js'

import VideoPlayer from 'vue-video-player'
Vue.use(VideoPlayer);
require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');


// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 调用插件
Vue.use(ElementUI);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,  // 注册路由规则对象相当于router:router
  components: { App },
  template: '<App/>'
})
