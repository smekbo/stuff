import Vue from 'vue'
import Router from 'vue-router'
import chapter from '../components/chapter.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/chapter/:number',
      component: chapter
    }
  ]
})