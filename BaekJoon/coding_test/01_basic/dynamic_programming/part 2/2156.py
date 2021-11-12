# 코딩 테스트 준비 - 기초
# 백준 2156 포도주 시식
# 등급 실버 1

# 문제 해결 아이디어
# dp를 N 번째 포도주 잔까지 마실때의 최댓값을 저장한 리스트로 하면 될 것 같다.
# 규칙 찾기
# dp[1] = w[1]
# dp[2] = w[1] + w[2]
# dp[3] = dp[2], dp[1] + w[3], w[2] + w[3]
# dp[4] = dp[3], dp[2] + w[4], dp[1] + w[3] + w[4]
# dp[5] = dp[4], dp[3] + w[5], dp[2] + w[4] + w[5]
# 점화식
# dp[i] = max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i])
# 또 포도주의 갯수가 2개 이하라면 그냥 그 두 값을 합친게 최종 값이 된다.

import sys
n = int(sys.stdin.readline().rstrip())
w = [0]
dp = [0]

for i in range(n):
    w.append(int(sys.stdin.readline().rstrip()))

if len(w) < 4:
    print(sum(w))

else:
    dp.append(w[1])
    dp.append(w[1] + w[2])

    for i in range(3, n + 1):
        dp.append(max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i]))

    print(dp[n])
