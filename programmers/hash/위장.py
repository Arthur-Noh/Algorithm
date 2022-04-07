# 프로그래머스
# 코딩테스트 고득점 Kit
# 해시 : 위장

# 문제 해결 아이디어
# 해시로 접근하기보다는, 조합의 갯수를 세는 수학 문제로 생각하면 좋을 것 같다.
# 만약에
# 얼굴에 안경, 선글라스
# 바지에 청바지, 반바지
# 이런 경우가 있다면
# 조합의 갯수는 3 * 3 = 9 개가 나온다. ( 3인 이유는 안경, 선글라스, 아무것도 안낀 경우 )
# 근데 아예 아무거소 입지 않은 경우는 없다고 했으므로
# 총 조합의 갯수는 8개

# 코드는 입력받은 2차원 배열을 이름과 종류로 구분하고
# 구분된 종류들만 모아서 갯수를 센 후 곱하는 형식으로 진행하면 된다.


clothes = [
    ["yellohat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]


def solution(clothes):
    clothes_type = {}

    for name, kind in clothes:
        if kind in clothes_type:
            clothes_type[kind] += 1
        else:
            clothes_type[kind] = 1  # 처음 발견한 종류의 의상

    combination_count = 1

    for number in clothes_type.values():
        combination_count *= (number + 1)  # 의상을 입지 않은 경우를 포함하여 곱해준다.

    return combination_count - 1  # 모두 입지 않은 경우를 제외


print(solution(clothes))  # 정답 5
