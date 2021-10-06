# DFS/BFS 문제
# 백준 13549번
# 등급 골드 5

# 문제 해결 아이디어
# BFS로 해결할 수 있다.
# 이 문제에서는 순간이동은 0초, 이동은 1초가 걸린다.
# x + 1, x - 1 : 1초
# x * 2 : 0초

# 따라서 두 값을 나눠서 순간이동에는 시간이 걸리지 않게 식을 먼저 작성하면 된다.
from collections import deque
import sys

# 수빈이의 위치 n, 동생의 위치 k
n, k = map(int, sys.stdin.readline().split())
MAX_SIZE = 10 ** 5 + 1
visited = [-1] * MAX_SIZE


def bfs():
    queue = deque()
    queue.append(n)
    visited[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[k]

        if 0 <= x * 2 < MAX_SIZE and visited[x * 2] == -1: # x * 2한 값이 범위 사이에 있으며, 처음 방문인 경우
            visited[x * 2] = visited[x] # 방문하는데 0초가 걸리므로 그 값을 그대로 넣어주면 된다.
            queue.append(x * 2)

        for i in (x - 1, x + 1): # 이게 -와 + 의 순서를 바꾸면 틀렸다고 백준에서 인식함
            if 0 <= i < MAX_SIZE and visited[i] == -1:
                visited[i] = visited[x] + 1 # 방문하는데 1초가 걸리므로 그 값을 더해주면 된다.
                queue.append(i)


print(bfs())
