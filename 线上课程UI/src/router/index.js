// 引入路由类和Vue类
import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Video from "../components/Video";
import Login from "../components/Login";
import Register from "../components/Register";

// 注册路由类
Vue.use(Router);


// 初始化路由对象
export default new Router({
  // 设置路由模式为'history',去掉默认的#
  mode : "history",
  routes : [
    // 路由列表
    {  // 一个字典,代表一条url
      name : 'Home',  // name: "路由别名"
      path: '/', // path:"路由地址"
      component: Home,  // component:组件类名
    },
    {  // 一个字典,代表一条url
      name : 'Home',  // name: "路由别名"
      path: '/home', // path:"路由地址"
      component: Home,  // component:组件类名
    },
    {
      name : 'Video',
      path : '/video/:d',
      component : Video,
    },
    {
      name : "Login",
      path : "/user/login",
      component : Login
    },
    {
      name : "Register",
      path : "/user/register",
      component : Register
    },
  ]
})
