# 코딩 테스트 준비 - 기초
# 백준 1699 제곱수의 합
# 등급 실버 2

# 문제 해결 아이디어
# N을 제곱수들의 합으로 표현하는데, 그 제곱수들의 최소 갯수를 구하는 프로그램을 작성하라
# dp는 제곱수 합의 최소 갯수를 저장하는 리스트이다.
# 점화식은 i가 숫자, j 가 i보다 작거나 같은 제곱수라고 했을때
# dp[i] = min(dp[i-j]) + 1
# 예를들어 i 가 16이라고 했을때 i 보다 작거나 같은 제곱수는 1, 4, 9, 16이다.
# dp[i - 1], dp[i - 4], dp[i - 9], dp[i - 16] 중 가장 작은 값은 dp[i - 16] = 0이고
# 여기에 1을 더한 값을 dp[i]에 넣어준다.

import sys
n = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(n + 1)]
square = [i * i for i in range(1, 317)]

for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1

print(dp[n])
