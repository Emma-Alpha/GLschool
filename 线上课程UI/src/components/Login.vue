<template>

  <div class="login box">
    <link rel="stylesheet" href="/static/bootstrap/bootstrap-3.3.7-dist的副本/css/bootstrap.css">
    <div>
      <el-page-header @back="goBack" content="登录页面" style="width: 100%; padding: 20px; ">
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
          <div class="register-title" style="text-decoration: none">用户登录</div>
          <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                   class="demo-ruleForm">
            <el-form-item  prop="count" >
              <el-input v-model="ruleForm.count" placeholder="用户名/手机号"></el-input>
            </el-form-item>
            <el-form-item  prop="pass">
              <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="密码">
              </el-input>
            </el-form-item>
            <div id="geetest1"></div>
            <div class="rember">
              <p>
                <input type="checkbox" class="no" />
                <span>记住密码</span>
              </p>
              <p>忘记密码</p>
            </div>
            <el-form-item>
              <el-button type="primary" @click="submitForm('ruleForm')" style="width: 100%">登录</el-button>
            </el-form-item>
            <p class="go_login">没有账号 <span>立即注册</span></p>
          </el-form>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: 'Login',
        data() {

            var checkCount = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error("用户名/手机号不能为空"))
                }
            };

            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                }
            };
            return {
                ruleForm: {
                    pass: '',
                    count: '',

                },
                rules: {
                    count: [
                        {validator: checkCount, trigger: 'blur'}
                    ],
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],

                }
            };
        },
        methods: {
            goBack() {
                this.$router.push('/')
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert('submit!');
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
    width: 380px;
    float: right;
  }

  .login_padding {
    padding-left: 0;
    padding-top: 0;
    padding-right: 50px;
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

  .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
  }
  .go_login span{
    color: #84cc39;
    cursor: pointer;
  }
  .el-form-item .el-form-item__content {
  margin-left: 50px!important;
}
</style>
