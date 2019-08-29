# 파일명 및 함수명을 변경하지 마시오.
def summary(word):
    """
    아래에 코드를 작성하시오.
    word는 알파벳으로 구성되어 있습니다.
    요약된 문자열을 반환합니다.
    """
    for idx in range(len(word)):  # 문자의 길이만큼 반복
        if idx == 0:  # 첫번째 문자일 때는result, prev, count 초기값을 설정
            result = word[0] # 결과값을 저장
            prev = word[0]  # 이전 문자
            count = 1  # 문자의 개수
        else:
            if word[idx] == prev:  # 이전 문자와 비교하여 같다면 count를 1 늘림
                count += 1
            else:  # 다르면 result에 count 값과 새로운 문자 값을 추가
                result += str(count) + word[idx]
                count = 1  # count를 1로 초기화시킴
            prev = word[idx]  # 비교를 위한 prev를 현재 문자로 설정
    result += str(count)  # 반복을 마친 뒤 미쳐 저장하지 못한 마지막 문자의 개수를 추가
    return result


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))
