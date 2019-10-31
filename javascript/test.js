function sum(x, callbackfn) {
    setTimeout(callbackfn, 1000, x+1)   // 1초 뒤에 계산됨, 세번째 인자를 받아들임
    return x+1
}
var result = 0
sum(2, function(x){
    result = x
    console.log(result) // 3이 출력됨, timeout 때문에 뒤늦게 들어감
})
console.log(result) // 0이 출력됨