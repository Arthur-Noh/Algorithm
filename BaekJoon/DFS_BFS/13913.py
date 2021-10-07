# DFS/BFS 문제
# 백준 13549번
# 등급 골드 5

# 문제 해결 아이디어
# BFS로 해결할 수 있다.
# 전에 있던 위치로 돌아가기 위해서 2차원 배열을 사용한다. visited
# 전에 했던 숨바꼭질 문제와 동일하게 해결하되
# visited[i][0]에는 이동 횟수를 저장하고
# visited[i][1]에는 이동 전의 위치를 기억 하도록 한다.

# 마지막에 visited[k][1]을 새로운 큐에 저장하여
# k값에 x값을 대입하여 전의 위치를 찾도록 한다.

from collections import deque
import sys

# 수빈이의 위치 n, 동생의 위치 k
n, k = map(int, sys.stdin.readline().rstrip())
MAX_SIZE = 10 ** 5 + 1
visited = [[-1, -1] for _ in range(MAX_SIZE)]


def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s][0] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[k][0]

        for i in (x * 2, x - 1, x + 1):
            if 0 <= i < MAX_SIZE and visited[i][0] == -1:
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = x
                queue.append(i)


print(bfs(n))

li = deque()
li.append(k)

while True:
    if visited[k][1] != -1:
        li.appendleft(visited[k][1])
        k = visited[k][1]
    else:
        break

for _ in range(len(li)):
    sys.stdout.write("{0} ".format(li[_]))
