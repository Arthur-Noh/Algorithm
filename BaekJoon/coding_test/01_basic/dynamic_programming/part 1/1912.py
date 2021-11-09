# 코딩 테스트 준비 - 기초
# 백준 1912 연속합
# 등급 실버 2

# 문제 해결 아이디어
# 왼쪽부터 차례대로 더해가면서 큰 숫자가 나올 경우 dp 에 넣어주면 된다.
# dp의 0번째 인덱스에는 비교를 위해 numbers의 첫번째 값을 넣어준다.
# dp[i]와 numbers[i + 1]의 숫자를 합한 값과 그냥 numbers[i + 1]값을 비교하고
# 더 큰 값을 dp에 저장한다.
# 그리고 dp 에서 가장 큰 값을 출력한다.

import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [numbers[0]]

for i in range(n - 1):
    dp.append(max(dp[i] + numbers[i + 1], numbers[i + 1]))

print(max(dp))
