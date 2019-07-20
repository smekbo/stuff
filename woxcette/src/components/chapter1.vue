<template>
  <div class="container">   
    <div class="row post" v-for="post in $options.postData" v-if="post.image" v-bind:class="{spoiler: post.spoiler}">
      <div class="col s12 poster"><b>{{post.poster}}</b></div>
      <img class="col s5 image" :src="post.image" v-if="post.body !== null"></img>
      <img class="col s12 image" :src="post.image" v-if="post.body === null"></img>
      <span class="col s7 body" v-html="post.body"></span>
    </div>
  </div>
</template>

<script>
import Data from '../assets/chapter1.json'
import '../assets/css/materialize.min.css'
import '../assets/css/style.css'
import '../assets/js/materialize.min.js'
  
function importAll(r) {
  return r.keys().map(r);
}

const images = importAll(require.context('../assets/img', false, /\.(png|jpe?g|svg)$/));
  
var y = 0;
for (var i = 0; i < Data.length; i++){
  if (Data[i].image !== "" && Data[i].poster !== "Suggestion"){
    Data[i].image = images[y];
    y++;
  }
  else {
    Data[i].image = null;
  }
}
  
export default {
  name: 'posts',
  postData: Data
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
