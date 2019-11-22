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

</style>
