<template>

  <div class="login box" style="overflow: auto">
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div id="login_body" style="overflow: auto">
      <!--      <div style="background: url('/static/image/fj_2.jpg'); float: left; background-size: 100% 100%">-->
      <div style="width: 525px; float: left;" class="imag_box">
        <div class="login_log">
          <img src="../../static/image/login_logo.png" alt="">
        </div>
        <div class="login_icon">
          <img src="../../static/image/login_icon.png" alt="">
        </div>
      </div>

      <!--      </div>-->
      <div id="login_box">
        <div style="height: 20px">
          <!--          <img src="/static/image/Gdlgxylogo.png" alt=""-->
          <!--               style="width: 300px ;padding: 0 auto;display: block;margin: 0 auto">-->
        </div>
        <div class="login_padding" style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);background: white">
          <div class="register-title" style="text-decoration: none; margin-left: 20px">
            <p style="display: inline" @click="ruleForm.status=1" :class="ruleForm.status===1?'active':''">用户登录</p>
            <p style="display: inline"> | </p>
            <p style="display: inline" @click="ruleForm.status=2" :class="ruleForm.status===2?'active':''">短信登录</p>
          </div>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="50px"
                   class="demo-ruleForm" v-if="ruleForm.status===1">
            <el-form-item prop="count">
              <el-input v-model="ruleForm.count" placeholder="用户名/手机号/邮箱" prefix-icon="iconfont ic-user"></el-input>
            </el-form-item>
            <el-form-item prop="pass">
              <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="密码"
                        prefix-icon="iconfont ic-password">
              </el-input>
            </el-form-item>
            <div id="geetest1"></div>
            <div class="rember">
              <p>
                <input type="checkbox" class="no" v-model="ruleForm.save_pass"/>
                <span>记住密码</span>
              </p>
              <div>
                <p data-toggle="dropdown" id="dropdownMenu1">忘记密码</p>
                <ul class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenu1" style="top: 33px">
                  <li>
                    <router-link to="/user/phone/reset_password">用手机号重置密码</router-link>
                  </li>
                  <li>
                    <router-link to="/user/email/find_password">用邮箱重置密码</router-link>
                  </li>
                  <li><a target="_blank" href="/p/9058d0b8711d">无法用海外手机号登录</a></li>
                  <li><a target="_blank" href="/p/498a9fa7da08">无法用 Google 帐号登录</a></li>
                </ul>
              </div>
            </div>
            <el-form-item>
              <el-button type="primary" id="TencentCaptcha" @click="get_verify" style="width: 100%">登录</el-button>
            </el-form-item>
            <p class="go_login">没有账号
              <router-link to="/user/register">立即注册</router-link>
            </p>
          </el-form>

          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="50px"
                   class="demo-ruleForm" v-if="ruleForm.status===2">
            <el-form-item prop="mobile">
              <el-input v-model="ruleForm.mobile" placeholder="手机号" prefix-icon="iconfont ic-phone"></el-input>
            </el-form-item>
            <el-form-item prop="sms">
              <el-input v-model="ruleForm.sms" placeholder="请输入短信" prefix-icon="iconfont ic-verify">
                <template slot="append"><span @click="sendSMS" :style="ruleForm.sms_status?'pointer-events:none':''"><i>{{ruleForm.sms_title}}</i></span>
                </template>
              </el-input>
            </el-form-item>
            <div id="geetest2"></div>
            <el-form-item>
              <el-button type="primary" id="TencentCaptcha1" @click="get_verify1" style="width: 100%">登录</el-button>
            </el-form-item>
            <p class="go_login">没有账号
              <router-link to="/user/register">立即注册</router-link>
            </p>
          </el-form>

          <div class="more-sign">
            <h6>社交帐号登录</h6>
            <ul>
              <li id="weibo-link-wrap" class="">
                <a class="weibo" id="weibo-link">
                  <i class="iconfont ic-weibo"></i>
                </a>
              </li>
              <li><a id="weixin" class="weixin" target="_blank" href=""><i class="iconfont ic-wechat"></i></a></li>
              <li><a id="qq" class="qq" target="_blank" @click.prevent="login_qq"><i class="iconfont ic-qq_connect"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {
            var validateSms = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error("手机号不能为空"))
                } else {
                    callback()
                }
            };

            var validateMobile = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error("短信不能为空"))
                } else {
                    callback()
                }
            };

            var checkCount = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error("用户名/手机号不能为空"))
                } else {
                    callback()
                }
            };

            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    callback()
                }
            };
            return {
                ruleForm: {
                    pass: '',
                    count: '',
                    save_pass: false,
                    login_main: true,
                    sms_title: "发送短信",
                    sms_status: false,
                    sms: '',
                    mobile: '',
                    status: 1,
                },
                rules: {
                    count: [
                        {validator: checkCount, trigger: 'blur'}
                    ],
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    sms: [
                        {validator: validateSms, trigger: 'blur'}
                    ],
                    mobile: [
                        {validator: validateMobile, trigger: 'blur'}
                    ],

                }
            };
        },
        methods: {
            login_qq() {
                this.$axios.get(`${this.$settings.Host}/oauth/QQ_login/`, {}).then(response => {
                    location.href = response.data
                }).catch(error => {
                    console.log(error.response);
                    this.$message.error("网络超时，请重新刷新页面")
                })
            },
            get_verify1() {
                // 首先从后端获取appId
                this.$axios.get(`${this.$settings.Host}/user/verify/`).then(
                    response => {
                        // 拿到了appId,构建验证码对象
                        let appId = response.data;
                        let self = this;
                        // 这里其实是给这个元素绑定了一个事件
                        let tct = new TencentCaptcha(document.getElementById("TencentCaptcha1"),
                            appId, function (res) {
                                // 验证码的回调函数
                                if (res.ret === 0) {
                                    // 票据
                                    let ticket = res.ticket;
                                    let randstr = res.randstr;
                                    self.check_verify1(ticket, randstr)
                                }
                            }
                        );
                        // 显示验证码
                        tct.show()
                    }
                ).catch(error => {
                    this.$message.error("获取验证码出错!请联系管理员!!!!!")
                })
            },

            check_verify1(ticket, randstr) {
                // 将ticket,randstr发送到后端进行验证
                this.$axios.post(`${this.$settings.Host}/user/verify/`, {
                    'ticket': ticket,
                    'randstr': randstr
                }).then(response => {
                    if (response.status === 200) {
                        // 校验成功, 进行登录,这里调用之前写好的登录方法
                        this.submitForm1('ruleForm')
                    } else {
                        this.$message.error("校验失败!")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("校验验证码出错!请联系管理员!")
                })
            },

            get_verify() {
                // 首先从后端获取appId
                console.log(this.$settings.Host);
                this.$axios.get(`${this.$settings.Host}/user/verify/`).then(
                    response => {
                        // 拿到了appId,构建验证码对象
                        let appId = response.data;
                        let self = this;
                        // 这里其实是给这个元素绑定了一个事件
                        let tct = new TencentCaptcha(document.getElementById("TencentCaptcha"),
                            appId, function (res) {
                                // 验证码的回调函数
                                if (res.ret === 0) {
                                    // 票据
                                    let ticket = res.ticket;
                                    let randstr = res.randstr;
                                    self.check_verify(ticket, randstr)
                                }
                            }
                        );
                        // 显示验证码
                        tct.show()
                    }
                ).catch(error => {
                    this.$message.error("获取验证码出错!请联系管理员!!!!!")
                })
            },

            check_verify(ticket, randstr) {
                // 将ticket,randstr发送到后端进行验证
                console.log("发送ajax成功~~~~");
                this.$axios.post(`${this.$settings.Host}/user/verify/`, {
                    'ticket': ticket,
                    'randstr': randstr
                }).then(response => {
                    if (response.status === 200) {
                        // 校验成功, 进行登录,这里调用之前写好的登录方法
                        console.log("校验成功~~")
                        this.submitForm('ruleForm')
                    } else {
                        this.$message.error("校验失败!")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("校验验证码出错!请联系管理员!")
                })
            },

            sendSMS() {
                this.$axios.get(`${this.$settings.Host}/user/login/mobile/${this.ruleForm.mobile}`).then(response => {
                    this.$message(response.data);
                    let num = 60;
                    let self = this;
                    var test = setInterval(function () {
                        if (num > 0) {
                            self.ruleForm.sms_title = `${num}秒后可以重试`;
                            self.ruleForm.sms_status = true;
                            num--;
                        } else {
                            self.ruleForm.sms_title = "发送短信";
                            self.ruleForm.sms_status = false;
                            clearInterval(test)
                        }
                    }, 1000)
                }).catch(error => {
                    this.$alert("网络错误！请联系客服工作人员", "广东理工学院")
                })
            },


            goBack() {
                this.$router.push('/')
            },
            submitForm(formName) {
                let self = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        self.$axios.post(`${self.$settings.Host}/user/login/`, {
                            username: self.ruleForm.count,
                            password: self.ruleForm.pass
                        }).then(response => {

                            if (self.ruleForm.save_pass) {
                                sessionStorage.removeItem('user_token');
                                sessionStorage.removeItem('user_id');
                                sessionStorage.removeItem('user_name');
                                localStorage.setItem('user_token', response.data.token);
                                localStorage.setItem('user_id', response.data.id);
                                localStorage.setItem('user_name', response.data.username);
                            } else {
                                console.log('不保存密码！~~~ ',response.data);
                                localStorage.removeItem('user_token');
                                localStorage.removeItem('user_id');
                                localStorage.removeItem('user_name');
                                sessionStorage.setItem('user_token', response.data.token);
                                sessionStorage.setItem('user_id', response.data.id);
                                sessionStorage.setItem('user_name', response.data.username);
                            }
                            self.$router.go(-1);
                        }).catch(error => {
                            self.$alert("账号或密码错误", "广东理工学院");
                            self.ruleForm.pass = '';
                        })
                    } else {
                        return false;
                    }
                });
            },


            submitForm1(formName) {
                let self = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        console.log(self.ruleForm.mobile);
                        console.log(self.ruleForm.sms);

                        self.$axios.post(`${self.$settings.Host}/user/login/mobile/`, {
                            mobile: self.ruleForm.mobile,
                            sms: self.ruleForm.sms
                        }).then(response => {
                            if (self.ruleForm.save_pass) {
                                sessionStorage.removeItem('user_token');
                                sessionStorage.removeItem('user_id');
                                sessionStorage.removeItem('user_name');
                                localStorage.setItem('user_token', response.data.token);
                                localStorage.setItem('user_id', response.data.id);
                                localStorage.setItem('user_name', response.data.username);
                            } else {
                                localStorage.removeItem('user_token');
                                localStorage.removeItem('user_id');
                                localStorage.removeItem('user_name');
                                sessionStorage.setItem('user_token', response.data.token);
                                sessionStorage.setItem('user_id', response.data.id);
                                sessionStorage.setItem('user_name', response.data.username);
                            }
                            self.$router.go(-1);
                        }).catch(error => {
                            self.$alert("账号或密码错误", "广东理工学院");
                            self.ruleForm.sms = '';
                        })
                    } else {
                        return false;
                    }
                });
            },

            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>
  .login_log img {
    float: left;
    width: 88%;
    margin: 40px;
    margin-left: 160px;
  }

  .login_icon img {
    float: left;
    width: 88%;
    margin: 20px;
    margin-top: 10px;
    margin-left: 200px;
  }

  .imag_box {
    width: 525px;
    float: left;
    margin-right: 241px;
  }

  #login_body {
    background-image: url("../../static/image/login_bg.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .register-title {
    width: 100%;
    font-size: 24px;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #4a4a4a;
    letter-spacing: .39px;
  }

  #login_box {
    margin: 40px;
    float: left;
    margin-left: 50px;
    margin-right: 125px;
  }

  .login_padding {
    padding-left: 0;
    padding-top: 0;
    padding-right: 30px;
    padding-bottom: 25px;
  }

  .rember {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
  }

  .rember p:first-of-type {
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 55px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
  }

  .rember p:nth-of-type(2) {
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
  }

  .rember input {
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
  }

  .rember p span {
    display: inline-block;
    font-size: 12px;
    width: 100px;
    /*position: absolute;*/
    /*left: 20px;*/

  }

  .go_login {
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 0;
    margin-left: 40px;
  }

  .go_login span {
    color: #84cc39;
    cursor: pointer;
  }

  .more-sign {
    text-align: center;
    margin-top: 10px;
    margin-left: 40px;
  }

  .more-sign h6 {
    position: relative;
    margin: 0 0 10px;
    font-size: 12px;
    color: #b5b5b5
  }

  .more-sign h6:before {
    left: 30px
  }

  .more-sign h6:after, .more-sign h6:before {
    content: "";
    border-top: 1px solid #b5b5b5;
    display: block;
    position: absolute;
    width: 60px;
    top: 5px
  }

  .more-sign h6:after {
    right: 30px
  }

  .more-sign ul {
    margin-bottom: 10px;
    list-style: none
  }

  .more-sign ul li {
    margin: 0 5px;
    display: inline-block
  }

  .more-sign ul a {
    width: 50px;
    height: 50px;
    line-height: 50px;
    display: block
  }

  .more-sign ul i {
    font-size: 28px
  }

  .more-sign .ic-weibo {
    color: #e05244
  }

  .more-sign .ic-wechat {
    color: #00bb29
  }

  .more-sign .ic-qq_connect {
    color: #498ad5
  }

  .more-sign .ic-douban {
    color: #00820f
  }

  .more-sign .ic-more {
    color: #999
  }

  .more-sign .weibo-loading {
    pointer-events: none;
    cursor: pointer;
    position: relative
  }

  .more-sign .weibo-loading:after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: #fff
  }

  .more-sign .weibo-loading:after {
    background-color: #3f3f3f
  }

  .more-sign .weibo-loading:before {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin: -10px 0 0 -10px;
    border-radius: 10px;
    border: 2px solid #e05244;
    border-bottom-color: transparent;
    vertical-align: middle;
    -webkit-animation: rolling .8s infinite linear;
    animation: rolling .8s infinite linear;
    z-index: 1
  }

  .active {
    font-weight: 700;
    color: #ea6f5a;
    border-bottom: 2px solid #ea6f5a
  }


</style>
