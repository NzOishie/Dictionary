import Vue from 'vue'
import Router from 'vue-router'
import Item from '../components/Item'
import Word from '../components/Word'
import About from '../components/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Item
    },
    {
      path: '/word/:word',
      component: Word
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }

  ]
})
