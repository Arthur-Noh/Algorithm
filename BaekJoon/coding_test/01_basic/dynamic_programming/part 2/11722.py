# 코딩 테스트 준비 - 기초
# 백준 11722 가장 긴 감소하는 부분 수열
# 등급 실버 2

# 문제 해결 아이디어
# dp에는 각 자리에 올 수 있는 최대값을 담아준다.
# A  :  10  30  10  20  20  10
# dp :  1   1   2   2   2   3
# 자기 자신의 인덱스보다 작은 인덱스 숫자 중에서 자신보다 큰 값의 인덱스를 구해주고
# s 라는 리스트에 그 인덱스에 해당하는 dp 값을 넣어준다.
# s 리스트의 숫자 중 가장 큰 값에 +1 한 값을 넣어준다.

import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * n

for i in range(1, n):
    s = []
    for j in range(i):
        if a[i] < a[j]:
            s.append(dp[j])

    if not s:
        continue
    else:
        dp[i] += max(s)

print(max(dp))
