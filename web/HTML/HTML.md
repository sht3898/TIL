# HTML

* `Hyper Text Markup Language` 의 약자
* Hyper Text
  - 기존의 선형적인 텍스트가 아닌 비선형적으로 이루어진 텍스트, Hyper Link를 통해 텍스트를 이동한다.
  - HTTP (Hyper Text Transfer Protocol) : Hyper Text를 주고 받는 규칙
  - HTTP(S) : Hyper Text Transfer Protocol Secure
* Markup
  * **HTML 요소**(엘리먼트, Elements)와 그들의 속성(Attributes)과 문자 기반 **데이터 형태**와 **문자 참조**와 **엔티티 참조**를 포함하는 몇 가지 핵심 구성 요소로 구성
* Language
  - 웹 페이지를 작성하기 위한 역할 표시 언어
* HTML 파일
  * HTML로 작성된 문서파일
* 웹 표준
  * `W3C` : World Wide Web Consortium
  * `WHATWG` : Web Hypertext Application Technology Working Group
* 속상값 입력시 공백 no



## HTML 문서의 기본 구조

```html
<!DOCTYPE html> <!-- DOCTYPE 선언부 -->
<html lang="en"> <!-- ~끝까지 html 요소 -->
<head>  <!-- head 요소 -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>  <!-- body 요소 -->
  
</body>
</html>
```

* `DOCTYPE` 선언부 : 사용하는 문서의 종류를 선언하는 부분. 보통 html을 사용한다.
* `html` 요소 : HTML 문서의 최상위 요소로 문서의 root를 뜻한다. head와 body 부분으로 구분된다.
* `head` 요소 : 문서 제목, 문자코드(인코딩)과 같이 해당 문서 정보를 담고 있으며, 브라우저에 나타나지 않는다. CSS 선언 혹은 외부 로딩 파일 지정등도 작성한다.
* `body` 요소 : 브라우저에 나타나는 정보로 실제 내용에 해당한다.





## Tag와 DOM TREE(Document Object Model)

### 0) 주석(Comment)

<!--주석 내용 -->

* HTML에서 사용되는 주석 표기법(화면에 나오지 않음)



### 1) 요소(Element)

<'h1> 여는 태그 contents <''/h1> 닫는 태그

* HTML의 element는 태그와 내용(contents)로 구성되어 있다. 태그는 대소문작를 구별하지 않으나, 소문자로 작성해야 한다. 요소간의 중첩도 가능.



### 2) Self-closing element

```html
<img src="url"/>
```

* 닫는 태그가 없는 태그도 존재한다.



### 3) 속성(Attribute)

* 태그에는 속성이 지정될 수 있다.
* id, class, style 속성은 태그와 상관없이 모두 사용 가능하다.
* 공백은 사용하지 말고, 큰 따옴표("")를 사용하도록 한다.



### 4) DOM 트리

* 태그 안에 태그가 있는 방식으로 구조화 되어 있는 것

* 태그는 중첩되어 사용가능하며, 이때 위와 같은 관계를 갖는다.

* 부모-자식 관계

  ![parent](./images/parent.png)

* 형제 관계

  ![sibling](./images/sibling.png)

```html
<body>
    <h1></h1>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</body>
```

- `<h1>`과 `<ul>`은 형제 관계
- `시맨틱 태그(Semantic Tag)`
  - `<div>` `</div>`



## HTML

- `open in browser` ,`HTML Snippets` 설치

- `open in browser` - alt + b 하면 브라우저에서 열기 가능

- crtl + shift + p -> settings.json에서 html과 css 설정 추가

  ```html
  {
      "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
      "editor.fontFamily": "'Fira Code', 'Consolas', 'Courier New', monospace",
      "editor.fontLigatures": true,
      "[html]": {
          "editor.tabSize": 2
      },
      "[css]" : {
          "editor.tabSize": 2
      }
  }
  ```

- `emmet.io` 에서 html 문법 정보 확인



## Etc

- ctrl + alt + 화살표 -> 동시 입력 가능
- h1+h2+h3+h4+h5 하고 탭 누르면 동시에 여러개 입력 가능



# 수업 정리

## Tags

### DOCTYPE 선언과 head

문서의 기본 설정을 하고 title 등을 설정함

```html
<!--!+tab-->
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
```



### Body

문서의 본문이 담기는 곳

```html
<body>
  <h1>문서의 제목 - 여는태그/닫는태그</h1>
  <!-- 닫는 태그가 없는 self-closing 태그도 있습니다. -->
  <input type="text"> <br> <!--엔터(다음 라인으로)-->
  <img src="bonobono.jpg" alt="보노보노사진">
  <hr> <!--수평선을 그려주는 태그-->
  <div><!--의미가 없지만, 레이아웃을 나누는 태그(display: block)-->
    <p>div태그의 자식(child)</p>
    <p>위의 p태그와 형제(sibling)</p>
  </div>
  <footer><!--시맨틱 태그 (HTMLS에서 추가한 태그)-->
    <p>똑같은 영역인데, 여기는 푸터!</p>
  </footer>
</body>
</html>
```

![1565538828921](./images/1.png)





