# Javascript Engine vs Javascript Runtime

## Javascript Engine

자바스크립트 엔진은 파싱과 [JIT 컴파일](https://ko.wikipedia.org/wiki/JIT_컴파일)을 하는 머신을 제공해야합니다.

자바스크립트로 쓰여진 스크립트로 기계가 실행가능한 과정을 만들어내는 과정을 할 수 있어야합니다. 대표적인 예시는 Google V8 엔진이 있습니다.



출처: https://geonlee.tistory.com/91 [빠리의 택시 운전사]



## Javascript Runtime

자바스크립트 런타임환경은 프로그램에 실행동안 사용 가능한 내장된 라이브러리를 제공합니다. 따라서 만약 당신이 브라우저 안에서 윈도우 오브젝트나 DOM API를 사용하고자한다면, 이 과정에 브라우저의 JavaScript 런타임 환경(Runtime Environment)이 포함될 것입니다. Node.js 런타임(runtime)은 Cluster와 FileSystem API들 같은 다른 라이브러리들을 포함합니다. 두 런타임(Runtime) 모두 내장된 데이터 타입들과 Console 오브젝트 같은 공통된 기능들을 포함하고 있습니다.





출처: https://geonlee.tistory.com/91 [빠리의 택시 운전사]

