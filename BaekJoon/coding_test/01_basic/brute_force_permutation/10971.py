# 코딩 테스트 준비 - 기초
# 백준 10971 외판원 순회 2
# 등급 실버 2

# 문제 해결 아이디어
# TSP 문제
# 여러 도시들이 있고 한 도시에서 다른 도시로 이동하는 비용이 모두 주어졌을 때,
# 모든 도시들을 단 한번만 방문하고 원래 시작 지점으로 돌아오는 최소 비용의 이동 순서를 구하라
# 1. 각 번호에서 출발하여 제자리로 돌아오는 값을 구한다.
# 2. 1번 과정을 반복하면서 최솟값을 업데이트 한다.

import sys
n = int(sys.stdin.readline().rstrip())
travel = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = sys.maxsize


def dfs(start, next, value, visited):
    global result

    if len(visited) == n:
        if travel[next][start] != 0:
            result = min(result, value + travel[next][start])
        return

    for i in range(n):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()


for i in range(n):
    dfs(i, i, 0, [i])

print(result)
