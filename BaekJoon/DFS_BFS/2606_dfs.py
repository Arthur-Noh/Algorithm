# DFS/BFS 문제
# 백준 2606번
# 등급 실버 3

# 문제 해결 아이디어
# 이 문제는 DFS/BFS 모두 해결할 수 있다.
# DFS 로 해결해 보자
# 이 문제는 일반적인 그래프 방식으로 해결 하면 된다.
# 입력받은 컴퓨터의 수 N 크기의 그래프를 작성하여 0으로 초기화 하고
# 다음으로 입력받는 쌍의 위치마다 1로 초기화를 한다.
# dfs를 선언하여, 그래프가 서로 연결되어 있으면서 방문 visit가 0인 경우에
# visit 를 1로 바꾸고
# 마지막에 방문된 1의 갯수를 세어주면 된다.

import sys
# 컴퓨터의 갯수 n, 연결된 컴퓨터의 쌍 t
n = int(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())

# 일일히 쌍으로 입력 받는 것도 괜찮지만
# ex) [1, 2], [2, 3] .. 등등
# 그냥 n * n의 지도를 만들어서 연결되면 1, 아니면 0으로 정의하는 것이 더 편하다.
s = [[0] * n for _ in range(n)]
visit = [0 for _ in range(n)] # 바이러스에 감염 되면 1로 바뀔 것이다.

for i in range(t): # 해당하는 위치에 1로 변경
    a, b = map(int, sys.stdin.readline().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1


def dfs(v):
    visit[v] = 1
    for i in range(n):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)


dfs(0)
count = 0

for i in range(1, n): # 0번째 컴퓨터를 제외한 나머지 컴퓨터의 웜 바이러스 수
    if visit[i] == 1:
        count += 1

print(count)
