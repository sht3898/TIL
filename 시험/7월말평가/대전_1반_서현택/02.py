# 파일명 및 함수명을 변경하지 마시오.
def alphabet_count(word):
    """
    아래에 코드를 작성하시오.
    word는 소문자로만 구성되어 있습니다.
    알파벳을 key로, 갯수를 value로 가지는 딕셔너리를 반환합니다.
    """
    result = {}  # 결과값을 저장할 딕셔너리
    result_list = []  # 결과값을 저장할 때 필요한 값들만 골라내기 위한 리스트
    for char in word:  # word를 반복하며 해당 문자가 result_list에 있는지 확인
        if char not in result_list:  # 문자가 result_list에 없다면 삽입하고 result에는 해당 문자를 key, 1을 value로 하여 저장
            result_list.append(char)
            result[char] = 1
        else:  # 문자가 result_list에 있다면 result에 저장되어 있는 value 값을 1 증가
            result[char] += 1
    return result

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
