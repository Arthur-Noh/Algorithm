# 코딩 테스트 준비 - 기초
# 백준 9095 1, 2, 3 더하기
# 등급 실버 3

# 문제 해결 아이디어
# 1 = 1 - 1개
# 2 = 1 + 1, 2 - 2개
# 3 = 1 + 1 + 1, 1 + 2, 2 + 1, 3 - 4개
# 4 = 1 + 1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 2 + 2, 3 + 1, 1 + 3 - 7개
# n = (n - 1) + (n - 2) + (n - 3) 의 경우의 수 합과 같다.

import sys
t = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2, 4]

for i in range(4, 12):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])
