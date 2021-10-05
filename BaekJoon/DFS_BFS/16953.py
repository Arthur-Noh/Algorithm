# DFS/BFS 문제
# 백준 16953번
# 등급 실버 1

# 문제 해결 아이디어
# BFS로 해결할 수 있다.
# BFS로 해결 가능한 모든 경우의 수를 체크하면 되는 문제이다.

from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())

def bfs(z):
    queue = deque()
    queue.append((z, 1))

    while queue:
        x, count = queue.popleft()

        if x == b:
            return count # 두 값이 같아지면 반환

        # 해석
        # 만약 a 를 2배 한 값이 b보다 작다면 다시 queue에 입력
        # 만약 a 를 2배 한 값이 b보다 커서
        # a 뒤에 1을 붙인 값이 b보다 작은 경우 queue에 입력
        for i in (x * 2, int(str(x) + "1")):
            if 0 <= i <= b:
                queue.append((i, count+1))
                print(queue)

    return -1 # 만약 만들 수 없고 큐가 비는 경우 -1을 돌려준다.


print(bfs(a))
