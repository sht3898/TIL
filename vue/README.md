# Vue.js

[vue 사이트]( https://kr.vuejs.org/v2/guide/ )

* js - 명령형
* vue - 지시형

chrome extension에서 vue.js.develop 설치





## TODO

* v-for

  * 반복문 형태로 출력 가능하게 함

    ```html
    <div id="app">
      {{todos}}
      <li v-for="todo in todos">{{ todo }}</li>
    </div>
    ```
  
  ![image-20191104150148064](./03_01.png)

* v-if

  * 조건에 맞는 값만 출력

    ```html
    <li v-for="todo in todos" v-if="!todo.completed">
          {{ todo.content }}
        </li>
        <li v-else>
          [완료!]
        </li>
    ```

* v-on:click

  * 클릭하면 조건에 맞게 변경

    ```html
    <li v-for="todo in todos" v-if="!todo.completed" v-on:click="todo.completed=true">
        {{ todo.content }}
    </li>
    <li v-else>
        [완료!]
    </li>
    ```

* 클릭할때마다 완료, 미완료 상태 바꾸기

  ```html
  <li v-for="todo in todos" v-if="!todo.completed" v-on:click="toggleCompleted(todo)">
        {{ todo.content }}
      </li>
      <li v-else v-on:click="toggleCompleted(todo)">
        [완료!]
      </li>
  ```

  ```html
  methods: {
          toggleCompleted: function(todo) {
            todo.completed = !todo.completed
          }
        }
  ```

  

* 이미지 추가

  * 일반적인 것들을 제외하고는 디렉토리를 써서 출력한다

    ```html
    <img v-bind:src="logo" alt="" width="200px">
    ```

    ```html
    data: {
            logo: "https://repository-images.githubusercontent.com/105165445/b8efdd00-5d13-11e9-902e-3ce3c3d7e548",
            todos: [
              {
    ```

### 이벤트 핸들링

[링크]( https://kr.vuejs.org/v2/guide/events.html )







## 강아지

* v-for, v-src 기억하기

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  </head>
  <body>
    <div id="app">
      <img v-for="image in images" v-bind:src="image" alt="댕댕이" width="200px">
      <!-- 2-3. 반복문 -->
      <button v-on:click="getDog()">새로운 강아지 보기</button>
      <p>{{count}}</p>
    </div>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          images: [], // 2-1. 배열로 변경
          count: 0
        },
        methods:{
          getDog: function() {
            // 요청 보내서 가지고 오면,
            axios.get("https://dog.ceo/api/breeds/image/random")
            .then(response => {
            // imageUrl을 변경
              console.log(this) // arrow가 아니라면 this가 window여서 저장안됨
              this.images.push(response.data.message) // 2-2. 배열에 값넣기로 바꾸기
              this.count ++
            })
          }
        }
      })
    </script>
  </body>
  </html>
  ```

  



## 정리(vue_directive.html)

* vue 설치하고 시크릿 모드와 url 링크도 가능하게 설정

* 반복문과 조건문

  * 반복 => v-for
  * 조건 => v-if

* v-model

  * data에 있는 해당 model을 수정

  * v-model을 사용하려면 data 내에서 초기화 작업 필요

* v-bind

  ```html
  <!-- 속성값: v-bind
        v-bind 생략하는 방법으로도 작성 가능
      -->
      <img v-bind:src="url" alt="">
      <img :src="url" alt="">
  ```

  ```html
  <script>
      const app = new Vue({
        el: '#app',
        data: { // app.$data
        url: 'https://joshua1988.github.io/images/posts/web/vuejs/logo.png',
            ...
  ```

* v-on:click

  ```html
  <button v-on:click="countUp">+++++</button>
      <p>{{ counter }}</p>
      <button @click="countDown">------</button>
  ```

  ```html
  methods: {
          countUp: function() {
            this.counter ++
            console.log(this.counter)
          },
          countDown: function() {
            this.counter--
            console.log(this.counter)
          }
        }
  ```

  * 단축어로도 사용할 수 있다.(=@click)

