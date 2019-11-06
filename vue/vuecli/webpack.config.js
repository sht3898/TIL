// webpack 설정
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')
module.exports = {
    mode: 'development',
    // 여러개의 파일을 읽어오기
    entry: {
        app: path.join(__dirname, 'src', 'main.js')
    },
    // 관련된 모듈
    module: { 
        rules: [
            {
                test: /\.vue$/,  // .vue 확장자는
                use: 'vue-loader',  // 모두 vue-loader로 번역을 해라
            },
            {
                test: /\.css$/,
                use: ['vue-style-loader', 'css-loader']
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    // 최종 결과 (.js)
    output: {
        filename: 'app.js',
        path: path.join(__dirname, 'dist')
    }
}
