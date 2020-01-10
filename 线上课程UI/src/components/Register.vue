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
      <div class="login_box" style="margin: 40px;">
        <div class="login_padding" style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);background: white">
          <div class="register-title" style="text-decoration: none">用户注册</div>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="50px"
                   class="demo-ruleForm">
            <el-form-item  prop="mobile">
              <el-input v-model.number="ruleForm.mobile" placeholder="手机号" prefix-icon="iconfont ic-phone"></el-input>
            </el-form-item>
            <el-form-item  prop="pass">
              <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="密码" prefix-icon="iconfont ic-password"
                        show-password></el-input>
            </el-form-item>
            <el-form-item prop="checkPass">
              <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off" prefix-icon="iconfont ic-password"
                        placeholder="请确认密码" show-password></el-input>
            </el-form-item>
            <el-form-item  prop="sms">
              <el-input v-model="ruleForm.sms" type="text" placeholder="请输入短信" prefix-icon="iconfont ic-verify">
                <template slot="append"><span @click="sendSMS" :style="ruleForm.sms_status?'pointer-events:none':''"><i>{{ruleForm.sms_title}}</i></span>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item>
              <!--              <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>-->
              <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
              <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
          </el-form>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Register',
        data() {
            let self = this;
            var checkMobile = (rule, value, callback) => {
                if (!value) {
                    callback(new Error("手机号不能为空"));
                    self.ruleForm.sms_status = true
                }
                setTimeout(() => {

                    if (!Number.isInteger(value)) {
                        callback(new Error('请输入数字值'));
                        self.ruleForm.sms_status = true
                    } else {
                        let re = /1[3-9]\d{9}/.test(value);
                        if (!re) {
                            callback(new Error("手机格式不对"));
                            self.ruleForm.sms_status = true
                        } else {
                            self.checkMobile(callback);
                            self.ruleForm.sms_status = false
                        }
                    }
                })
            };

            var checkSms = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('短信不能为空'));
                }
                setTimeout(() => {
                    callback()
                }, 1000);
            };
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    if (this.ruleForm.checkPass !== '') {
                        this.$refs.ruleForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.pass) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                ruleForm: {
                    pass: '',
                    checkPass: '',
                    sms: '',
                    mobile: '',
                    mobile_status: false,
                    sms_title: "发送短信",
                    sms_status: false,
                },
                rules: {
                    mobile: [
                        {validator: checkMobile, trigger: 'blur'}
                    ],
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {validator: validatePass2, trigger: 'blur'}
                    ],
                    sms: [
                        {validator: checkSms, trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            // 发送短信
            sendSMS() {
                this.$axios.get(`${this.$settings.Host}/user/sms/${this.ruleForm.mobile}`).then(response => {
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


            // 发送ajax去检查手机号码的唯一性
            checkMobile(callback) {
                this.$axios.get(`${this.$settings.Host}/user/mobile/${this.ruleForm.mobile}/`).then(response => {
                    let ret = response.data.status;
                    if (ret) {
                        callback()
                    } else {
                        callback(new Error("该手机号码已经被注册了！"))
                    }
                }).catch(error => {
                    this.$alert("网络错误，请刷新页面重试！", "广东理工学院")
                })
            },

            goBack() {
                this.$router.push('/')
            },
            submitForm(formName) {
                let self = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        self.$axios.post(`${self.$settings.Host}/user/`, {
                            mobile: self.ruleForm.mobile,
                            password: self.ruleForm.pass,
                            sms_code: self.ruleForm.sms
                        }).then(response => {
                            self.$alert("注册成功！欢迎", "广东理工学院");
                            localStorage.removeItem("user_token");
                            localStorage.removeItem("user_id");
                            localStorage.removeItem("user_name");
                            sessionStorage.setItem('user_token', response.data.token);
                            sessionStorage.setItem('user_id', response.data.id);
                            sessionStorage.setItem('user_name', response.data.username);
                            self.$router.push("/")
                        }).catch(error => {
                            console.log(error.response.data);
                            self.$message(error.response.data)
                        })
                    } else {
                        console.log('error submit!!');
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
  .register-title {
    width: 100%;
    font-size: 24px;
    text-align: center;
    padding-top: 30px;
    padding-bottom: 30px;
    color: #4a4a4a;
    letter-spacing: .39px;
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
