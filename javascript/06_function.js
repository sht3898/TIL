/*
    * 함수
*/

console.log(myAdd(1, 2))
console.log(myAdd2(1, 2))

// 선언식 -> hosting, 출력됨
function myAdd(a, b){
    return a + b
}

// 표현식
let myAdd2 = function (a, b){
    return a + b
}


/*
    * arrow function
    ES6+
*/

let myFunction = function(a) {
    return a + 1
}
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

/*
    * 익명 함수
    바로 실행
*/
(function (a) {
    return a * 10
}(10))

// arrow function으로 똑같이 구현
((a) => a*10)(10)
