# Javascript

## 1-1. 선언과 할당

|     var     |         let(변수)         |        const(상수)        |
| :---------: | :-----------------------: | :-----------------------: |
| 함수 스코프 |        블록 스코프        |        블록 스코프        |
|  무한 선언  |         재선언 X          |    재선언 X, 재할당 X     |
|  호이스팅   | 임시공간(Error Reference) | 임시공간(Error Reference) |

var => let 바꾸는 것은 상관 x
* 재할당

  ```javascript
  var myVar // 선언
  myVar = 1 // 할당
  console.log(myVar)
  ```

* 재선언

  ```javascript
  var myVar // 선언
  var myVar = 'Hello' // 재선언
  ```

* const는 선언과 동시에 할당을 해줘야 값을 부여할 수 있다.



## 1-2. scope

ES6 + (ES2015) 이상에서는 변수가 기본적으로 var로 적용되어있음

* var

  ```javascript
  let VarFunction = function(){
      var myVar = 0
      if (true) {
          var myVar = 1
          console.log(myVar)	// 1
      }
      console.log(myVar)	// 1
  }
  ```

* let

  ```javascript
  let LetFunction = function(){
      let myLet = 0
      if (true) {
          let myLet = 1
          console.log(myLet)	// 1
      }
      console.log(myLet)	// 0
  }
  ```

  

## 2. hoistion

* var

  ```javascript
  console.log(taewoo)
  var taewoo = '김태우'
  ```

  1. 선언과 동시에 초기화

  2. 할당

* let

  ```javascript
  console.log(kyungho)    // ReferenceError - 초기화하기전 접근 X
  let kyungho = '이경호'
  ```
  * let, const는 TDZ(Temporal Dead Zone)이 존재
  1. 선언
2. TDZ
  3. 초기화
4. 할당




## 3. type

* number

  typeof를 검색하면 number로 뜨는 것들

  ```javascript
  3
  -5
  Infinity
  typeof Infinity
  Nan // Not Number라는 뜻
  0/0 // Nan
  ```

* string

  엔터도 인식

  ```javascript
  // string
  let myName = '탁희'
  myName = "탁\n희"
  // `(backtick) : ES6+ 템플릿리터럴
  // string interpolation, 줄바꿈(개행)
  myName = `탁
  희`
  console.log(`안녕하세요, ${myName}입니다.`)
  ```

* boolean

  모두 소문자로 사용

  ```javascript
  // boolean, 모두 소문자로 사용
  true
  false
  ```

* empty value

  ```javascript
  // empty value
  undefined   // type -> undefined
  null    // type -> object
  typeof null
typeof undefined
  ```
  
* 형변환

  ```javascript
  '1' + 10    // 110
  '1' * 10    // 10
  '12' / 4    
  // 3
  let myNum = '12'
  Number(myNum)   // 12
  Number(myNum)/4 // 3
  ```



## 4. operator

* js에서 if문 등의 비교는 세개가 기본 ( === )

  ```javascript
  // 동등 연산자(==)
  
  1 == '1' // true
  
  // 일치 연산자( === )
  1 === '1' // false
  
  // 할당( =, +=, -=, *=, /= )
  
  // 비교 > < >= <=
  
  // 논리 and( && ) or(||)
  
  // not !
  
  // 삼항연산자 표현식? true : false
  2 > 4 ? true : false
  
  ```



## 5. flow

* if문

  ```javascript
  let userName = prompt('넌 누구니?')
  let message
  
  if (userName === 'admin'){
      message = '<h1>Hello SSAFY</h1>'
  } else if (userName === '1q2w3e4r') {
      message = 'Admin page입니다.'
  } else {
      message = `<h1>${userName} 환영합니다.</h1>`
  }
  
  document.write(message)
  ```

* switch-case문

  ```javascript
  switch(userName) {
      case '1q2w3e4r': {
          message = '<h2>관리자님 충성충성^^7</h2>'
          break
      }
      case 'ssafy': {
          message = '<a href="https://edussafy.com">싸피</a>'
          break
      }
      default: {
          message = `<h1>${username} 환영합니다.</h1>`    // backtick
          break
      }
  }
  
  document.write(message)
  ```

  case마다 break를 걸지 않으면 default 다 거치게 되어서 default에 있는 메시지를 출력하게 됨



## 6. function

* 파이썬의 익명 함수

  ```python
  def my_fun(x):
      x = x + 1
  
  def my_func2 = lambda x : x+1
  ```

* 위의 내용을 javascript로 표현

  ```javascript
  /*
      * 함수
  */
  
  console.log(myAdd(1, 2))
  console.log(myAdd2(1, 2))
  ```

* 선언식

  ```javascript
  // 선언식 -> hosting, 출력됨
  function myAdd(a, b){
      return a + b
  }
  ```

* 표현식

  ```javascript
  // 표현식
  let myAdd2 = function (a, b){
      return a + b
  }
  ```

* arrow function (ES6+)

  ```javascript
  let myFunction = function(a) {
      return a + 1
  }
  ```

* function

  ```javascript
  // 1. function 키워드 삭제 후 =>
  let myArrowFunction = (a) => {return a + 1}
  // 1-1. 인자가 하나라면, 소괄호 삭제 가능
  // 1-2. 문장이 한 줄이고, 리턴이라면 중괄호 및 return 키워드 생략 가능
  let myArrowFunction1 = a => a + 1
  
  // 제곱의 결과를 나타내는 square 함수를 표현식
  let square = function (num) {
      return num ** 2
  }
  // arrow function
  square2 = (num) => { return num ** 2}
  square2 = num => {return num ** 2}
  square2 = num => num**2 // 인자 1개면 이렇게 표현 가능
  
  let greeting = function(){
      console.log('happy!')
  }
  
  // 1-3. 인자가 없는 경우에는 () or _
  greeting = () => {console.log('happy!')}
  greeting()
  greeting = _ => {console.log('happy!')}
  greeting()
  
  // 1-4. 기본인자(입력 값이 없을 때 출력 되는 값)
  let greeting2 = (name='타키') => name
  ```



## 7. array

```javascript
let numbers = [10, 1, 3, 5]

