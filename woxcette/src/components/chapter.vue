<template>
  <div class="container">   
    <div class="row post" v-for="(post, index) in posts" v-show="isAuthor(post)" v-bind:class="{spoiler: post.spoiler}">
      <div class="col s12 poster"><b>{{post.poster}}</b></div>
      <img class="col s5 image" :src="post.image" v-if="post.body !== null" v-on:click="expand"></img>
      <span class="col s7 body" v-html="post.body"></span>
    </div>
  </div>
</template>

<script>
import '../assets/css/materialize.min.css'
import '../assets/css/style.css'
import '../assets/js/materialize.min.js'
  
function importAll(r) {
  return r.keys().map(r);
}

var images = importAll(require.context('../assets/img', true, /\.(png|jpe?g|svg|gif)$/));

var loadChapter = function(chapter){
  var json = require('../assets/chapter' + chapter + '.json')
  
  return json;
}
  
export default {
  name: 'posts',
  data: function() {
    return {
      posts: ""
    }
  },
  methods: {
    expand: function(event){
//       console.log(event);
      if (event.target.className.includes("s5")){
        event.target.className = "col s7 image" 
        event.target.nextElementSibling.className = "col s5 body"
      }
      else {
        event.target.className = "col s5 image"
        event.target.nextElementSibling.className = "col s7 body"
      }
    },
    isAuthor: function(post){
      if (post.poster !== "Suggestion" && ( post.image !== null && post.image !== "")){
        return true
      }
      else { return false }
    }
  },
  created () {
    this.posts = loadChapter(this.$route.params.number)
  },  
  watch: {
    '$route' (to, from) {
      var json = loadChapter(to.params.number)
      this.posts = json
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
