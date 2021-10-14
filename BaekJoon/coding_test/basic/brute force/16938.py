# 코딩 테스트 준비 - 기초
# 백준 16938 캠프 준비
# 등급 골드 4

# 문제 해결 아이디어
# 이 문제는 DFS로 해결할 수 있다.
# 먼저 입력 다 받고
# 합계가 L 보다 크고 S 보다 작으면서, 최댓값에서 최솟값을 뺀 값이 X보다 큰 경우
# 한번 세어주면 된다.
# DFS로 계속 인덱스에 해당하는 값을 더해주면서 최댓값인 R을 넘어서는 순간
# return을 하여 종료하면 된다.
# 그 이외에는 계속 dfs를 수행하여 다음 값을 찾는다.

import sys

# 문제의 갯수 : N
# 난이도의 합(최소) : L
# 난이도의 합(최대) : R
# 난이도의 차 : X
n, l, r, x = map(int, sys.stdin.readline().split())

# 문제의 난이도 입력
diff = list(map(int, sys.stdin.readline().split()))

# 가능한 경우의 수
count = 0


def dfs(idx, s, min_n, max_n):
    global count
    if l <= s <= r and max_n - min_n >= x:
        count += 1

    if s > r:
        return

    for next_idx in range(idx + 1, n):
        dfs(next_idx, s + diff[next_idx], min(min_n, diff[next_idx]), max(max_n, diff[next_idx]))


dfs(-1, 0, 10**6 + 1, 0)
print(count)
