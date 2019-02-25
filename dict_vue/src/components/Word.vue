<template>
  <div class="container">
    <div class="jumbotron title" >
      <h3>{{$route.params.word}}</h3>
    </div>
    <div class="jumbotron meaning">
      <div>
        <h3 class="text">{{result[0].meaning}}</h3>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Word',
  data: function () {
    return {
      result: ''
    }
  },
  created () {
    axios
      .get('http://127.0.0.1:5000?word=' + this.$route.params.word)
      .then(response => (this.result = response.data.results))
  }

}

</script>

<style scoped>
  .title{
    background-color: dodgerblue;
    padding-top: 10px;
    padding-bottom: 10px;
    margin-left: 0;
    color: white;
    margin-top: 10%;
  }
  .meaning{
    background-color: white;
    margin:0;
    pading:0;
   color: dodgerblue;
    border: 2px;
    border-style:solid;
    margin-top: -38px;

  }
  .text{
    padding: 0;
    margin: 0;
    color: blue;
  }

</style>
