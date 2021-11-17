# 코딩 테스트 연습 - 프로그래머스
# 해시 - 위장
# 성공

# 문제 해결 아이디어
# 단순하게 생각하면 옷을 무엇을 입을지 경우의 수를 고르는 문제이다.

# 예시와 같이
# 머리 : 노랑모자, 녹색모자
# 안경 : 파란선글라스
# 이렇게 주어진 경우 이 옷들을 조합해서 입는 경우의 수는
# (2 + 1) * (1 + 1) = 6 가지 경우의 수가 나오게 된다.
# 1을 추가해서 경우를 더하는 이유는 입지 않았을 경우를 추가한 것이다.

# 그러나 이 총 6가지 경우의 수에서 '아무것도 입지 않았을 때'의 경우를 빼주면 된다.

clothes = [['yellowhat', 'headgear'],
           ['bluesunglasses', 'eyewear'],
           ['green_turban', 'headgear']]


def solution(clothes):
    answer = {}

    for c in clothes:
        if c[1] in answer :  # clothes는 이차원 배열이므로 두번째 열에 해당하는 값이 키값이 된다.
            answer[c[1]] += 1  # 이미 키 값이 존재하면 +1

        else:  # 키 값이 없고 처음 들어온 입력이라면
            answer[c[1]] = 1 # 1을 입력

    count = 1
    for i in answer.values():  # 각 키에 대한 값을 꺼내서 곱해준다.
        count *= (i + 1)

    return count - 1


print(solution(clothes))
