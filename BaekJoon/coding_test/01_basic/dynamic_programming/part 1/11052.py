# 코딩 테스트 준비 - 기초
# 백준 11052 카드 구매하기
# 등급 실버 1

# 문제 해결 아이디어
# 카드 등급은 별로 중요하지 않고 카드팩과 금액이 중요하다
# N 개의 카드까지의 최대 비용을 저장한 DP 리스트를 생성한다.
# dp[1]의 값은 money[1]의 값과 동일하다. (한장을 사는 경우는 하나밖에 없으므로)
# dp[1] = money[1] 
# dp[2] = dp[1] + money[1] or money[2]
# dp[3] = dp[2] + money[1] or dp[1] + money[2] or money[3]
# dp[4] = dp[3] + money[1] or dp[2] + money[2] or dp[1] + money[3] or money[4]
# 점화식
# dp[i] = dp[i - j] + money[j] 이 생성된다.

import sys

# 구매하려는 카드의 개수 N
n = int(sys.stdin.readline().rstrip())

# 카드팩의 금액
# 문제의 편의상 0번째 항의 값은 사용하지 않도록 0으로 초기화를 한다.
money = [0] + list(map(int, sys.stdin.readline().split()))

# 구매한 카드의 최대 비용을 저장한 리스트
# 0번째 항의 값을 사용하지 않기 위해 n + 1개를 만들어 준다.
dp = [0] * (n + 1)

# 1개를 구매하는데 최댓값은 1개 카드팩 가격 밖에 없으므로
dp[1] = money[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + money[j]:
            dp[i] = dp[i - j] + money[j]

print(dp[n])
