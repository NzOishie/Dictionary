<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <div class="container">
        <b-navbar-brand href="/">Dictionary</b-navbar-brand>

        <b-navbar-toggle target="nav_collapse" />

        <b-collapse is-nav id="nav_collapse">
          <b-navbar-nav>
            <b-nav-item href="/">Home</b-nav-item>
            <b-nav-item href="#/about">About</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
    <router-view></router-view>
    <p class="qoute">"I was reading	the dictionary. I thought
      it was a poem about everything."
      --Steven Wright</p>
  </div>
</template>

<script>
import Item from './components/Item'
import Word from './components/Word'
import About from './components/About'
export default {
  name: 'App',
  components: {Item, Word, About}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.qoute{
  color: darkblue;
  margin-top: 20px;
}
</style>
