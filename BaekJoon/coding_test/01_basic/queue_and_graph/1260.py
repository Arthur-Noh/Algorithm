# 코딩 테스트 준비 - 기초
# 백준 1260 DFS와 BFS
# 등급 실버 2

# 문제 해결 아이디어
# 기본적인 DFS와 BFS로 해결하면 된다.

from collections import deque
import sys

# 정점의 개수 N, 간선의 개수 M, 탐색 시작 V
n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_dfs = [0] * (n + 1)
visit_bfs = [0] * (n + 1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


def bfs(v):
    q = deque()
    q.append(v)
    visit_bfs[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n + 1):
            if visit_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_bfs[i] = 1


def dfs(v):
    visit_dfs[v] = 1
    print(v, end=' ')

    for i in range(1, n + 1):
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


dfs(v)
print()
bfs(v)
