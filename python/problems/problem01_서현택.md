
# 상승장? 하락장?

> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

|Key Name|Description|
|------|---|
|opeing_price|최근 24시간 내 시작 거래금액|
|closing_price|최근 24시간 내 마지막 거래금액|
|min_price|최근 24시간 내 최저 거래금액|
|max_price|최근 24시간 내 최고 거래금액|


```python
import pprint
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
pprint.pprint(data)
```

    {'24H_fluctate': '-1343000',
     '24H_fluctate_rate': '-9.85',
     'average_price': '12699518.1004',
     'buy_price': '12283000',
     'closing_price': '12290000',
     'date': '1563170744320',
     'max_price': '13648000',
     'min_price': '11879000',
     'opening_price': '13633000',
     'sell_price': '12296000',
     'units_traded': '16828.30640801',
     'volume_1day': '16828.30640801',
     'volume_7day': '90000.82763557'}
    


```python
# 아래에 코드를 작성하세요.
gap = int(data['max_price']) - int(data['min_price'])
if int(data['opening_price']) + gap > int(data['max_price']):
    print('상승장')
else:
    print('하락장')
```

    상승장
    

# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

```
예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
```


```python
my_str = "Life is too short, you need python"
```


```python
# 아래에 코드를 작성하세요.
# ver1
# my_str를 반복하면서,
# 모음이 아니면,  answer에 추가한다.
# 반복문이 끝나면 출력한다.
answer = ''
for i in my_str:
    if i != 'i' and i != 'e' and i != 'o' and i != 'u':
        answer += i
print(answer)

# ver2
for i in my_str:
    if i == 'i' or i == 'e' or i == 'o' or i == 'u':
        i = ''
    print(i, end='')
```

    Lf s t shrt, y nd pythn
    Lf s t shrt, y nd pythn


```python
# 아래에 코드를 작성하세요.(선생님 버전)
result = ''
# my_str를 반복하면서,
for char in my_str:
    # 모음이 아니면,  result에 추가한다.
#     if char not in ['a', 'e', 'i', 'o', 'u']:
    if char not in 'aeiou':
        result += char
# 반복문이 끝나면 출력한다.
print(result)
```

    Lf s t shrt, y nd pythn
    


```python
for vowel in 'aeiou':
    my_str = my_str.replace(vowel, '')
print(my_str)
```

    Lf s t shrt, y nd pythn
    

# 개인정보보호
> 사용자의 핸드폰번호를 입력 받으려고한다. 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리를 하려고한다.
>
> 핸드폰번호는 010으로 시작해야하고 11자리여야한다. 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다

```
예시 입력)
01012341234
예시 출력)
*******1234
```


```python
phone = input()
```

    01092443898
    


```python
# 아래에 코드를 작성하세요.
# ver1
number = []
if len(phone) < 11:
    print('핸드폰 번호를 입력하세요')
elif phone[0:3] != '010':
    print('핸드폰 번호를 입력하세요')
else:
    print(f'*******{phone[7:11]}')

# ver2
phone_number = list(phone)
if len(phone) < 11:
    print('핸드폰 번호를 입력하세요')
elif phone[0:3] != '010':
    print('핸드폰 번호를 입력하세요')
else:
    for i in range(7):
        phone_number[i] = '*'
    for i in phone_number:
        print(i, end='')
```

    *******3898
    *******3898


```python
if phone[0:3] == '010' and len(phone) == 11:
    print('*'*7 + phone[-4:])
else:
    print('핸드폰 번호를 입력하세요')
```

    *******3898
    


```python
if phone.startswith('010') and len(phone) == 11:
    print(f'{phone[-4:]:*>11}')
```

    *******3898
    

# 정중앙
> 사용자가 입력한 문자열중 가운데 글자를 출력하라. 문자열이 짝수라면 가운데 두글자를 출력하라


```python
text = input()
```

    안녕하세요
    


```python
# 아래에 코드를 작성하세요.
if len(text) % 2 == 1:
    print(text[len(text)//2])
else:
    print(text[len(text)//2 - 1:len(text)//2 + 1])
```

    하
    


```python
num = len(text) // 2
if len(text) % 2:
    print(text[num])
else:
    print(text[num-1:num+1])
```

    하
    

# Python 1. 프로그래밍 언어 기초(Workshop)

## Problem

* 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요


```python
# 문제
n = 5
m = 9
print(('*' * n + '\n') * m)

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
    
    

* print 함수를 한번만 사용해 다음 문장을 출력하시오.
"파일은 C:\Windows\Users\내문서\Python에 저장이 되어 있습니다."
나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'


```python
print('''"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어 있습니다."
나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'
''')
```

    "파일은 C:\Windows\Users\내문서\Python에 저장이 되어 있습니다."
    나는 생각했다. 'cd를 써서 git bash로 들어가봐야지'
    
    

* 다음과 같은 이차방정식이 있을 때 근을 찾는 수식을 파이썬 코드를 이용하여 출력해보시오.
x^2 + 4x - 21


```python
x = -100
while x**2 + 4*x - 21 != 0:
    x = x + 1
print(x)
```

    -7
    


```python
print(-2 + ((4 + 21) ** (1/2))); print(-2 - ((4 + 21) ** (1/2)))
```

    3.0
    -7.0
    


```python
a = 1
b = 4
c = -21
```


```python
x1 = (-b + (b*b - 4*a*c) ** 0.5)/(2/a)
x2 = (-b - (b*b - 4*a*c) ** 0.5)/(2/a)
print(x1)
print(x2)
```

    3.0
    -7.0
    

# Python 1.  프로그래밍 기초(Homework)

1. Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요. 


```python
import pprint
import keyword
pprint.pprint(keyword.kwlist)
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
    

2. 파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다.(floating point rounding error)
따라서, 아래의 값을 비교하기 위해 작성해야 하는 코드를 작성하세요.
a = 0.1 * 3
b = 0.3


```python
a = 0.1 * 3
b = 0.3
print(type(a))
print(type(b))
round(a,1) == round(b,1)
```

    <class 'float'>
    <class 'float'>
    




    True




```python
a = 0.1 * 3
b = 0.3
abs(a-b) <= 1e-10
```




    True




```python
import math
math.isclose(a, b)
```




    True



3. 이스케이프 문자열 중 1) 줄바꿈 2) 탭 3) \을 작성하세요


```python
print('이스케이프', end='\n')
print('줄바꿈')
print('이스케이프', end='\t')
print('탭')
print('\'이스케이프\'')
```

    이스케이프
    줄바꿈
    이스케이프	탭
    '이스케이프'
    

4. "안녕, 철수야"를 String Interpolation을 사용하여 출력하세요.
print(name = "철수")


```python
name = '철수'
print(f'안녕, {name}야')
print('안녕, {}야'.format(name))
```

    안녕, 철수야
    안녕, 철수야
    

5. 다음 중 형변환시 오류가 발생하는 것은?
1) str(1) 2) int('30')
3) int(5) 4) bool('50')
5) int('3.5')
=> 5)번; 문자열은 int형으로 형변환 불가


```python
str(1)
int('30')
int(
True5)
bool('50')
```




    True


