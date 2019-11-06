# webpack

[참고 링크]( https://webpack.js.org/ )

* npm

  ```bash
  $ npm init # 실행하고 계속 enter 누르면 package.json 파일 생성됨
  ```

  * 비버있는 `package.json` 생성

  `node -> npm` 관계는 `python -> pip` 와 유사

* vue, webpack 설치

  ```bash
  $ npm install vue
  $ npm install webpack webpack-cli -D	# D는 개발자 버전으로 사용할 것이라는 것을 나타냄
  ```

  * webpack은 개발환경에서 모듈 번들러로써 활용하기 위한 것이므로 `-D` 옵션을 통해 `package.json`에서 `devDependencies`에 추가
  * node -> npm -> npm init -> install
  * python -> pip, activate, pip install django
  * 위의 두가지의 관계는 유사



webpack.config.js 파일 생성

src 폴더 생성, 그 안에 main.js 파일 생성

```js
// main.js

import Vue from 'vue'   // vue 자체를 불러옴
import App from './App.vue' // vue 파일(내가 만든)

new Vue({
    render: function(createElement) {
        createElement(App)
    }
})
```



## Vue 개발환경

### 1. vue 파일

```bash
$ npm install vue-loader vue-template-compiler -D
```

* vue-loader: vue 파일을 불러오는 역할
* vue-template-compiler: 해석하는 역할
* npm run build: 수정된 사항 반영



### 2. style

```bash
$ npm install vue-style-loader css-loader -D
```

* vue-style-loader: vue의 style
* css-loader: webpack css 불러오는 로더



# npm install -g @vue/cli

# vue create {프로젝트 이름}

enter

* default (babel, eslint)
* 