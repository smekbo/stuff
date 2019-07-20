<template>
  <div id="app">
    <div class="container header">
      <div class="row">
        <span class="col s12">A little town called</span>
        <h1 class="col s12">Coxwette</h1>
        <h2>Chapter {{$route.params.number}}</h2>
        <p><i>
          Presented stripped of quest context. Links to the original threads can be found <a href="https://tgchan.org/wiki/A_Little_Town_Called_Coxwette">here</a>.
        </i></p>
      </div>
  </div>
    <router-view></router-view>
  </div>
</template>

<script>
// import Woxcette from './components/Woxcette.vue'

export default {
  name: 'app'
}
</script>

<style>
</style>
