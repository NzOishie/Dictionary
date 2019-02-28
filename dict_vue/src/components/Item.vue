<template>
  <div class="home">
    <div class="container">
      <div class="jumbotron title" >
        <h5>Search for a word</h5>
      </div>
     <div>
       <div>
         <input class="form-control search-bar" type="text" v-on:keyup="fetchData" v-model="search" placeholder="Type Here.." >
       </div>
     </div>

      <div v-if="search != null" v-for="i in info" v-bind:key="i.word">
        <ul class="list-group">
          <li   class="list-group-item" v-bind:word="i.word" v-bind:meaning="i.meaning" v-on:click="showWord(i.word)"> {{i.word}}
          <br> {{i.meaning}}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Item',
  data: function () {
    return {
      info: [],
      search: '',
      show: false
    }
  },
  methods: {
    showWord (e) {
      this.show = !this.show
      this.$router.push('/word/' + e)
    },
    fetchData () {
      axios
        .get('http://127.0.0.1:5000?word=' + this.search)
        .then(response => (this.info = response.data.results))
    }
  }
}
</script>

 <style scoped>

   li:hover {
     background: dodgerblue;
     color: white;}
   .title{
     background-color: dodgerblue;
     padding-top: 9px;
     padding-bottom: 9px;
     margin-top: 10%;
     color: white;
   }
   .search-bar{
     width: 100%;
     padding-bottom: 20px;
     margin-top: -35px;
     height: 60px;
   }
   ::placeholder {
     padding-left: 45%;

   }

 </style>
