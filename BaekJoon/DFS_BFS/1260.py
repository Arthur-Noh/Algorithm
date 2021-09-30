# DFS/BFS 문제
# 백준 1260번
# 등급 실버 2

# 문제 해결 아이디어
# 일반적인 DFS와 BFS로 풀이하면 된다.

from collections import deque
import sys


def bfs(v):
    q = deque()
    q.append(v)
    visit_bfs[v] = 1
    while q:
        v = q.popleft()
        sys.stdout.write("{0} ".format(v))

        for i in range(1, n+1):
            if visit_bfs[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_bfs[i] = 1


def dfs(v):
    visit_dfs[v] = 1
    sys.stdout.write("{0} ".format(v))

    for i in range(1, n + 1):
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


# 정점의 개수 N, 간선의 개수 M, 시작 정점 번호 V
n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_dfs = [0] * (n + 1)
visit_bfs = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
