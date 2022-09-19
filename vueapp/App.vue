<template>
  <div class="black-bg" v-if="popup ==true">
    <div class="white-bg">
      <h4>상세페이지</h4>
      <p>상세페이지 내용</p>
    </div>
  </div>
  <!-- v-if / v-else v-else-if -->
  
  

  <div class="menu">
    <a href="#" v-for="i in menu" :key="i">{{i}}</a>
    <!-- <a href="#">Products</a>
    <a href="#">Intro</a> -->

    <!-- v-for 반복문 : v-for ="아무이름 in 반복갯수" :key ="아무이름"-->
  </div>
  <div>
    <h4 :style="title" @click="popup = true">{{products[0]}}</h4>
    <p>월 {{price1}}만원</p>
    <button @click="like[0]++">좋아요</button>
    <span>like : {{like[0]}}</span>
  </div>

  <div>
    <h4>{{products[1]}}</h4>
    <p>월 30만원</p>
    <button @click="like[1]++">좋아요</button>
    <span>like : {{like[1]}}</span>
  </div>

  <div>
    <h4>{{products[2]}}</h4>
    <p>월 30만원</p>
    <button @click="like[2]++">좋아요</button>
    <span>like : {{like[2]}}</span>
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data(){
    return {
      title : 'color:red',
      price1 : 60,
      products : ['경산원룸','대가대 원룸','창원원룸'],
      menu : ['Home', 'Products', 'Intro'],
      like : [0,0,0],
      popup : false
    }  
  },
  methods: {
    v_plus(){
      this.like += 1
    }
  },
}
</script>

<style>
body{
  margin:0;
}
div {
  box-sizing: border-box;
}
.black-bg{
  width: 100%; height: 100%;
  background: #000000;
  position: fixed; padding:20px;
}
.white-bg{
  width: 100%;
  background: rgb(59, 223, 223);
  padding:20px;
}
.menu {
    background-color: black;
    padding: 15px;
    border-radius:5px;
}
.menu a{
  color:white;
  text-decoration: none;
  padding: 10px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
