
# Python2. 데이터구조(Workshop)

## Problem

두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.


```python
# 문제
n = 5
m = 9
for i in range(m):
    for j in range(n):
        print('*', end='')
    print('')
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
    

과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.


```python
# 문제
student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
print(f'평균 점수는 {sum(student.values())/len(student.keys())}')
```

    평균 점수는 87.75
    

다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여 key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.


```python
# 문제
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
my_dict = {'A' : 0, 'B' : 0, 'AB' : 0, 'O' : 0}
for key in blood_types:
    if key == 'A':
        my_dict[key] += 1
    elif key == 'B':
        my_dict[key] += 1
    elif key == 'AB':
        my_dict[key] += 1
    else:
        my_dict[key] += 1
print(my_dict)
```

    {'A': 3, 'B': 3, 'AB': 3, 'O': 3}
    

# Python 2. 데이터구조(homework)

1. 아래 보기 중, 변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 분류하시오.
String List Tuple Range Set Dictionary

1) mutable   : List, Set, Dictionary(value)

2) immutable : String, Tuple, Range, Dictionary(key)

2. range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.


```python
number = range(51)
print(list(number[1::2]))
```

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    

3. 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.


```python
student = {'서현택' : 27, '최무연' : 28, '조선행' : 27, '송지영' : 26, '최성철' : 26, '박진희': 28}
print(student.keys())
print(student.values())
```

    dict_keys(['서현택', '최무연', '조선행', '송지영', '최성철', '박진희'])
    dict_values([27, 28, 27, 26, 26, 28])
    