numbers[0] // 10
numbers[-1] // undefined
numbers.length // 4 (길이)

numbers.reverse()   // return + 원본 변경
numbers.push(3) // 마지막 원소에 추가 + return (길이)
numbers.pop()   // 마지막 원소 제거 + return (원소)
numbers.unshift(3)  // 가장 첫번째 원소에 추가
numbers.shift() // 가장 첫번째 원소 제거 + return (원소)

numbers.includes(1) // 포함여부 확인
numbers.indexOf(1)  // 가장 먼저 존재하는 위치

numbers.join()  // 기본이 ,
numbers.join('-')   // -로 연결

```



## 8. object

```javascript
const me = {
    name: 'kim',
    'phone number': '01092443898',
    phone: {
        type: 'iphone XS MAX'
    },
    // 메서드 function 키워드만 작성하자!
    greeting: function() { 
        console.log(this)   // me 객체를 가리킴
        console.log(`hi ${this.name}`)  // this: 자기자신을 뜻함
    },
    greeting2: () => {
        console.log(this)   // 전역객체인 window를 가리킴
        console.log(`hi ${this.name}`)
        // this.name이 출력되지 않음
        // arrow function에서의 this는 무조건 상위에 있는 객체
        // 
    }
}
var name = 'kim'    // window 객체의 name이 kim 으로 바뀜


console(me.name)
console(me['name'])
console(me.phone.type)

// ES6+ 오브젝트 리터럴 표기법
// 
let book = '자바스크립트 완전 정복'
let albums = {
    IU: ['좋은날', '밤편지'],
    BTS: ['작은것들을 위한 시']
}

let bag = {
    book,
    albums
}

// JSON (JavaScript Object Notation): JS object의 표기법
// 자바스크립트 오브제특 표기법을 가진 문자열. JSON 자체가 문자열
// object -> JSON
let jsonData = JSON.stringify(me)
let myObject = JSON.parse(jsonData)

```

Notion 문서



## 9. array_helper_method

```javascript
/*
    Array helper methods
*/


/*
    Array.forEach
*/

let numbers = [1, 2, 3]
// 1. 반복문 (for)
for (let i=0; i<=numbers.length; i++){
    console.log(numbers[i])
}
// 2. 반목문 (for .. of)
for (let num of numbers){
    console.log(num)
}
// 3. forEach, callback 함수
numbers.forEach(function(num){
    console.log(num)
})
// 실습
const images = [
    {height: 30, width: 20},
    {height: 100, width: 100},
    {height: 10, width: 5},
]
// let areas = [600, 1000, 50] 로 나오게 출력
let areas = []
images.forEach(function(image, idx){
    console.log(idx)
    areas.push(image.height*image.width)
})
console.log(areas)

/*
    map
    : 콜백함수의 return 결과를 각각 원소로 하는 배열을 **리턴**!
*/
let numbers = [1, 2, 3]

let doubleNumbers = numbers.map(function(number){
    return number * 2
})
console.log(doubleNumbers)

let doubleNumbers2 = numbers.map(number => number*2)
console.log(doubleNumbers2)

// 실습 images -> map
let areas = images.map(function(image){
    return image.height * image.width
})
console.log(areas)

let areas2 = images.map(image => image.height * image.width)
console.log(areas2)

/*
    filter
    : 콜백함수의 return 결과가 참인 것을 각각 원소로 하는 배열을 **리턴**!
*/
// images의 높이가 100보다 작은 object만 담은 배열
let myImage = []
for (let image of images){
    if (image.height < 100) {
        myImage.push(image)
    }
}


let area3 = images.map(function(image){
    if (image.height < 100){
        return image.height * image.width
    }
})
console.log(area3)


