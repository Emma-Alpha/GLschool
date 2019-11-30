<template>

  <div class="login box">
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div>
      <el-page-header @back="goBack" content="注册页面" style="width: 100%; padding: 20px; ">
      </el-page-header>
    </div>
    <div class="jumbotron" style="height: 800px; padding-top:0; ">
      <!--      <div style="background: url('/static/image/fj_2.jpg'); float: left; background-size: 100% 100%">-->
      <div style="float: left ; margin: 30px; ">

        <p></p>
        <h1 style="display: inline">Welcome to Guangdong </h1>
        <h2>Science and Engineering College</h2>
        <h1 style="display: inline">欢迎</h1>
        <h2 style="display: inline">来到</h2>
        <p></p>
        <h1 style="display: inline">广东理工学院</h1>
      </div>
      <!--      </div>-->
      <div class="login_box" style="margin: 40px;">
        <div>
          <img src="/static/image/Gdlgxylogo.png" alt=""
               style="width: 300px ;padding: 0 auto;display: block;margin: 0 auto">
        </div>
        <div class="login_padding" style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);background: white">
          <div class="register-title" style="text-decoration: none">用户注册</div>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                   class="demo-ruleForm">
            <el-form-item label="账号" prop="mobile">
              <el-input v-model.number="ruleForm.mobile" placeholder="手机号"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
              <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="密码"
                        show-password></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
              <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"
                        placeholder="请确认密码" show-password></el-input>
            </el-form-item>
            <el-form-item label="短信" prop="sms">
              <el-input v-model="ruleForm.sms" placeholder="请输入短信">
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
                    if (!Number.isInteger(value)) {
                        callback(new Error('请输入数字值'));
                    } else {
                        if (value > 999999 || value < 999) {
                            callback(new Error('短信格式4-6位'));
                        } else {

                            callback();
                        }
                    }
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
                            if(num>0){
                            self.ruleForm.sms_title = `${num}秒后可以重试`;
                            self.ruleForm.sms_status = true;
                            num--;
                            }else{
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
                            sessionStorage.setItem('user_token',response.data.token);
                            sessionStorage.setItem('user_id',response.data.id);
                            sessionStorage.setItem('user_name',response.data.username);
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

  .login_box {
    width: 400px;
    float: right;
  }

  .login_padding {
    padding-left: 0;
    padding-top: 0;
    padding-right: 30px;
    padding-bottom: 25px;
  }
</style>
