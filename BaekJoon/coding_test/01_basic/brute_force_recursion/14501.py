# 코딩 테스트 준비 - 기초
# 백준 14501 퇴사
# 등급 실버 3

# 문제 해결 아이디어
# 부르트 포스로 해결 한다면, 백트래킹으로 해결할 수 있을 것 같다.
# 1. 상담을 한다. : dfs(day + t[day], s + p[day])
# - 현재 날짜에서 상담에 걸리는 날을 더해준다.
# - 상담후 얻을 수 있는 수익을 더해준다.
# 2. 상담을 안한다. : dfs(day + 1, s)
# - 현재 날짜에 하루를 더해준다.
# - 상담 후 얻을 수 있는 수익을 그대로 다시 전달한다.
# 3. 정답을 찾은 경우 : day == n + 1
# - 현재 날짜가 퇴사일과 동일한 경우에만 합계 s의 최대값을 비교하여 전달한다.
# 4. 불가능한 경우 : day > n + 1
# - 그냥 return 해준다.


import sys
# 입력 받기
# n + 1 일에 퇴사하므로 편의상 0번 값을 사용 안한다.
n = int(sys.stdin.readline().rstrip())
t = [0] * (n + 1)
p = [0] * (n + 1)
result = 0

# 각각 값을 입력 받는다.
# 편의상 리스트의 첫번째 값[0]을 사용하지 않는다.
for i in range(1, n + 1):
    t[i], p[i] = map(int, sys.stdin.readline().split())


def dfs(day, s):  # 날짜와 합계s 를 dfs의 인자 값으로 입력 받는다.
    global result

    # 종료 조건 : 퇴사일과 같다면
    if day == n + 1:
        result = max(result, s)
        return

    # 불가능한 경우 : 퇴사일을 넘는 경우
    if day > n + 1:
        return

    # 상담을 한다.
    dfs(day + t[day], s + p[day])

    # 상담을 안한다.
    dfs(day + 1, s)


dfs(1, 0)
print(result)
