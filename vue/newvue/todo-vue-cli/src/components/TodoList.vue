<template>
    <div class="todo-list">
      <h2>{{ category }}</h2>
      <input type="text" v-model="newTodo">
      <button @click="addTodo">입력</button>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.content }}
        <button @click="removeTodo(todo.id)">삭제</button>
      </li>
    </div>
</template>

<script>
export default {
    props: {
        category: {
          type: String,
          required: true  // 항상 필요하다
          }
      },  // 하위 컴포넌트로 데이터 전송 + 검증
      data: function() {
        return {
          todos: [],
          newTodo: ''
        }
      },
      methods: {
        addTodo() {
          this.todos.push({
            id: Date.now(),
            content: this.newTodo,
            completed: false,
          })
          this.newTodo = ''
        },
        removeTodo: function(id) {
          this.todos = this.todos.filter(todo => {
            return todo.id !== id
          })
        }
      }
}
</script>

<style lang="">
    /* li {
        color: blue;
    } */
</style>