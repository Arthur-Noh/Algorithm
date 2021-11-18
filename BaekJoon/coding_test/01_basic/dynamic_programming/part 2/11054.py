# 코딩 테스트 준비 - 기초
# 백준 11054 가장 긴 바이토닉 부분 수열
# 등급 골드 5

# 문제 해결 아이디어
# 어렵게 생각하지 말고 왼쪽, 오른쪽으로 증가하는 수열의 길이를 각각 계산하고
# 그 길이를 가진 리스트의 둘의 합을 구하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

increase = [1] * n  # 왼쪽에서 증가하는 수열 dp
decrease = [1] * n  # 오른쪽에서 증가하는 수열 dp
result = [0] * n

# 왼쪽에서 증가하는 수열
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and increase[i] < increase[j] + 1:
            increase[i] = increase[j] + 1

# 오른쪽에서 증가하는 수열
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[i] > a[j] and decrease[i] < decrease[j] + 1:
            decrease[i] = decrease[j] + 1

# 두 리스트의 합을 구한다.
# 단 자기자신을 포함한 길이를 쟀기 때문에
# 각각에서 -1 을 해주면 된다.
for i in range(n):
    result[i] = increase[i] + decrease[i] - 1

print(max(result))
