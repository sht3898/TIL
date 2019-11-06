<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <TodoList category="싸피"/>   <!-- 변경 되었음 -->
    <TodoList category="취업"/>   <!-- 변경 되었음 -->
    <TodoList category="개인"/>   <!-- 변경 되었음 -->
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'

export default {
  name: 'app',
  components: {
    TodoList  // 변경되었음
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
