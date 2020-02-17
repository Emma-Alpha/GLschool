<template>
  <div>
    <Head></Head>
    <NewHead></NewHead>
    <Hostdoor></Hostdoor>
    <Ranking_List></Ranking_List>
    <yunwei_Ranking_list></yunwei_Ranking_list>
    <Footer></Footer>

  </div>
</template>


<script>
    import Ranking_List from "./common/Ranking_List";
    import NewHead from "./common/NewHead";
    import Footer from "./common/Footer";
    import Head from "./common/Head";
    import Hostdoor from "./common/Hostdoor";
    import Yunwei_Ranking_list from "./common/Yunwei_Ranking_list";

    export default {
        name: "Home",
        components: {
            Head,
            NewHead,
            Ranking_List,
            Footer,
            Hostdoor,
            Yunwei_Ranking_list
        }
    }
</script>

<style>

</style>
