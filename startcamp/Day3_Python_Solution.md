# Day 3 Python 문제풀이

## 문제 1

문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

```python
str = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.
print(str)
print(type(str))
print(f'첫 번째 글짜: {str[0]}, 두 번째 글자: {str[-1]}')
```

인덱스에 접근할 때 -로 접근하면 -1부터 차례로 마지막부터 접근한다.



## 문제 2

자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

```python
numbers = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
# Ver 1
for num in range(1, numbers+1):
    print(num)
# Ver 2
for num in range(numbers):
    print(num+1)
```

numbers를 통해 받은 문자를 반복을 통해 출력하는데 range 범위를 1부터 설정해서 가는 방법과 print할 때 1을 더해서 하는 두 가지 방법이 있다.



## 문제 3

숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

```python
number = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
# Ver 1
if number % 2:
    print(f'{number}은(는) 홀수입니다.')
else:
    print(f'{number}은(는) 짝수입니다.')
# Ver 2
if not number % 2:
    print(f'{number}은(는) 짝수입니다.')
else:
    print(f'{number}은(는) 홀수입니다.')
```

`Ver1`

number를 2로 나눌 때 나머지가 1이면 True로 처리가 되고, 0이면 False를 처리가 되는 것을 이용하여 홀수, 짝수를 구분할 수 있다.

`Ver2`

반대로 출력하고 싶다면 number 앞에 not을 붙여서 True/False를 반대로 뒤집어서 원하는 결과를 얻을 수 있다.

## 문제 4

표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

국어는 90점 이상,

영어는 80점 초과,

수학은 85점 초과, 

과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)

다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 

```python
a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))
위의 4줄의 주석을 풀고 아래에 코드를 작성해 주세요.
if a >= 90 and b > 80 and c > 85 and d >= 80:
    print('True')
else:
    print('False')
```

각각의 점수를 a, b, c, d를 통해 입력받고 and 조건을 통해 네 가지 조건을 모두 만족할 때 True를 출력하도록 설정한다.



## 문제 5

표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.

입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

\# 입력 예시: 300000;20000;10000

```python
prices = input('물품 가격을 입력하세요: ')
# 1. 반복문
int_price = []
for price in prices:
    int_price.append(int(price))
print(int_price)

# 2. list comprehension
int_price2 = [int(price) for price in prices]
print(int_price2)

# 3. map : 첫 번째 인자의 함수를 두 번째 인자를 반복하며 적음.
# 반복 가능한 객체에 함수를 각각 적용.
int_price3 = map(int, prices)
print(int_price3)
for price in int_price3:
    print(price)

int_price3 = sorted(int_price3, reverse = True)
```

> list에 처음 저장된 값들은 string형 변수이기 때문에, 99, 100과 같은 값을 비교하면 출력이 제대로 되지 않는다. 따라서 비교하기 전에 미리 int형 변수로 바꿔서 올바른 비교를 할 수 있게 만들어야 원하는 값을 출력할 수 있다.

`Ver1`

list형 변수인 int_price를 생성한 뒤, 반복문을 통해 새롭게 정렬된 값들을 입력해서 출력한다.

`Ver2`

list comprehension을 이용하여 새롭게 정렬된 값들은 int_price2에 입력해서 출력한다.

`Ver3`

map 함수를 이용하여 prices의 값들을 모두 int형으로 변환한 뒤, 출력한다.

`list.sort()` : return이 None, 원본 리스트 자체를 변경.

`sorted(list)` : return이 정렬된 리스트, 원본 자체는 변경하지 않음.









# Day3 (여기부터 선생님)

## HTML/CSS

## HTML

`HTML`은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <title>Document</title>
   </head>
   <body>
       <h1>용훈아 안녕!</h1>
   </body>
   </html>
   ```

   * `<head>` `</head>`는 문서의 정보를 담고 있다.
   * `<body>` `</body>`는 문서의 본문을 담고 있다.

2.  태그의 종류

   1. 기본적으로 태그는 `여는 태그`와 `닫는 태그`로 구성된다.

      ```html
      <h1>
          제목1
      </h1>
      ```

   2. `닫는 태그`가 없는 경우도 있다.(self-closing tag)

      ```html
      <img src="_"/>
      ```

   3. 태그의 구성

      ```html
      <img src="____" width="300" height="300"/>
      <a href="https://google.com" class="blue">구글</a>
      ```

   * 태그별로 공통적으로 가질 수 있는 속성 : id, class, style
   * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     * img - src, width, height
     * a - href



## CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ```css
     p {
         color : red;
     }
     ```

   * class 선택자

     ```css
     .blue {
         color : blue;
     }
     ```

   * id 선택자

     ```css
     #pink {
         color : pink;
     }
     ```

   선택자 우선순위는 id 선택자 > class 선택자 > 태그 선택자 순서로 적용된다.



## Flask

`Flask`는 파이썬 기반의 micro framework이다. 

### 기본 활용법

1.  설치

   ```bash
   $ pip install flask
   ```

2.  기본 코드

   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3.  서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 flask run 명령어는 app.py 파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   * 마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

   ```bash
   $ python app.py
   ```




### Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string.name>')
def hi(name):
    return f'{name}아 안녕?'
```

### Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```bash
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야한다.

```python
return render_template('hi.html', name=name)
```

 그리고 출력을 위해서는 `{{ }}` 사용한다.

```jinja2
<h1> {{name}} 안녕?</h1>
```

