# 파일명 및 함수명을 변경하지 마시오.
def can_divide(numbers, divisor):
    """
    아래에 코드를 작성하시오.
    numbers는 0이 아닌 양의 정수가 담긴 리스트입니다.
    divisor는 0이 아닌 양의 정수입니다.
    numbers에 담겨있는 숫자들 중, divisor로 나누어 떨어지는 숫자들을 오름차순으로 정렬한 리스트를 반환합니다.
    """
    result_list = []  # 결과값을 저장할 리스트 생성
    for number in numbers:  # numbers를 반복하며 divisor로 나누어 지는 것들만 result_list에 저장
        if number % divisor == 0:
            result_list.append(number)
    if len(result_list) <= 0:  # result_list에 원소가 없어서 길이가 0보다 작다면 reuslt_list에 -1 저장
        result_list.append(-1)
    return sorted(result_list)  # result_list를 정렬하여 반환






# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(can_divide([20, 3, 5, 7], 5))
    print(can_divide([4, 3, 2, 1], 1))
    print(can_divide([7, 11, 13], 3))
