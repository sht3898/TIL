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
