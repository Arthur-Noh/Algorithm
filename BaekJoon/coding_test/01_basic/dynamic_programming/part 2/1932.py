# 코딩 테스트 준비 - 기초
# 백준 1932 정수 삼각형
# 등급 실버 1

# 문제 해결 아이디어
# 간단하게 생각하면 된다.
# 삼각형의 꼭대기부터 차례대로 내려오면서 경로에 있는 최댓값을 저장시킨다.
# 맨 아래층 까지 내려온 후 max값을 출력하기만 하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
t = []

for i in range(n):
    t.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i][j]+ t[i - 1][j], t[i][j] + t[i - 1][j - 1])

print(max(t[n - 1]))
