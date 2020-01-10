// 引入路由类和Vue类
import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Aliplayer from "../components/Aliplayer";
import Login from "../components/Login";
import Register from "../components/Register";
import IT_Course from "../components/IT_Course";
import Cart from "../components/Cart";
import Detail from "../components/Detail";
import PhoneSetPassword from "../components/PhoneSetPassword";
import EmailFindPassword from "../components/EmailFindPassword";
import EmailSetPassword from "../components/EmailSetPassword";
import QQCallBack from "../components/QQCallBack";
// import Head from "../components/common/Head";
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
      name : 'Aliplayer',
      path : '/aliplayer/:d',
      component : Aliplayer,
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
    {
      name : "IT_Course",
      path : "/course/:id",
      component : IT_Course
    },
    {
      name : "Cart",
      path : "/cart",
      component : Cart
    },
    {
      name : "Detail",
      path : "/course/detail/:id",
      component : Detail
    },
    {
      name : "PhoneSetPassword",
      component : PhoneSetPassword,
      path : "/user/phone/reset_password",
    },
    {
      name : "EmailFindPassword",
      component : EmailFindPassword,
      path : "/user/email/find_password",
    },
    {
      name : "EmailSetPassword",
      component : EmailSetPassword,
      path : "/reset_password",
    },
    {
      name : "QQCallBack",
      component : QQCallBack,
      path : "/qq_callback",
    },


  ]
})
