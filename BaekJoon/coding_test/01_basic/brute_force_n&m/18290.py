# 코딩 테스트 준비 - 기초
# 백준 18290 NM과 K(1)
# 등급 실버 1

# 문제 해결 아이디어
# 백 트래킹으로 해결할 수 있다.
# 근데 자꾸 시간 초과가 발생하는데, 이 시간 초과를 해결하는 방법은 중복해서 계산하는 방법을 없애는 것이다.
# 같은 행에서도 중복 선택을 피하기 위해 이전에 선택한 행과 같은 행인 경우와 아닌 경우로 나눌 수 있다.

import sys

n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 1]

result = -10 ** 6


def dfs(px, py, index, sum):
    if index == k:
        global result
        result = max(result, sum)
        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            # 현재 위치를 방문했는지 확인한다.
            if visited[x][y]:
                continue

            ok = True
            
            # 상하좌우로 방문 했는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False
            
            # 방문하지 않았다면
            if ok:
                visited[x][y] = True
                dfs(x, y, index + 1, sum + board[x][y])
                visited[x][y] = False


dfs(0, 0, 0, 0)

print(result)
