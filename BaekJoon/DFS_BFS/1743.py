# DFS/BFS 문제
# 백준 1743번
# 등급 실버 1

# 문제 해결 아이디어
# 음식물 쓰레기가 있는 좌표를 1로 표기하고, graph에서 완전 탐색을 수행한다.
# 만약 1이 있는 경우 BFS 를 실행한다.
# 상, 하, 좌, 우를 비교하며 1이 있는 경우, 큐에 계속 값을 넣어 count 를 증가시킨다.
# BFS 종료 후, count와 최대값을 비교하여 result에 넣는다.

import sys
from collections import deque

# N, M, K 입력
n, m, k = map(int, sys.stdin.readline().split())

# 그래프
graph = [[0] * m for _ in range(n)]

# 방문 체크
visit = [[0] * m for _ in range(n)]

# 쓰레기의 위치 입력
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1

# 이동 방향 입력 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0  # 총 쓰레기의 갯수
v = 0  # 쓰레기의 갯수


def bfs(x, y):
    global v  # 쓰레기의 갯수, 편하게 전역변수로 선언한다.

    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    v += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                v += 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)
            result = max(result, v)
            v = 0

print(result)
