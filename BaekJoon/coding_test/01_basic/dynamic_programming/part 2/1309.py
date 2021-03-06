# 코딩 테스트 준비 - 기초
# 백준 1309 동물원
# 등급 실버 1

# 문제 해결 아이디어
# 사실 규칙을 찾아서 풀이해도 된다.
# N = 1, 2, 3, 4 ... 일때 경우의 수는 [3, 7, 17, 41 ...] 이다
# 점화식 : dp[i] = 2 * dp[i - 1] + dp[i - 2]

# 그게 아니라면 2차원 배열을 만들어 해결하면 된다.
# s[n][0], s[n][1], s[n][2] 이렇게 세가지로 나눈다.
# s[n][0]는 두칸 중에 사자가 왼쪽에 있는 경우
# s[n][1]은 두칸 중에 사자가 오른쪽에 있는 경우
# s[n][2]는 사자가 없는 경우를 구해준다.

import sys
n = int(sys.stdin.readline().rstrip())
dp = [[0] * 3 for i in range(100001)]

# 동물원의 우리가 (1, 2) 크기, N = 1일 때
# 사자가 왼쪽, 오른쪽, 없는 경우 3개밖에 없으므로 각각 1로 초기화를 해준다.
for i in range(3):
    dp[1][i] = 1

# 사자가 대각선으로만 겹치거나 없으면 되므로 아예 없는 경우는 이전에 없던 경우도 합쳐주면 된다.
for i in range(2, n + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901

print(sum(dp[n]) % 9901)
