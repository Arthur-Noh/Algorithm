# DFS/BFS 문제
# 백준 2606번
# 등급 실버 3

# 문제 해결 아이디어
# 이 문제는 DFS/BFS 모두 해결할 수 있다.
# BFS로 풀이해보자
# queue에 넣고 방문 했을때만 visited에 넣어 그 길이를 출력하도록 한다.

from collections import deque
import sys

# 컴퓨터의 갯수 n, 연결된 컴퓨터의 쌍의 수 t
n = int(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())

s = [[0] * n for _ in range(n)]

# 2차원 리스트에 넣어주기
# 해당하는 위치는 1이 된다.
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1


# BFS 함수
def bfs(s, start):
    queue = deque()
    queue.append(start)
    visited = []

    while queue:
        start = queue.popleft()
        visited.append(start) # 연결되는 컴퓨터의 인덱스 번호가 입력된다.

        for i in range(n):
            if s[start][i] and i not in visited and i not in queue:
                queue.append(i)

    return len(visited) # 연결된 컴퓨터의 인덱스의 갯수를 리턴한다.


print(bfs(s, 0) - 1)  # 1번째 컴퓨터는 항상 감염되어 있기 때문에 제외
