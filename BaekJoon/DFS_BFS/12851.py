# DFS/BFS 문제
# 백준 12581번
# 등급 골드 5

# 문제 해결 아이디어
# BFS로 해결할 수 있다.
# BFS로 해결 가능한 모든 경우의 수를 체크하면 되는 문제이다.

# visited[i][0] : 가장 빠른 시간
# visited[i][1] : 방법의 수

# 참고 : https://it-garden.tistory.com/345

from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())
MAX_SIZE = 10 ** 5 + 1
visited = [[-1, 0] for _ in range(MAX_SIZE)]


def bfs(n):
    queue = deque()
    queue.append(n)

    visited[n][0] = 0
    visited[n][1] = 1

    while queue:
        x = queue.popleft()

        for i in (x + 1, x - 1, x * 2):
            if 0 <= i < MAX_SIZE:
                if visited[i][0] == -1:  # 처음 방문하는 경우
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    queue.append(i)

                elif visited[i][0] == visited[x][0] + 1:  # 한 번 이상 방문하는 경우
                    visited[i][1] += visited[x][1]  # 방법을 더해준다.


bfs(a)
sys.stdout.write("{0}\n".format(visited[b][0]))
sys.stdout.write("{0}\n".format(visited[b][1]))
