# 코딩 테스트 준비 - 기초
# 백준 1463 1로 만들기
# 등급 실버 3

# 문제 해결 아이디어
# 다이나믹 프로그래밍으로 해결할 수 있는 문제이다.
# 단순 조건으로는 (n/3, n/2, n -=1) 이 문제를 해결할 수 없다.
# 10 -> 5 -> 4 -> 3 -> 1 : 5회
# 10 -> 9 -> 3 -> 1 : 4회
# n/3 보다 n-1을 먼저 해줘야 최솟값이 나온다.

# n 이라는 수는 n//3을 연산전으로 돌리면, 즉 +1 하면 만들 수 있다.
# n 이라는 수는 n//2을 연산전으로 돌리면, 즉 +1 하면 만들 수 있다.
# n 이라는 수는 n -1을 연산전으로 돌리면, 즉 +1 하면 만들 수 잇다.

# 점화식
# dp(n) = min(dp(n//3) + 1, dp(n//2) + 1, dp(n - 1) + 1)

import sys
n = int(sys.stdin.readline().rstrip())
dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[n])