// filter는 map과 다르게 undefined 된 것은 반환하지 않고 tru 인 것만 반환
myImage = images.filter(function(image){
    return image.height < 100
})
console.log(myImage)

// fruit만 뽑아내기
let products = [
    {name: 'banana', type: 'fruit'},
    {name: 'tomato', type: 'vegitable'},
    {name: 'apple', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'}
]

let bag = []
bag = products.filter(function(product){
    return product.type === 'fruit'
})

bag = products.filter(product => product.type === 'fruit')


/*
    reduce(callbackfn, initialvalue)
    : return 결과를 누적한 결과를 return
*/

let mySsafy = [100, 100, 95, 90]
let totalScore = 0
mySsafy.forEach(function(score){
    totalScore += score
})

totalScore = mySsafy.reduce(function(total, score){
    console.log(score)  // 원소
    console.log(total)  // 누적
    return total + score
}, 100) // 초기값

mySsafy.reduce((total, score) => total + score, 100)

/*
    find: 일치하는 첫번째 원소를 리턴
*/
mySsafy.find(function(score){
    return score === 90
})

let heros = [
    {name: '헐크', age: 100},
    {name: '아이언맨', age: 50},
    {name: '스파이더맨', age: 30}
]
heros.find(function(hero){
    return hero.age === 30
})
/*
    Array helper methods
*/


/*
    Array.forEach
*/

let numbers = [1, 2, 3]
// 1. 반복문 (for)
for (let i=0; i<=numbers.length; i++){
    console.log(numbers[i])
}
// 2. 반목문 (for .. of)
for (let num of numbers){
    console.log(num)
}
// 3. forEach, callback 함수
numbers.forEach(function(num){
    console.log(num)
})
// 실습
const images = [
    {height: 30, width: 20},
    {height: 100, width: 100},
    {height: 10, width: 5},
]
// let areas = [600, 1000, 50] 로 나오게 출력
let areas = []
images.forEach(function(image, idx){
    console.log(idx)
    areas.push(image.height*image.width)
})
console.log(areas)

/*
    map
    : 콜백함수의 return 결과를 각각 원소로 하는 배열을 **리턴**!
*/
let numbers = [1, 2, 3]

let doubleNumbers = numbers.map(function(number){
    return number * 2
})
console.log(doubleNumbers)

let doubleNumbers2 = numbers.map(number => number*2)
console.log(doubleNumbers2)

// 실습 images -> map
let areas = images.map(function(image){
    return image.height * image.width
})
console.log(areas)

let areas2 = images.map(image => image.height * image.width)
console.log(areas2)

/*
    filter
    : 콜백함수의 return 결과가 참인 것을 각각 원소로 하는 배열을 **리턴**!
*/
// images의 높이가 100보다 작은 object만 담은 배열
let myImage = []
for (let image of images){
    if (image.height < 100) {
        myImage.push(image)
    }
}


let area3 = images.map(function(image){
    if (image.height < 100){
        return image.height * image.width
    }
})
console.log(area3)


// filter는 map과 다르게 undefined 된 것은 반환하지 않고 tru 인 것만 반환
myImage = images.filter(function(image){
    return image.height < 100
})
console.log(myImage)

// fruit만 뽑아내기
let products = [
    {name: 'banana', type: 'fruit'},
    {name: 'tomato', type: 'vegitable'},
    {name: 'apple', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'}
]

let bag = []
bag = products.filter(function(product){
    return product.type === 'fruit'
})

bag = products.filter(product => product.type === 'fruit')


/*
    reduce(callbackfn, initialvalue)
    : return 결과를 누적한 결과를 return
*/

let mySsafy = [100, 100, 95, 90]
let totalScore = 0
mySsafy.forEach(function(score){
    totalScore += score
})

totalScore = mySsafy.reduce(function(total, score){
    console.log(score)  // 원소
    console.log(total)  // 누적
    return total + score
}, 100) // 초기값

mySsafy.reduce((total, score) => total + score, 100)

/*
    find: 일치하는 첫번째 원소를 리턴
*/
mySsafy.find(function(score){
    return score === 90
})

let heros = [
    {name: '헐크', age: 100},
    {name: '아이언맨', age: 50},
    {name: '스파이더맨', age: 30}
]
heros.find(function(hero){
    return hero.age === 30
})
heros.find(hero => hero.age === 30)

/*
    some:
    일부라도 일치하나
    every:
    모두 일치하나
*/

let myNumbers = [1, 2, 3, 4]
myNumbers.some(function(number){
    return number % 2 === 0
})

myNumbers = [3, 5]
myNumbers.every(function(number){
    return number % 2 !== 0
})
```



## 10. dom

```javascript
// my-list 출력
document.querySelector('#my-list')

// 모든 text 출력
document.querySelectorAll('.text')

// 조건에 맞는 첫번째 text 출력
document.querySelector('.text')

```

* 아이디는 문서당 하나만 존재