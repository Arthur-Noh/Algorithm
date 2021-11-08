# 코딩 테스트 준비 - 기초
# 백준 15990 1, 2, 3 더하기 5
# 등급 실버 2

# 문제 해결 아이디어
# 같은 수를 두 번 이상 연속해서 사용하면 안된다.
# dp[1] dp[2] dp[3]에 각각 1, 2, 3으로 끝나는 상황을 넣는다.
# ex) dp[3]은
# 2 1
# 1 2
# 3
# 이 예시와 같이 끝나는 숫자가 1일때 2일때 3일때 각각 1개씩 이다.

# 그 후
# n이 만약 6인 상황에서
# dp[5]에서 2로 끝난거에 +1을 해주거나, 3으로 끝난거에 +1을 해주면 -> dp[6][0]
# dp[4]에서 1로 끝난거에 +2 또는 +3으로 끝난거에 +2 -> dp[6][1]
# dp[3]에서 1 또는 2로 끝난거에 +3 을 해주면 -> dp[6][2]

# 정리하면
# dp[i][0] = dp[i - 1][1] + dp[i - 2][2]
# dp[i][1] = dp[i - 2][0] + dp[i - 2][2]
# dp[i][2] = dp[i - 3][0] + dp[i - 3][1]

# 2차원으로 쪼개서 생각해야 한다.
# 1, 2, 3으로 끝난 갯수를 세고 그 뒤에 해당하는 숫자를 붙이면 된다.

import sys
t = int(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(3)] for i in range(100001)]
m = 1000000009

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 6 일 때 만약에
    # 5에서 2와 3으로 끝난거에 1 붙이기
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % m
    # 4에서 1과 3으로 끝난거에 2 붙이기
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % m
    # 3에서 1과 2로 끝난거에 3 붙이기
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % m

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(sum(dp[n]) % m)
