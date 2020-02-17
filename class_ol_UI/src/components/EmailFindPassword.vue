<template>

  <div class="login box" style="overflow: auto">
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div id="login_body" style="overflow: auto">
      <div style="width: 525px; float: left;" class="imag_box">
        <div class="login_log">
          <img src="../../static/image/login_logo.png" alt="">
        </div>
        <div class="login_icon">
          <img src="../../static/image/login_icon.png" alt="">
        </div>
      </div>
      <div class="login_box" style="margin: 40px;">
        <div class="login_padding">
          <div class="register-title">
            <p style="display: inline">通过邮箱重置密码</p>
          </div>

          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="50px"
                   class="demo-ruleForm">
            <el-form-item prop="count">
              <el-input v-model="ruleForm.count" placeholder="邮箱" prefix-icon="iconfont ic-email"></el-input>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" id="TencentCaptcha" @click="get_verify" style="width: 100%">登录</el-button>
            </el-form-item>
          </el-form>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'EmailFindPassword',
        data() {

            var checkCount = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error("邮箱不能为空"))
                } else {
                    callback()
                }
            };

            return {
                ruleForm: {
                    count: '',
                },
                rules: {
                    count: [
                        {validator: checkCount, trigger: 'blur'}
                    ],
                }
            };
        },
        methods: {
            get_verify() {
                // 首先从后端获取appId
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
                this.$axios.post(`${this.$settings.Host}/user/verify/`, {
                    'ticket': ticket,
                    'randstr': randstr
                }).then(response => {
                    if (response.status === 200) {
                        // 校验成功, 进行登录,这里调用之前写好的登录方法
                        this.submitForm('ruleForm')
                    } else {
                        this.$message.error("校验失败!")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("校验验证码出错!请联系管理员!")
                })
            },

            goBack() {
                this.$router.push('/')
            },
            submitForm(formName) {
                let self = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        self.$axios.get(`${self.$settings.Host}/user/send_email/`, {
                            params: {email: self.ruleForm.count,}
                        }).then(response => {
                            self.$message.success("邮件发送成功，请注意接收")
                        }).catch(error => {
                            self.$alert("邮箱地址不存在或错误", "广东理工学院");
                            self.ruleForm.count = '';
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
  .demo-ruleForm{
    display: block;
  }
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
    display: inline-block;
    margin: 0 auto 50px;
    padding: 10px;
    font-weight: 400;
    color: #969696;
  }

  #login_box {
    margin: 40px;
    float: left;
    margin-left: 50px;
    margin-right: 125px;
  }

  .login_padding {
    width: 400px;
    margin: 60px auto 0;
    padding: 50px 50px 30px;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 0 8px rgba(0, 0, 0, .1);
    vertical-align: middle;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    flex-direction: column;
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
