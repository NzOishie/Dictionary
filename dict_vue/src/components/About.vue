<template xmlns:by="http://www.w3.org/1999/xhtml">
   <div class="container">
     <div class="jumbotron about" >
      <p class="black">This is a dictionary made with Scrapy, Flask Restful and Vue.js</p>
       <p class="black">The data is scraped from <a class="dblue" href="http://www.english-bangla.com/browse/index/a">here.</a></p>
       <br><br>
       <b class="black"> Developed by: </b> <span class="blue">  Naz Zarreen Oishie </span>
     </div>
   </div>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style scoped>
  .about{
    background-color: white;
    color: dodgerblue;
    border: 2px solid;
    margin: 10% 0 0;

  }
  .blue{
    color: blue;
  }
  .black{
    color: black;
  }
  .dblue{
    color:dodgerblue;
  }
</style>
