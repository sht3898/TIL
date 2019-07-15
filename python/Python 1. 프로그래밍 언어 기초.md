# Python 1. 프로그래밍 언어 기초(Workshop)

```text
jupyter 접속시 폴더에서 bash 접속 후 jupyter notebook 입력
```

# Problem

* 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요

```python
# 문제
n = 5
m = 9
print(('*' * n + '\n') * m)
```

```
*****
*****
*****
*****
*****
*****
*****
*****
*****
```

- print 함수를 한번만 사용해 다음 문장을 출력하시오. "파일은 C:\Windows\Users\내문서\Python에 저장이 되어 있습니다." 나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'

```python
print('''"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어 있습니다."
나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'
''')
```

```
"파일은 C:\Windows\Users\내문서\Python에 저장이 되어 있습니다."
나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
```

* 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.
x^2 + 4x - 21

> Ver 1

```python
x = -100
while x**2 + 4*x - 21 != 0:
    x = x + 1
print(x)
```

```
-7
```

> Ver 2

```python
print(-2 + ((4 + 21) ** (1/2))); print(-2 - ((4 + 21) ** (1/2)))
```

```
3.0
-7.0
```



# Python 1.  프로그래밍 기초(Homework)

1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import pprint
import keyword
pprint.pprint(keyword.kwlist)
```

```
['False',
 'None',
 'True',
 'and',
 'as',
 'assert',
 'async',
 'await',
 'break',
 'class',
 'continue',
 'def',
 'del',
 'elif',
 'else',
 'except',
 'finally',
 'for',
 'from',
 'global',
 'if',
 'import',
 'in',
 'is',
 'lambda',
 'nonlocal',
 'not',
 'or',
 'pass',
 'raise',
 'return',
 'try',
 'while',
 'with',
 'yield']
```

2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.(floating point rounding error)
따라서, 아래의 값을 비교하기 위해 작성해야 하는 코드를 작성하세요.
a = 0.1 * 3
b = 0.3

``` python
a = 0.1 * 3
b = 0.3
print(type(a))
print(type(b))
round(a,1) == round(b,1)
```

```
<class 'float'>
<class 'float'>
True
```

3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \을 작성하세요

```python
print('이스케이프', end='\n')
print('줄바꿈')
print('이스케이프', end='\t')
print('탭')
print('\'이스케이프\'')
```

```
이스케이프
줄바꿈
이스케이프	탭
'이스케이프'
```

4. "안녕, 철수야"를 String Interpolation을 사용하여 출력하세요.
print(name = "철수")

```python
name = '철수'
print(f'안녕, {name}야')
```

5. 다음 중 형변환시 오류가 발생하는 것은?
  1) str(1) 

  2) int('30')

  3) int(5)

  4) bool('50')

  5) int('3.5')

  => 5)번; 문자열은 int형으로 형변환 불가

```python
str(1)
int('30')
int(
True5)
bool('50')
```

```
True
```

