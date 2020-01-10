<template>

  <div class="login box">
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
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
          <div class="register-title" style="text-decoration: none"><p style="display: inline">通过邮箱重置密码</p></div>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                   class="demo-ruleForm">
            <el-form-item label="账号" prop="mobile">
              <el-input v-model="ruleForm.email" placeholder="邮箱" readonly></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
              <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="密码"
                        show-password></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
              <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"
                        placeholder="请确认密码" show-password></el-input>
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
        name: 'PhoneSetPassword',
        data() {
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
                    console.log(value);
                    console.log(this.ruleForm.pass);
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                ruleForm: {
                    email: '',
                    pass: '',
                    checkPass: '',
                },
                rules: {
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {validator: validatePass2, trigger: 'blur'}
                    ],

                }
            };
        },
        created(){
          this.get_email()
        },

        methods: {
            get_email(){
              // 获取邮箱地址
                this.$axios.put(`${this.$settings.Host}/user/send_email/`,{
                    access_token: this.$route.query.access_token
                }).then(response=>{
                    this.ruleForm.email = response.data;
                    console.log(response.data)
                }).catch(error=>{
                    console.log(error.response);
                    this.$message.error("获取邮箱地址失败!!!!")
                })
            },



            // 发送ajax去检查手机号码的唯一性
            checkMobile(callback) {
                this.$axios.get(`${this.$settings.Host}/user/mobile/${this.ruleForm.mobile}/`).then(response => {
                    let ret = response.data.status;
                    if (ret) {
                        callback(new Error("手机号码不存在！！！！"))
                    } else {
                        callback()
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
                        self.$axios.post(`${self.$settings.Host}/user/send_email/`, {
                            access_token : this.$route.query.access_token,
                            password: this.ruleForm.pass,
                            password2: this.ruleForm.checkPass
                        }).then(response => {
                            self.$alert("重置密码成功！欢迎", "广东理工学院");
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
