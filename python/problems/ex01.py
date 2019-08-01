# 파일명 및 함수명을 변경하지 마시오.
def positive_sum(numbers):
    """
    여기에 코드를 작성하시오.
    numbers는 숫자들이 담긴 리스트입니다.
    numbers에 담긴 숫자들 중, 양의 정수들의 합을 반환합니다.
    """
    result = 0
    for idx in numbers:
        if idx > 0:
            result += idx
    return result







# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(positive_sum([1, -4, 7, 12])) #=> 20
    print(positive_sum([-1, -2, -3, -4])) #=> 0