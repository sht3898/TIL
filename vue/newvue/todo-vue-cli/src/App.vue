<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 컴포넌트를 호출 -->
    <TodoList category="싸피"/>   <!-- 변경 되었음 -->
    <TodoList category="취업"/>   <!-- 변경 되었음 -->
    <TodoList category="개인"/>   <!-- 변경 되었음 -->
  </div>
</template>

<script>
// 1. 컴포넌트를 부모 컴포넌트에서 불러옴.
import TodoList from './components/TodoList.vue'  // 변경

export default {
  name: 'app',
  components: {
    TodoList  // 변경되었음 2. 컴포넌트를 추가
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
