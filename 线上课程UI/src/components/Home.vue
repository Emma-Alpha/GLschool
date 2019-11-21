<template>
  <div>
    <Header></Header>
    <banner></banner>
    <Timer></Timer>
    <Care></Care>
    <Footer></Footer>
  </div>
</template>


<script>
  import Care from "./common/Care";
  import Header from "./common/Header";
  import banner from "./common/banner";
  import Timer from "./common/Timer";
  import Footer from "./common/Footer";
    export default {
        name: "Home",
        components : {
            Header,
            banner,
            Care,
            Timer,
            Footer
        }
    }
</script>

<style >
/* 声明全局样式和项目的初始化样式 */
body,h1,h2,h3,h4,p,table,tr,td,ul,li,a,form,input,select,option,textarea{
  margin:0;
  padding: 0;
  font-size: 15px;
}
a{
  text-decoration: none;
  color: #333;
}
ul,li{
  list-style: none;
}
table{
  border-collapse: collapse; /* 合并边框 */
}

/* 工具的全局样式 */
.full-left{
  float: left!important;
}
.full-right{
  float: right!important;
}
</style>
