<template>
  <div class="header">
    <div class="content_box">
      <div class="content">
        <div class="logo full-left">
          <img src="/static/image/Gdlgxylogo.png" id="logo_img" alt="">
        </div>
        <ul class="nav full-left">
          <li>
            <el-dropdown>
              <span class="el-dropdown-link" >
                学院介绍<i class="el-icon-arrow-down el-icon--right"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item >学校简介</el-dropdown-item>
                <el-dropdown-item >校训与办学理念</el-dropdown-item>
                <el-dropdown-item >发展历程</el-dropdown-item>
                <el-dropdown-item >学院领导</el-dropdown-item>
                <el-dropdown-item >领导关怀</el-dropdown-item>
                <el-dropdown-item >奖状荣誉</el-dropdown-item>
                <el-dropdown-item >校园风光</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </li>
          <li><span>轻课</span></li>
          <li><span>学位课</span></li>
          <li><span>题库</span></li>
          <li><span>知识座谈会</span></li>
        </ul>
        <div class="login-bar full-right">
          <div class="shop-cart full-left">
            <img src="/static/image/cart.svg" alt="">
            <span>购物车</span>
          </div>
          <div class="login-box full-left">
            <span>登录</span>
            &nbsp;|&nbsp;
            <span>注册</span>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
    export default {
        name: "Header",
        data() {
            return {
                activeName: 'second',
                T:false
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
        }
    }
</script>

<style scoped>

  #xuanxiang {
    display: inline-block;
    margin-top: 20px;
    height: 80px;
  }

  .header {
    height: 80px;
  }

  .content_box {
    width: 100%;
    height: 80px;
    position: fixed;
    z-index: 3;
    background-color: #fff;
    box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
  }

  .header .content {
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
  }

  .header .content .logo {
    height: 80px;
    line-height: 80px;
    margin-right: 50px;
    cursor: pointer; /* 设置光标的形状为爪子 */
  }

  .header .content .logo img {
    vertical-align: middle;
  }

  .header .nav li {
    float: left;
    height: 80px;
    line-height: 80px;
    margin-right: 30px;
    font-size: 16px;
    color: #4a4a4a;
    cursor: pointer;
  }

  .header .nav li span {
    padding-bottom: 16px;
    padding-left: 5px;
    padding-right: 5px;
  }

  .header .nav li:hover span {
    color: #000;
  }

  .header .login-bar {
    height: 80px;
  }

  .header .login-bar .shop-cart {
    margin-right: 20px;
    border-radius: 17px;
    background: #f7f7f7;
    cursor: pointer;
    font-size: 14px;
    height: 28px;
    width: 88px;
    margin-top: 30px;
    line-height: 32px;
    text-align: center;
  }

  #logo_img {
    width: 300px;
  }

  .header .login-bar .shop-cart:hover {
    background: #f0f0f0;
  }

  .header .login-bar .shop-cart img {
    width: 15px;
    margin-right: 4px;
    margin-left: 6px;
  }

  .header .login-bar .shop-cart span {
    margin-right: 6px;
  }

  .header .login-bar .login-box {
    margin-top: 33px;
  }

  .header .login-bar .login-box span {
    color: #4a4a4a;
    cursor: pointer;
  }

  .header .login-bar .login-box span:hover {
    color: #000000;
  }
  .el-dropdown-link {
    cursor: pointer;
    /*color: #409EFF;*/
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }

</style>
