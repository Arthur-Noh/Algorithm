# 코딩 테스트 준비 - 기초
# 백준 9095 1, 2, 3 더하기
# 등급 실버 1

# 문제 해결 아이디어
# DP 문제이고 규칙을 살펴보면 된다.
# 1 = (1) - 1개
# 2 = (1 + 1), (2) - 2개
# 3 = (1 + 1 + 1), (1 + 2), (2 + 1), (3) - 4개
# 4 = (1 + 1 + 1 + 1), (1 + 1 + 2), (1 + 2 + 1), (2 + 1 + 1), (2 + 2), (1 + 3), (3 + 1) - 7개
# 4번째 경우의 수는 1, 2, 3 번째의 경우의 수를 합한 값과 같다.
# 따라서 5번째 경우의 수는 2, 3, 4 번째의 경우의 수를 합한 값과 같다.
# n이 3보다 클 때, f(n) = f(n - 1) + f(n - 2) + f(n - 3)

import sys
t = int(sys.stdin.readline().rstrip())


def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solve(n - 1) + solve(n - 2) + solve(n - 3)
    

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(solve(n))
