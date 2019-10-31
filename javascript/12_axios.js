console.log('hi')
axios.get('https://jsonplaceholder.typicode.com/posts/1')
    .then(response => {     // get으로 요청을 받았을때 실행
        console.log(response)
        document.write(`
            <h1>${response.data.id} : ${response.data.title}</h1>
            <p>${response.data.body}</p>
        `)
        return response.data
    })
// axios보다 먼저 나옴, get으로 요청 받아오는 것보다 먼저 실행되기 때문
console.log('bye')
