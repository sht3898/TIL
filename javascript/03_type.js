/*
* 원시타입(primitive data type)
    - boolean
    - null
    - undefined
    - number
    - string
    - symbol (ES6+)

* 객체타입(object)
    - object
*/

// number (typeof 를 검색하면 number로 뜨는 것들)
3
-5
Infinity
typeof Infinity
Nan // Not Number라는 뜻
0/0 // Nan
2.14e4
2.14e-4
10/0 // Infinity

// string
let myName = '탁희'
myName = "탁\n희"
// `(backtick) : ES6+ 템플릿리터럴
// string interpolation, 줄바꿈(개행)
myName = `탁
희`
console.log(`안녕하세요, ${myName}입니다.`)

// boolean, 모두 소문자로 사용
true
false

// empty value
undefined   // type -> undefined
null    // type -> object
typeof null
typeof undefined

// 이상한 형변환
'1' + 10    // 110
'1' * 10    // 10
'12' / 4    
// 3
let myNum = '12'
Number(myNum)   // 12
Number(myNum)/4 // 3