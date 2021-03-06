# 코딩 테스트 준비 - 기초
# 백준 13398 연속합 2
# 등급 골드 5

# 문제 해결 아이디어
# 두가지 경우로 나눠서 생각한다.
# 1. 특정 원소를 제거하지 않고 최대 연속합을 구하는 dp
# 2. 특정 원소를 제거하고 최대 연속합을 구하는 dp
# 1의 경우 그냥 풀이하면 되지만, 2의 경우 잘 생각해봐야 한다.

# 2도 두가지로 나눠서 생각할 수 있는데
# 2-1. i번째 원소를 제거하고 최대 연속합을 구하는 dp
# 2-2. i번째 이전에 원소를 제거하고 i번째 원소를 더하는 dp
# 2-1의 경우 이것은 1에서 구한 값과 동일하다.
# 2-2의 경우 2-1에서 구하고 제거된 리스트에서 원소를 더한 값과 같다.

# 점화식으로 표현하면
# dp[0][i] : 특정 원소를 제거하지 않은 리스트
# dp[1][i] : 특정 원소를 제거한 리스트
# 1. dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i - 1])
# 2. dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])


import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우
dp = [[0] * n for _ in range(2)]

dp[0][0] = arr[0]

# N이 1인 경우 원소가 하나밖에 없으므로 바로 출력
if n == 1:
    print(dp[0][0])

else:
    result = -1001

    for i in range(1, n):
        # 아무런 원소를 제거하지 않았을 때, (이전까지의 연속합 + i 번째 원소)와 (i번째 원소)를 비교하여 큰 값을 대입
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])

        # 특정 원소를 제거하는 경우
        # 1. i번째 원소를 제거하는 경우
        # dp[0][i - 1]
        # 2. i번째 이전에서 이미 특정원소를 제거하여 i번째 원소를 선택하는 경우
        # dp[1][i - 1] + arr[i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

        # dp 진행중 가장 큰 값으로 갱신한다.
        result = max(result, dp[0][i], dp[1][i])

    print(result)
