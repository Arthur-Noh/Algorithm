# 코딩 테스트 준비 - 기초
# 백준 14501 퇴사
# 등급 실버 3

# 문제 해결 아이디어
# 이 문제는 DFS 백 트래킹으로도 해결할 수 있고
# DP로 해결할 수 있다.
# 이번에는 DP로 해결해보자
# 우선 6, 7일처럼 n을 넘어가면 안되기 때문에 dp[i + 1]의 값(최댓값)을 넣어준다.
# 예를 들어 i 가 4라고 한다면,
# dp[i + 1]의 값(0)과 p[i] + dp[i + t[i]](15 + 0)의 값 중 큰 값을 넣어준다.(dp[4] = 15)
# i 가 3이라고 한다면,
# dp[i + 1]의 값(15)과 p[i] + dp[i + t[i]](20 + 15)의 값 중 큰 값을 넣어준다.(dp[3] = 35)
# 이런식으로 최댓값을 넣어주면 i가 0일때 최댓값이 되므로
# dp[0]의 값을 출력해준다.

import sys
n = int(sys.stdin.readline().rstrip())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])
