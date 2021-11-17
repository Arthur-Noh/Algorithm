# 코딩 테스트 준비 - 기초
# 백준 11055 가장 큰 증가 부분 수열
# 등급 실버 1

# 문제 해결 아이디어
# 수열 a = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8] 이라고 했을 때
# dp 에는 각자리에 올 수 잇는 가장 큰 값을 넣게 된다.
# dp = [1, 101, 3, 53, 113, 6, 11, 17, 24, 32]
# dp[i]에 오게될 값은 a[0] ~ a[i -1]의 값 중에 a[i]보다 작은 값의 인덱스를 구한 뒤
# 그 인덱스에 맞는 dp의 값 중에 가장 큰 값을 a[i]에 더하면 된다.
# 예를들어 dp[4]에 오게될 값을 구해보면
# a[0] 부터 a[3] 까지 ap[4] 보다 작은 값의 인덱스는 0(1), 2(2), 3(50) 이다.
# 이때 dp[0] = 1, dp[1] = 3. dp[3] = 53중 가장 큰 값은 53이므로
# dp[4] = a[4] + dp[3] 즉, dp[4] = 113

import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = a[0]

for i in range(1, n):
    s = []
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            s.append(dp[j])
    if not s:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + max(s)
        
print(max(dp))
