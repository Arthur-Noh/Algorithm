# DFS/BFS 문제
# 백준 2178번
# 등급 실버 1

# 문제 해결 아이디어
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸의 수를 구하여라
# 이 문제는 BFS를 활용하여 해결할 수 있다.
# BFS는 시작지점에서 가장 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일하다.
# 따라서 (1,1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리값을 기록하면 해결할 수 있다.

from collections import deque
import sys


# BFS로 풀이하면 된다.
def bfs(x, y):
    # 큐(Queue) 구현을 위해서 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재의 위치에서 4가지 방향으로의 위치를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간을 벗어난 경우는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 미로 벽에 부딛힌 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드에 처음 방문하는 경우에만 최단거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


# N, M 입력
n, m = map(int, sys.stdin.readline().split())

# 미로 입력
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# 이동 할 좌표 상, 하, 좌, 우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로 찾기 출력
print(bfs(0, 0))
