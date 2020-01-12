<template>
  <div>
    <!--    <Header></Header>-->
    <Head></Head>
    <!--    <banner></banner>-->
    <NewHead></NewHead>
<!--    <Timer></Timer>-->
    <Hostdoor></Hostdoor>
    <Care></Care>
    <Footer></Footer>
  </div>
</template>


<script>
    import Care from "./common/Care";
    import Header from "./common/Header";
    import NewHead from "./common/NewHead";
    import banner from "./common/banner";
    import Timer from "./common/Timer";
    import Footer from "./common/Footer";
    import Head from "./common/Head";
    import Hostdoor from "./common/Hostdoor";

    export default {
        name: "Home",
        components: {
            // Header,
            Head,
            NewHead,
            banner,
            Care,
            // Timer,
            Footer,
            Hostdoor
        }
    }
</script>

<style>

</style>
