# 코딩 테스트 준비 - 기초
# 백준 11724 연결 요소의 개수
# 등급 실버 2

# 문제 해결 아이디어
# dfs로 해결하면 된다.
# 파이썬은 최대 재귀 횟수가 1000회 이기 때문에 반드시 sys.setrecursionlimit(10000)를 써줘야 한다. 

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
graph[0] = [0, 0]
visited = [False] * (n + 1)

count = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
