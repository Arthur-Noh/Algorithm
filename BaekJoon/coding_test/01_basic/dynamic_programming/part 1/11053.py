# 코딩 테스트 준비 - 기초
# 백준 11053 가장 긴 증가하는 부분 수열
# 등급 실버 2

# 문제 해결 아이디어
# 첫 번째 인덱스부터 수열의 길이를 최댓값을 저장해 나간다.
# 수열 A = {10, 20, 10, 30, 20, 50}이 있을 때, 4번째 숫자 30까지의 수열 길이의 최댓값을 구해보자.
# 첫 번째 숫자부터 검사를 해 나간다.
# 자기 자신(30)보다 작은 숫자들 중에서 가장 큰 길이를 구하고 그 길이에 +1 을 하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
